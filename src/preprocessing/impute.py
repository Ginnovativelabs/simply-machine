import numpy as np
import pandas as pd
from typing import Union, List
from sklearn.impute import KNNImputer

class Imputer:
    """A comprehensive class for handling 
    missing data imputation in machine learning."""
    
    def __init__(self, strategy: str = 'mean'):
        """
        Initialize the Imputer.
        
        Args:
            strategy: Imputation strategy ('mean', 'median', 'mode', 'forward_fill', 'backward_fill')
        """
        self.strategy = strategy
        self.fill_values = {}
    
    def fit(self, data: pd.DataFrame) -> 'Imputer':
        """Fit the imputer to the data."""
        if self.strategy == 'mean':
            self.fill_values = data.mean(numeric_only=True).to_dict()
        elif self.strategy == 'median':
            self.fill_values = data.median(numeric_only=True).to_dict()
        elif self.strategy == 'mode':
            self.fill_values = data.mode(numeric_only=True).iloc[0].to_dict()
        return self
    
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Apply imputation to the data."""
        data = data.copy()
        
        if self.strategy in ['mean', 'median', 'mode']:
            for col, val in self.fill_values.items():
                data[col].fillna(val, inplace=True)
        elif self.strategy == 'forward_fill':
            data.fillna(method='ffill', inplace=True)
        elif self.strategy == 'backward_fill':
            data.fillna(method='bfill', inplace=True)
        
        return data
    
    def fit_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Fit and transform in one step."""
        return self.fit(data).transform(data)
    
    def impute_constant(self, data: pd.DataFrame, value: Union[int, float]) -> pd.DataFrame:
        """Fill missing values with a constant."""
        return data.fillna(value)
    
    def impute_interpolation(self, data: pd.DataFrame) -> pd.DataFrame:
        """Use interpolation for missing values."""
        return data.interpolate(method='linear')
    
    def impute_knn(self, data: pd.DataFrame, n_neighbors: int = 5) -> pd.DataFrame:
        """Fill missing values using KNN (requires sklearn)."""
        imputer = KNNImputer(n_neighbors=n_neighbors)
        return pd.DataFrame(imputer.fit_transform(data), columns=data.columns)