import os
from box.exceptions import BoxValueError 
import yaml
from CNNClassifier import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import json
import joblib


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def save_json(path: Path, data: dict) :
    """saves json file

    Args:
        path (Path): path of the file
        data (dict): data to be saved

    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"json file: {path} saved successfully")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """loads json file

    Args:
        path (Path): path of the file
    
    Returns:
        ConfigBox: ConfigBox type data 

    """
    with open(path, "r") as json_file:
        contents = json.load(json_file)
    logger.info(f"json file: {path} loaded successfully")
    return ConfigBox(contents)  

@ensure_annotations
def save_bin(path: Path, data: Any) :
    """saves json file

    Args:
        path (Path): path of the file
        data (Any): data to be saved in bin file

    """
    joblib.save_bin(path, data)
    logger.info(f"bin file: {path} saved successfully")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """loads bin file

    Args:
        path (Path): path of the file
    
    Returns:
        Any: data loaded from bin file

    """
    contents = joblib.load_bin(path)
    logger.info(f"bin file: {path} loaded successfully")
    return contents  


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())