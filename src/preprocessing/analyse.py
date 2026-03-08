import numpy as np
import pandas as pd
import hashlib

class Analyser:
    """A class for analyzing data in a pandas DataFrame."""

    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def derive_type(self,column: str) -> str:
        """Derive the data type of a column based on its content."""
        if column not in self.data.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        series = self.data[column]
        data_type = ""
        for val in series.dropna():
            if isinstance(val, str):
                if self.__check_categorical(series):
                    data_type = 'categorical'
                else:
                    data_type = 'text'
                break
            elif isinstance(val, float):
                if self.__check_integer(series):
                    data_type = 'integer'
                else:
                    data_type = 'numeric'
                break
            elif isinstance(val, bool):
                data_type = 'boolean'
                break
            else:
                data_type = 'unknown'
                break
        return data_type if data_type else 'unknown'


    def __check_categorical(self, column: pd.Series) -> bool:
        unique_count = column.nunique()
        if unique_count <= 10:
            return True
        return False

    def __check_integer(self, column: pd.Series) -> bool:
        if (column.dropna().apply(lambda x: x == round(x)).all()):
            return True
        return False

    def get_columns_type_dict(self) -> dict:
        """Convert object columns to categorical types and return the new data types."""
        return {column: {'data-type': self.derive_type(column)} for column in self.data.columns}

    def nan_count(self, column: str) -> int:
        """Count the number of NaN values in a specified column."""
        if column in self.data.columns:
            return self.data[column].isna().sum()
        else:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
   
    def not_nan_count(self, column: str) -> int:
        """Count the number of non-NaN values in a specified column."""
        if column in self.data.columns:
            return self.data[column].notna().sum()
        else:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    def get_nan_count_dict(self) -> dict:
        """Return a dictionary with the count of NaN values for each column."""
        return {column: {'nan-count': self.nan_count(column).item()} for column in self.data.columns}
    
    def get_not_nan_count_dict(self) -> dict:
        """Return a dictionary with the count of non-NaN values for each column."""
        return {column: {'not-nan-count': self.not_nan_count(column).item()} for column in self.data.columns}

    def mask_hash(self, column: str) -> pd.Series:
        """Mask column values with cryptographic hashes if the value is a string."""
        if column in self.data.columns: 
            return self.data[column].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
        else:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    def checksum(self, column: str) -> int:
        """Calculate the checksum of a specified column."""
        return sum(hash(x) for x in self.data[column].dropna()) % (2**32)
