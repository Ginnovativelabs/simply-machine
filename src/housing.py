from pathlib import Path
import sys
import pandas as pd
import tarfile
import urllib.request
import urllib.error
import ssl
import certifi

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from preprocessing.analyse import Analyser

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True) 
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        # Create SSL context with certifi certificates
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        # Download file using urllib with SSL context
        with urllib.request.urlopen(url, context=ssl_context) as response:
            with open(tarball_path, 'wb') as out_file:
                out_file.write(response.read())
    with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

if __name__ == "__main__":
    housing = load_housing_data()
    analyser=Analyser(housing)
    print(analyser.get_columns_type_dict())
    print(analyser.get_nan_count_dict())  
    print(analyser.get_not_nan_count_dict())
