from pathlib import Path
import sys
import pandas as pd


# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from preprocessing.mask import SensitiveDataMasker

if __name__ == "__main__":
    headhunter = pd.read_csv(Path("datasets/hr-grapevine-headhunter-database.csv"))
    masked_headhunter = SensitiveDataMasker().mask_dataframe(headhunter, {'Email': 'email', 'Phone': 'phone','Address Line 1': 'address'})
    print(masked_headhunter[['Email', 'Phone', 'Address Line 1']].head()) 
       