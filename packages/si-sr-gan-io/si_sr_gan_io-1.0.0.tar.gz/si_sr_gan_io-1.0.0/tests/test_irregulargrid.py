import numpy as np
import rasterio as rio
from si_sr_gan_io import irregulargrid, utils


def test_swath_resample():
    """
    Test the swath resample method
    """

    # Create WGS84 bounds from UTM 31N bounds
    bounds = rio.coords.BoundingBox(left=300000.0, bottom=4790220.0, right=409800.0, top=4900020.)
    crs = 'epsg:32631'
    wgs84_bounds = utils.bb_transform(crs, 'epsg:4326', bounds, all_corners=True)

    # Now generate irregularly sampled lat/lon
    lon_1d = np.array([
        wgs84_bounds.left + (wgs84_bounds.right - wgs84_bounds.left) / (1.5**p) for p in range(10)
    ])
    lat_1d = np.array([
        wgs84_bounds.bottom + (wgs84_bounds.top - wgs84_bounds.bottom) / (1.5**p) for p in range(10)
    ])

    # Generate 2d sampling grid
    lon_2d, lat_2d = np.meshgrid(lon_1d, lat_1d)

    nb_discrete_vars = 2
    nb_continuous_vars = 3

    continuous_vars = np.arange(lon_2d.shape[0] * lon_2d.shape[1] * nb_continuous_vars).reshape(
        *lon_2d.shape, nb_continuous_vars).astype(float)

    discrete_vars = np.arange(lon_2d.shape[0] * lon_2d.shape[1] * nb_discrete_vars).reshape(
        *lon_2d.shape, nb_discrete_vars)

    out_dv, out_cv, xcoords, ycoords = irregulargrid.swath_resample(
        lat_2d,
        lon_2d,
        target_crs=crs,
        target_bounds=bounds,
        target_resolution=100.,
        sigma=100.,
        discrete_variables=discrete_vars,
        continuous_variables=continuous_vars)

    assert out_cv.shape == (1098, 1098, nb_continuous_vars)
    assert out_dv.shape == (1098, 1098, nb_discrete_vars)
    assert xcoords.shape == (1098, )
    assert ycoords.shape == (1098, )

    assert (~np.isnan(out_cv)).sum() == 2970
    assert np.nanmax(out_cv) == 296.
    assert np.nanmin(out_cv) == 33.
