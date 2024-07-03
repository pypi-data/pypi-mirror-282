# Cheb3D library

## Installation (local)


### Create a virtual environment and source it
```bash
cd ..
python -m virtualenv venv
source venv/bin/activate
pip install cython
```


### Launch the build
```bash
python setup.py build_ext --inplace
```


### Test it
```bash
cp Cheb3D/PyNumSpec.cpython* Test/.
cd Test
python verif.py
```

#### Notes
A try to explain how the library works is given in [Test_explaination.md](Test_explaination.md)


### Intallation (pip)

```bash
pip install Cheb3D
```



# Packaging in PIP:


## on Macos
``` bash
pip install wheel
```

``` bash
python setup.py sdist bdist_wheel
```
This will create two packages in the directory `dist/`:
.A file .tar.gz (source distribution)
.A file .whl (built distribution)

### Chargiing on PyPI

``` bash
pip install twine
```

then

``` bash
twine upload dist/*

```

## on Linux
```bash
docker run --rm -v $(pwd):/io quay.io/pypa/manylinux1_x86_64 /io/build_multilinux.sh
twine upload dist/*
```

# Cleaning
You have to put a new value for version in setup.py and pyproject.py
and clean up the build:

``` bash
rm -rf dist build Cheb3D.egg-info
```
