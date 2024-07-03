from decouple import Config, RepositoryEnv
import os


def get_config():
    package_root = os.path.dirname(os.path.abspath(__file__))
    env_file_path = os.path.join(package_root, '../.env')
    config = Config(RepositoryEnv(env_file_path))
    return config

