# MyKMeansProject

This package provides Python bindings to run KMeans and GeoKMeans algorithms using a C++ backend.

## Installation

You can install this package using pip:

```bash
pip install mykmeansproject
```


Usage

```python
from mykmeansproject.kmeans import run_lloyd_kmeans, run_geokmeans

result = run_lloyd_kmeans(
    100,
    0.0001,
    12,
    17,
    [
        "./Breastcancer.csv",
        "./CreditRisk.csv",
        "./census.csv",
        "./birch.csv"
    ]
)

run_geokmeans(
        100,
        0.0001,
        12,
        17,
        [
            "./Breastcancer.csv",
            "./CreditRisk.csv",
            "./census.csv",
            "./birch.csv"
        ]

print(result)
```