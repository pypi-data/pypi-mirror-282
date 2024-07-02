import warnings
import os
from pathlib import Path
import json


class KaggleDownloader:
    def __init__(self, dataset, creds_str, is_kaggle_env=os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')):
        """
        Initialize the KaggleDownloader with the specified dataset and credentials.

        Args:
            dataset (str): The name of the dataset to download.
            creds_str (str): A JSON string containing the 'username' and 'key' for Kaggle API authentication.
            is_kaggle_env (str, optional): The environment variable indicating if the code is running in a Kaggle environment. Defaults to the value of 'KAGGLE_KERNEL_RUN_TYPE' environment variable, or an empty string if not set.
        """
        warnings.warn(
            "The `__init__` method is deprecated and will be removed in a future version. "
            "Please use the `from_kaggle_env()` method instead.",
            DeprecationWarning,
            stacklevel=2)
        self.dataset = dataset
        self.creds = json.loads(creds_str)
        self.iskaggle_env = is_kaggle_env
    
    @classmethod
    def build(cls, dataset, username=None, key=None, is_kaggle_env=os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')):
        """
        Create an instance of KaggleDownloader with the specified dataset and credentials.

        Args:
            dataset (str): The name of the dataset to download.
            username (str): The Kaggle username.
            key (str): The Kaggle API key.
            is_kaggle_env (str, optional): The environment variable indicating if the code is running in a Kaggle environment. Defaults to the value of 'KAGGLE_KERNEL_RUN_TYPE' environment variable, or an empty string if not set.

        Returns:
            KaggleDownloader: An instance of KaggleDownloader initialized with the provided dataset and credentials.
        """
        creds_str = json.dumps({"username": username, "key": key})
        return cls(dataset, creds_str, is_kaggle_env)

    def load_or_fetch_kaggle_dataset(self):
        if self.iskaggle_env:
            path = '/kaggle/input/' + str(self.dataset)
        else:
            
            path = self.dataset
            # it's important to do that before importing kaggle
            # as importing kaggle will check authentication
            if self.creds['username']:
                os.environ['KAGGLE_USERNAME'] = self.creds['username']
            if self.creds['key']:
                os.environ['KAGGLE_KEY'] = self.creds['key']

            import zipfile,kaggle
            kaggle.api.competition_download_cli(path)
            zipfile.ZipFile(f'{path}.zip').extractall(path)
        return Path(path)
