import requests
import os
from tqdm import tqdm


def download(url: str, save_dir: str, file_name: str):
    response = requests.get(url)
    os.makedirs(f'{save_dir}', exist_ok=True)
    if response.status_code == 200:
        with open(os.path.join(f'{save_dir}', f"{file_name}"), 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download image for {file_name}. Status code: {response.status_code}")


def to_webp(name: str) -> str:
    return f'{name}.webp'


def get_filename(name: str, extension: str) -> str:
    return f'{name}.{extension}'


def download_all(url: list, save_dir: str, file_name: list, extension: str = None, timeit: bool = False) -> None:
    if timeit:
        from performer_helper import TimeIt
        with TimeIt():
            download_all(url=url, save_dir=save_dir, file_name=file_name, extension=extension, timeit=False)
    else:
        os.makedirs(f'{save_dir}', exist_ok=True)
        if len(url) != len(file_name):
            print(f"The length of url and file_name should be the same.")
        for url, name in tqdm(zip(url, file_name), total=min(len(url), len(file_name))):
            response = requests.get(url)
            if response.status_code == 200:
                if extension is not None:
                    file_name = get_filename(name, extension)
                if os.path.isfile(os.path.join(f'{save_dir}', f"{file_name}")):
                    print(f"{file_name} already exists. Skipping...")
                    continue
                with open(os.path.join(f'{save_dir}', f"{file_name}"), 'wb') as f:
                    f.write(response.content)
            else:
                print(f"Failed to download image for {file_name}. Status code: {response.status_code}")
        print(f"All images have been downloaded to {save_dir}")
