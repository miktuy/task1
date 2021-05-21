from pathlib import Path
from typing import List
from dataclasses import dataclass
from xml.etree import ElementTree as ET

from src.logger import logger


@dataclass
class FileDescription:
    source_path: Path
    destination_path: Path


class ConfigHandler:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        if not self.config_path.exists():
            raise FileNotFoundError(f'Wrong config path: `{config_path}`')
        self.files: List[FileDescription] = []

    def read_config(self):
        tree = ET.parse(self.config_path)
        config = tree.getroot()
        for file in config:
            if (source_path := Path(file.attrib['source_path'], file.attrib['file_name'])).exists():
                self.files.append(
                    FileDescription(
                        source_path,
                        Path(file.attrib['destination_path'], file.attrib['file_name'])
                    )
                )
            else:
                logger.warning(f'File `{source_path}` not found!')
        return self.files
