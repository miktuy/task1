import argparse
import sys

from src.ConfigHandler import ConfigHandler
from src.CopyManager import CopyManager


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Copy files from config")
    parser.add_argument("-c", "--config", type=str, default='config.xml', help="Path to config (xml file)")
    params = parser.parse_args(sys.argv[1:])

    handler = ConfigHandler(params.config)
    files = handler.read_config()
    CopyManager(files).copy()
