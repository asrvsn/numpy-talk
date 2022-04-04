import sys
from glob import glob
from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext
import platform

cflags = ['-O3', '-Wall']
if sys.platform in ['linux', 'linux2']:
	cflags.append('-fopenmp') # Link OpenMP

ext = Pybind11Extension(
	'kuramoto._cpp',
	include_dirs=['./cpp'],
	sources=sorted(glob('cpp/*.c*')),
	define_macros = [('EXTENSION_NAME', '_cpp')],
	extra_compile_args = cflags,
)

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
		'line_profiler',
	],
	include_package_data=True,
	cmdclass={"build_ext": build_ext},
	ext_modules=[ext],
)
