from setuptools import setup, find_packages

setup(name='wswfg_archiver',
      version='1.0',
      author='amas0',
      description='Python utility to archive the web comic "Will save world for gold"',
      packages=find_packages(),
      install_requires=[
            'aiohttp',
            'bs4'
      ],
      entry_points={
            'console_scripts': [
                  'wswfg = wswfg_archiver.main:main'
            ]
      }
      )
