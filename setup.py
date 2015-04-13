from setuptools import setup

setup(name='smilesfinder',
      version='0.1',
      description='A python package to generate canonical SMILES from chemical names, SLN representations or both',
      url='https://github.com/dsmurrell/smilesfinder',
      author='Daniel Murrell',
      author_email='dsmurrell@gmail.com',
      license='MIT',
      packages=['smilesfinder'],
      entry_points = {
        'console_scripts': ['get-canonical-smiles=smilesfinder.command_line:main'],
        },
      zip_safe=False)