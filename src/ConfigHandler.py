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
            source_path = file.attrib.get('source_path')
            destination_path = file.attrib.get('destination_path')
            file_name = file.attrib.get('file_name')
            if not all((source_path, destination_path, file_name)):
                raise KeyError(f'Not expected attributes for tag `{file.tag}`: {", ".join(file.attrib.keys())}!')

            if (source := Path(source_path, file_name)).exists():
                self.files.append(
                    FileDescription(
                        source,
                        Path(destination_path, file_name)
                    )
                )
            else:
                logger.warning(f'File `{source}` not found!')
        return self.files
