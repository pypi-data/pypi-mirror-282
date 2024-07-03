import datetime
import os
from dataclasses import dataclass, field
from typing import Optional

import affine
import numpy as np
import pytest
import rasterio as rio
from pyproj import CRS

from si_sr_gan_io import ecostress_v2

ECOSTRESS_PRODUCT_NAME = 'ECOv002_L2T_LSTE_26870_001_28PCA_20230402T115902_0710_01'


def get_ecostress_v2_folder() -> str:
    """
    Retrieve ecostress folder from env var
    """
    return os.path.join(os.environ['si_sr_gan_io_TEST_DATA_PATH'], 'ecostress_v2',
                        ECOSTRESS_PRODUCT_NAME)


@pytest.mark.requires_test_data
def test_ecostressv2_instantiate():
    """
    Test Ecostress (collection v2) class instantiation 
    """
    ecostressv2_folder = get_ecostress_v2_folder()
    eco_ds = ecostress_v2.EcostressV2(ecostressv2_folder)

    assert eco_ds.product_dir == ecostressv2_folder
    assert eco_ds.product_name == ECOSTRESS_PRODUCT_NAME
    assert eco_ds.tile == '28PCA'
    assert eco_ds.date == datetime.date(2023, 4, 2)
    assert eco_ds.time == datetime.time(11, 59, 2)
    assert eco_ds.year == 2023
    assert eco_ds.day_of_year == 92
    assert eco_ds.bounds == rio.coords.BoundingBox(left=300000.0,
                                                   bottom=1490260.0,
                                                   right=409760.0,
                                                   top=1600020.0)
    assert eco_ds.transform == affine.Affine(70.0, 0.0, 300000.0, 0.0, -70.0, 1600020.0)
    assert eco_ds.crs == CRS.from_epsg(32628)


@dataclass(frozen=True)
class ReadAsNumpyParams:
    """
    Class to store read_as_numpy parameters
    """
    bands: list[ecostress_v2.EcostressV2.Band] = field(
        default_factory=lambda: ecostress_v2.EcostressV2.GROUP_ALL)
    masks: list[ecostress_v2.EcostressV2.Mask] = field(
        default_factory=lambda: ecostress_v2.EcostressV2.ALL_MASKS)
    crs: Optional[str] = None
    resolution: float = 70
    no_data_value: float = np.nan
    bounds: rio.coords.BoundingBox = None
    algorithm: rio.enums.Resampling = rio.enums.Resampling.cubic
    dtype: np.dtype = np.dtype('float32')

    def expected_shape(self) -> tuple[int, int]:
        """
        return expected shape
        """
        if self.bounds is not None:
            return (int(np.ceil((self.bounds[3] - self.bounds[1]) / self.resolution)),
                    int(np.ceil((self.bounds[2] - self.bounds[0]) / self.resolution)))

        return (int(10980 * 10 / self.resolution), int(10980 * 10 / self.resolution))


@pytest.mark.parametrize(
    "parameters",
    [
        ReadAsNumpyParams(),
        # Set a bounding bounding
        ReadAsNumpyParams(bounds=rio.coords.BoundingBox(400000.0, 1590000.0, 407000.0, 1597000.0)),
        # Set a different target crs
        ReadAsNumpyParams(bounds=rio.coords.BoundingBox(-16.2, 13.0, -15.2, 14.0),
                          crs='EPSG:4326',
                          resolution=0.01)
    ])
def test_read_as_numpy_and_xarray(parameters: ReadAsNumpyParams):
    """
    Test the read_as_numpy method
    """
    eco_ds = ecostress_v2.EcostressV2(get_ecostress_v2_folder())

    # Read as numpy part
    bands_arr, mask_arr, xcoords, ycoords, crs = eco_ds.read_as_numpy(**parameters.__dict__)

    assert bands_arr.shape == (len(parameters.bands), *parameters.expected_shape())
    assert mask_arr is not None and mask_arr.shape == (len(
        parameters.masks), *parameters.expected_shape())
    assert (~np.isnan(bands_arr)).sum() > 0

    assert ycoords.shape == (parameters.expected_shape()[0], )
    assert xcoords.shape == (parameters.expected_shape()[1], )

    if parameters.crs is not None:
        assert crs == parameters.crs

    # Test read as xarray part
    eco_xr = eco_ds.read_as_xarray(**parameters.__dict__)

    for c in ['t', 'x', 'y']:
        assert c in eco_xr.coords

    assert eco_xr['t'].shape == (1, )
    assert eco_xr['x'].shape == (parameters.expected_shape()[1], )
    assert eco_xr['y'].shape == (parameters.expected_shape()[0], )

    for band in parameters.bands:
        assert band.value in eco_xr.variables
        assert eco_xr[band.value].shape == (1, *parameters.expected_shape())

    assert eco_xr.attrs['tile'] == '28PCA'
    if parameters.crs is not None:
        assert eco_xr.attrs['crs'] == parameters.crs
