import argparse
import sys

from src.ConfigHandler import ConfigHandler
from src.CopyManager import CopyManager


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Copy files which are described in config")
    parser.add_argument("-c", "--config", type=str, default='config.xml', help="Path to config (xml file). Default is './config.xml'")
    params = parser.parse_args(sys.argv[1:])

    files = []

    try:
        handler = ConfigHandler(params.config)
        files = handler.read_config()
    except (FileNotFoundError, KeyError) as e:
        print(f'Error: {e}')
        exit(1)

    CopyManager(files).copy()
