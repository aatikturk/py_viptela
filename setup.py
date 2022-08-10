import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent


VERSION = '0.2.3'
PACKAGE_NAME = 'py_viptela'
AUTHOR = 'Adem Atikturk'
AUTHOR_EMAIL = 'aatikturk@gmail.com'
URL = 'https://github.com/aatikturk/py_viptela'
LICENSE = 'GNU General Public License v2.0'
DESCRIPTION = 'A Python wrapper around Cisco vManage API'


LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

# Dependencies for the package
INSTALL_REQUIRES = [
      'requests'
]

# Python version requirement
PYTHON_REQUIRES = '>=3'

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      python_requires=PYTHON_REQUIRES,
      py_modules = ['baseclient', 'reqs'],
      packages=find_packages()
      )
