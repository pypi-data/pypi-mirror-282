import warnings
import os
from pathlib import Path
import json

class KaggleDownloader:
    def __init__(self, dataset, creds_str, is_kaggle_env=os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')):
        warnings.warn(
            "The `__init__` method is deprecated and will be removed in a future version. "
            "Please use the `from_kaggle_env()` method instead.",
            DeprecationWarning,
            stacklevel=2)
        self.dataset = dataset
        self.creds = json.loads(creds_str)
        os.environ['KAGGLE_USERNAME'] = creds_str['username']
        os.environ['KAGGLE_KEY'] = creds_str['key']
        self.iskaggle_env = is_kaggle_env
    
    @classmethod
    def build(cls, dataset, username, key, is_kaggle_env=os.environ.get('KAGGLE_KERNEL_RUN_TYPE', '')):
        return cls(dataset, f'{"username":{username}, "key": {key}}', is_kaggle_env)

    def load_or_fetch_kaggle_dataset(self):
        if self.iskaggle_env:
            path = '/kaggle/input/' + str(self.dataset)
        else:
            path = self.dataset
            import zipfile,kaggle
            kaggle.api.competition_download_cli(path)
            zipfile.ZipFile(f'{path}.zip').extractall(path)
        return Path(path)
