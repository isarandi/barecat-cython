# Barecat-Cython

A partial Cython/C implementation of the [Barecat storage file format](https://github.com/isarandi/barecat).
 
Install with:

```bash
sudo apt install libsqlite3-dev  # or equivalent with other package managers
pip install barecat-cython
```

## Usage

The classes `BarecatCython` and `BarecatMmapCython` are similar to `barecat.Barecat` but do not support writing and advanced functions such as listing directories and globbing, etc. Only retrieving file data based on a given key string (inner filepath) is supported.

The difference between the two classes in `barecat_cython` is that `BarecatCython` uses file handles and seek/read to access shard files, while `BarecatMmapCython` uses memory mapping. Depending on computer and filesystem properties, one or the other may be faster, though the difference is not large in my experience.

```python
from barecat_cython import BarecatCython, BarecatMmapCython

with BarecatCython('example.barecat') as bc:
    ...

with BarecatMmapCython('example.barecat') as bc:
    ...
```

