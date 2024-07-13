import os
import yaml
from box.exceptions import BoxValueError
from TextSummarization.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any
from ensure import ensure_annotations 

## Reads YAML file and return contents
# @ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''Read YAML file and return contents
    Args:
        path_to_yaml (Path): Path to the YAML file.
    Raises:
        ValueError: If the YAML file is empty.
    Returns:
        ConfigBox: ConfigBox type
    '''
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file is empty.")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''Create list of directories.
    Args:
        path_to_directories (list): List of paths to directories.
        ignore_log(bool,optional): ignore if multiple dirs is to be created
    '''
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
                logger.info(f"Directory created at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
     '''Get size in KB.
     Args:
         path (Path): Path to the file.
     Returns:
         str: Size of the file in KB.
     '''
     size_in_kb = round(os.path.getsize(path) / 1024)
     return f"~{size_in_kb} KB"