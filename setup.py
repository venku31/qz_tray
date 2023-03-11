from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in qz_tray/__init__.py
from qz_tray import __version__ as version

setup(
	name="qz_tray",
	version=version,
	description="Print using qz tray",
	author="Kishan Panchal",
	author_email="k.d.panchalofc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
