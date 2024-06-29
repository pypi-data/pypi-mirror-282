# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nfdata']

package_data = \
{'': ['*']}

install_requires = \
['Pint>=0.24.1,<0.25.0',
 'f90nml>=1.4.4,<2.0.0',
 'geopandas>=1.0.0,<2.0.0',
 'netCDF4>=1.7.1.post1,<2.0.0',
 'numpy>=2.0.0,<3.0.0',
 'pandas>=2.2.2,<3.0.0',
 'rasterio>=1.3.10,<2.0.0',
 'ruamel.yaml>=0.18.6,<0.19.0',
 'shapely>=2.0.4,<3.0.0']

entry_points = \
{'console_scripts': ['nfdata = nfdata.console:run']}

setup_kwargs = {
    'name': 'nfdata',
    'version': '0.1.0',
    'description': 'Compile and edit input data for the NanoFASE model',
    'long_description': '# NanoFASE Data\n\nThe NanoFASE Data module is a set of scripts to compile and edit input data for the [NanoFASE model](https://github.com/nerc-ceh/nanofase).\n\n[See the NanoFASE documentation for full documentation](https://nerc-ceh.github.io/nanofase/users/nanofase-data.html).\n\n*Still in development. Use with caution!*\n\n## Getting started\n\nThe easiest way to get started is to create a Conda environment using the provided [environment.yaml](./environment.yaml) file:\n\n```shell script\n$ conda env create -f environment.yaml\n$ activate nanofase-data\n```\n\nIf you don\'t want to use Conda, then this [environment.yaml](./environment.yaml) file lists the packages that need to be installed.\n\n## Usage\n\n```\nusage: nanofase_data.py [-h] [--output OUTPUT] {create,edit,constants} file\n\nCompile or edit data for the NanoFASE model.\n\npositional arguments:\n  {create,edit,constants}\n                        do you wish to create from scratch, edit the data or\n                        create a constants file?\n  file                  path to the config file (create/edit tasks) or\n                        constants file (constants task)\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --output OUTPUT, -o OUTPUT\n                        where to create the new constants file (for constants\n                        task)\n```\n\n### Creating a new dataset\n\nSpecifying the "create" option compiles a new NetCDF dataset and Fortran namelist constant file:\n\n```shell script\n$ python nanofase_data.py create /path/to/config.create.yaml\n```\n\nAn annotated example config file is given: [`config.create.example.yaml`](config.create.example.yaml). The file is quite self-explanatory, but a few further explanations are provided in [this document](docs/config.md).\n\nThe two files will be output to the paths specified in the config file.\n\n### Editing an existing dataset\n\nTo edit an existing NetCDF dataset, specify the "edit" option:\n\n```shell script\n$ python nanofase_data.py edit /path/to/config.edit.yaml\n```\n\nAn annotated example config file is given: [`config.edit.example.yaml`](config.edit.example.yaml). This is similar (but not identical) in format to the creation config file, except only those variables you with to edit should be specified (all other variables are left as-is).\n\nCertain variables can\'t be edited: `flow_dir`, `is_estuary`. Create a new dataset instead if you wish to change these variables.\n\nThe Fortran namelist file cannot be edited using this method and you should instead edit the file directly.\n\n### Only creating a new constants file\n\nTo simply convert a constants YAML file to a Fortran namelist file, you can use the `constants` option:\n\n```shell script\n$ python nanofase_data.py constants /path/to/constants.yaml -o /path/to/constants.nml\n```\n\nNo config file is required. The location of the newly created constants file is given by the `-o` or `--output` argument.\n\n### Tips\n- For the moment, all rasters must be the same CRS as the `flow_dir` raster, and this must be a projected raster. We recommend ESPG:27700 (British National Grid). In addition, all rasters except for `land_use` must be the same resolution as `flow_dir`. They can cover a large geographical region and the module will automatically clip them to the correct size.\n- Support for different file types is a bit sporadic at the moment. I suggest sticking the raster files for spatial variables, raster or CSV files for spatiotemporal variables (with 1 file per timestep for raster files) and shapefiles for point sources. You will trigger errors if you use an unsupported file.\n- Example input data files are given in `data.example/thames_tio2_2015/`. Running the model using the example config files uses these data. ',
    'author': 'Sam Harrison',
    'author_email': 'samharrison.xg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
