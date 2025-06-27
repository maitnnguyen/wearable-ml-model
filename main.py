import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_data():
    # Set Kaggle config path to local .kaggle/ folder
    os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(os.getcwd(), '.kaggle')

    # Check if kaggle.json is there
    config_path = os.path.join(os.environ['KAGGLE_CONFIG_DIR'], 'kaggle.json')
    print("🔍 Using config:", config_path)
    print("✅ Exists:", os.path.exists(config_path))

    # Authenticate and download
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        'pratyushpuri/wearable-health-devices-performance-analysis',
        path='data/raw',
        unzip=True
    )
    print("✅ Dataset downloaded and extracted.")

if __name__ == "__main__":
    download_data()

