from setuptools import setup

with open('__version__') as f:
    _version = f.readline().strip()

setup(name='simplePatchManager',
      version=_version,
      description='Simple Patch Manager',
      url='https://bitbucket.org/rmonico/simplePatchManager',
      author='Rafael Monico',
      author_email='rmonico1@gmail.com',
      license='GPL3',
      include_package_data=True,
      packages=['simplePatchManager'],
      entry_points={
          'console_scripts': ['spm=simplePatchManager.__main__:main'],
      },
      zip_safe=False,
      install_requires=[''])
