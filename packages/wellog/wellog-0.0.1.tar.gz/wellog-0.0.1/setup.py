import pathlib
from setuptools import find_packages, setup

with open('./README.md', 'r', encoding='utf-8') as fh:
  readme = fh.read()

setup(
  name='wellog',
  version='0.0.1',
  description='Registros',
  long_description=readme,
  long_description_content_type='text/markdown',
  author='Pedro Jesús Pérez Hernández',
  author_email='pedrojesus.perez@welldex.mx',
  url='https://gitwell.gwldx.com:2443/python_libraries/manager_logs',
  install_requires=['loguru'],
  license='MIT',
  packages=find_packages(),
  include_package_data=True
)