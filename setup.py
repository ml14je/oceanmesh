import versioneer
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

# https://github.com/pybind/python_example/
is_called = [
    "_HamiltonJacobi",
    "_delaunay_class",
    "_fast_geometry",
]

files = [
    "oceanmesh/cpp/HamiltonJacobi.cpp",
    "oceanmesh/cpp/delaunay_class.cpp",
    "oceanmesh/cpp/fast_geometry.cpp",
]

# no CGAL libraries necessary from CGAL 5.0 onwards
ext_modules = [
    Pybind11Extension(loc, [fi], libraries=["gmp", "mpfr"])
    for fi, loc in zip(files, is_called)
]

cmdclass = versioneer.get_cmdclass()
cmdclass.update({"build_ext": build_ext})

if __name__ == "__main__":
    setup(
        cmdclass=cmdclass,
        version=versioneer.get_version(),
        ext_modules=ext_modules,
        zip_safe=False,
    )
