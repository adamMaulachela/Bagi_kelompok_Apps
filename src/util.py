import yaml
import joblib
from datetime import datetime

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(base_dir, "../config/config.yaml")
# print(os.path.abspath(config_dir))


def time_stamp() -> datetime:
    # mengembalikan nilai tanggal dan waktu saat ini
    return datetime.now()


def load_config() -> dict:
    # memanggil yaml file
    try:
        with open(config_dir, "r") as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        raise RuntimeError("Parameter file not found in path")
    return config


def pickle_load(file_path: str):
    # ambil dan kembalikan pickle file
    return joblib.load(file_path)


def pickle_dump(data, file_path: str) -> None:
    # dump data ke dalam file
    joblib.dump(data, file_path)


params = load_config()
PRINT_DEBUG = params.get(
    "print_debug", False
)  # menggunakan default False jika kunci tidak ada


def print_debug(messages: str) -> None:
    # periksa apakah user akan menggunakan print atau tidak
    if PRINT_DEBUG:
        print(messages)
