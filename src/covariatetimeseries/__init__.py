import os
from typing import Final, Any
from pandas import DataFrame, read_csv
from covariatetimeseries.data_collections import CSV_SEPERATOR #type:ignore
from .timeseries_loader import load_timeseries

# Collection Path
_COLLECTION_PATH: Final[str] = os.path.join(os.path.dirname(__file__), 'data_collections')
# Cache
LOADED_DATASETS: Final[dict[DataFrame]] = {}

def collection_file_map(name: str) -> str:
    file_name = name
    if name in ["meta", "info"]:
        file_name = "_collection_info"
    return file_name

def __getattr__(name):
    # Check if the requested dataset in cache
    if name in LOADED_DATASETS:
        return LOADED_DATASETS[name]
    
    # Read
    file_path = os.path.join(_COLLECTION_PATH, f"{collection_file_map(name)}.csv")
    if os.path.isfile(file_path):
        df = read_csv(file_path, sep = CSV_SEPERATOR)
        # Cache
        LOADED_DATASETS[name] = df 
        return df
    else:
        raise AttributeError(f"Dataset '{name}' not found in the data folder. Check covariatetimeseries.meta DataFrame for overview information")
