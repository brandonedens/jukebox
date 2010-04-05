from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='jukebox',
      version=version,
      description="Jukebox software.",
      long_description="""\
Jukebox web and client software.""",
      classifiers=[],
      keywords='jukebox audio',
      author='Brandon Edens',
      author_email='brandon@as220.org',
      url='http://as220.org/git/gitweb/',
      license='GPL-3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
      }
)
