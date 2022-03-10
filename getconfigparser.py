from configparser import ConfigParser


def getconfigparser(config_path):
    parser = ConfigParser()
    parser.read(config_path)
    return parser