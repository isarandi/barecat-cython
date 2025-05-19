import numpy as np
from setuptools import Extension, setup

ext_modules = [
    Extension(
        'barecat_cython.barecat_cython',
        sources=['src/barecat_cython/barecat_cython.pyx', 'src/barecat_cython/barecat.c',
                 'src/barecat_cython/barecat_mmap.c', 'src/barecat_cython/crc32c.c'],
        extra_compile_args=['-O3', '-Wno-cpp', '-Wno-unused-function', '-std=c11'],
        include_dirs=[np.get_include()],
        define_macros=[("SQLITE_THREADSAFE", "2")],
        libraries=["sqlite3", "c"]
    )
]

setup(ext_modules=ext_modules)
