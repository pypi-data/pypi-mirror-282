# ExampleNewProject

This is a Python wrapper for a C++ project.

## Installation
```
pip install examplenewproject

```

____________________

```


from examplenewproject.wrapper import process_files

num_iterations = 100
threshold = 0.0001
num_clusters = 12
seed = 17
file_list = [
    "../../Sample_Data/Breastcancer.csv",
    "../../Sample_Data/CreditRisk.csv",
    "../../Sample_Data/census.csv",
    "../../Sample_Data/birch.csv"
]

results = process_files(num_iterations, threshold, num_clusters, seed, file_list)

for result in results:
    print(result)

```