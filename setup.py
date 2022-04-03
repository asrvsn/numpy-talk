import sys

try:
	from skbuild import setup
except ImportError:
	print(
		"Please update pip, you need pip 10 or greater,\n"
		" or you need to install the PEP 518 requirements in pyproject.toml yourself",
		file=sys.stderr,
	)
	raise

from setuptools import find_packages

setup(
	name='kuramoto',
	version="0.0.1",
	author='Anand Srinivasan',
	author_email='asrinivasan@fas.harvard.edu',
	description='Kuramoto model using NumPy + PyBind11',
	url='https://github.com/asrvsn/numpy-talk',
	package_dir={'': 'src'},
	packages=find_packages(where="src"),
	python_requires='>=3.9',
	install_requires=[
		'numpy>=1.22.0',
		'matplotlib',
	],
	# TODO: set -O3 and inline flags
	cmake_install_dir="src/kuramoto",
	include_package_data=True,
)
