import pandas as pd
import re
from typing import List, Dict

class SensitiveDataMasker:
    """Masks sensitive information in dataframes."""
    def __init__(self):
        self.patterns = {
            'phone': r'^\+?[0-9\s().\-]{7,30}$',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'address': r'\b\d+\s+[A-Za-z\s,.#-]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Drive|Dr|Lane|Ln|Court|Ct)\b',
        }
    
    def mask_phone(self, value: str) -> str:
        """Mask phone numbers."""
        if not isinstance(value, str):
            return value
        return re.sub(self.patterns['phone'], 'XXX-XXX-XXXX', value)
    
    def mask_email(self, value: str) -> str:
        """Mask email addresses."""
        if not isinstance(value, str):
            return value
        return re.sub(self.patterns['email'], 'xxx@xxx.com', value)
    
    def mask_address(self, value: str) -> str:
        """Mask addresses."""
        if not isinstance(value, str):
            return value
        return "Masked Address"
    
    def mask_organization(self, value: str) -> str:
        """Mask organization names."""
        if not isinstance(value, str):
            return value
        return '[ORGANIZATION]'
   
    def mask_dataframe(self, df: pd.DataFrame, 
                       sensitive_columns: Dict[str, str]) -> pd.DataFrame:
        """
        Mask sensitive columns in a dataframe.
        
        Args:
            df: Input dataframe
            sensitive_columns: Dict mapping column names to data types
                              (e.g., {'email': 'email', 'phone': 'phone'})
        
        Returns:
            Dataframe with masked sensitive information
        """
        df_masked = df.copy()
        
        for column, data_type in sensitive_columns.items():
            if column in df_masked.columns:
                if data_type == 'phone':
                    df_masked[column] = df_masked[column].apply(self.mask_phone)
                elif data_type == 'email':
                    df_masked[column] = df_masked[column].apply(self.mask_email)
                elif data_type == 'address':
                    df_masked[column] = df_masked[column].apply(self.mask_address)
                elif data_type == 'organization':
                    df_masked[column] = df_masked[column].apply(self.mask_organization)
        
        return df_masked