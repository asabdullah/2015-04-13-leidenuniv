# To compile:
#      python setup.py build_ext --inplace

from distutils.core import setup, Extension
from Cython.Distutils import build_ext

setup (name = "Exponential",
       version = "0.1",

       ext_modules = [Extension('exp_cython', ['exp_cython.pyx'])],

       cmdclass = {'build_ext': build_ext}
       )
