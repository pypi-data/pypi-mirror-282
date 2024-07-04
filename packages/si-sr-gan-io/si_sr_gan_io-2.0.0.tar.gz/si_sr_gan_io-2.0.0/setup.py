"""
    Setup file for si_sr_gan_io.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.0.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup, find_namespace_packages


if __name__ == "__main__":
    try:
        setup(
			use_scm_version={"version_scheme": "no-guess-dev"},
            packages=find_namespace_packages(where="src"),
            package_dir={"": "src"},
            include_package_data=True,
            package_data={
                "si_sr_gan_io.data.sentinel2": ["*.gpkg","*.csv","*.zip"],
                "si_sr_gan_io.data.venus": ["*.gpkg","*.csv","*.txt"],
            }
        )
    except:  # noqa
        print("\n\nAn error occurred while building the project, "
              "please ensure you have the most updated version of setuptools, "
              "setuptools_scm and wheel with:\n"
              "   pip install -U setuptools setuptools_scm wheel\n\n")
        raise
