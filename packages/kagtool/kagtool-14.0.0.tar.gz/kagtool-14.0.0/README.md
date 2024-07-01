First, go create your api key by clicking on [your profile](https://www.kaggle.com/settings)

1. API > Create Token
2. Download the file
3. Replace username and key by your own

```python
from kagtool.datasets.kaggle_downloader import KaggleDownloader

dataset_name = 'titanic'

path = KaggleDownloader.build(dataset_name,
                              'YOUR_USERNAME',
                              'YOUR_KEY').load_or_fetch_kaggle_dataset()

path.ls()
```
