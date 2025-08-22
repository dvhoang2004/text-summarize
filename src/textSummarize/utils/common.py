import os
import yaml
from textSummarize.logging import logger
from box.exceptions import BoxValueError
from ensure import ensure_annotations   
from box import ConfigBox
from pathlib import Path
from typing import Any


# @ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox object.
    Args:
        (path_to_yaml: Path): Path to the YAML file.
    Raises:
        ValueError: If the file does not exist or is not a valid YAML file.
        e: empty file
    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except BoxValueError: 
        raise ValueError(f"File {path_to_yaml} is empty or not a valid YAML file.")
    except Exception as e:
        raise e
    
# @ensure_annotations
def create_directories(path_to_dirs: list, verbose=True) -> None:
    """
    Create directories if they do not exist.
    
    Args:
        path_to_dirs (Path): Path to the directory to be created.
        
    Raises:
        OSError: If there is an error creating the directory.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created successfully or already exists.")

# @ensure_annotations
def get_size(path : Path) -> str:
    """
    Get the size of a file or directory in KB.
    
    Args:
        path (Path): Path to the file or directory.
        
    Returns:
        str: Size in KB, formatted as a string.
    """
    if not path.exists():
        raise FileNotFoundError(f"The path {path} does not exist.")
    
    size = round(os.path.getsize(path) / 1024)
    return f"Size of {path} is {size} bytes."