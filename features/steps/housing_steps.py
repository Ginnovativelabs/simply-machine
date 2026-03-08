from behave import given,when,then
from pandas.api import types as ptypes
import pandas as pd
import os

from preprocessing.analyse import Analyser

@given('the dataset "{path}" is loaded')
def load_dataset(context, path):
    csv_path = path
    # if relative path, make relative to project root (behave run location)
    if not os.path.isabs(csv_path):
        csv_path = os.path.join(context.project_root, csv_path)
    context.analyser = Analyser(pd.read_csv(csv_path))

@when(u'the Anaylser object is initiated with the dataset')
def initialize_analyser(context):
    if not hasattr(context, 'analyser'):
        raise AssertionError("Analyser not initialized. Use the Given step to load the CSV.")

@then('the column "{col}" should be "{expected_type}"')
def check_column_type(context, col, expected_type):
    if context.analyser is None:
        raise AssertionError("Analyser not initialized. Use the Given step to load the CSV.")
    series = context.analyser.derive_type(col)
    checker = expected_type.lower()
    if not checker==series:
        # helpful failure message with actual dtype
        raise AssertionError(f'Column "{col}" expected to be {expected_type}, actual dtype: {series}')

@then('the key "{key}" should have the value "{expected_value}"')
def check_column_type(context, key, expected_value):
    if context.analyser is None:
        raise AssertionError("Analyser not initialized. Use the Given step to load the CSV.")
    datatypes = context.analyser.get_columns_type_dict()
    if key not in datatypes:
        raise AssertionError(f'Column "{key}" not found in datatypes dictionary.')
    if datatypes[key]['data-type'] != expected_value:
        raise AssertionError(f'Column "{key}" expected to be {expected_value}, actual dtype: {datatypes[key]}')

@then(u'the column "{column}" should have zero NaN values')
def check_nan(context, column):
    if context.analyser is None:
        raise AssertionError("Analyser not initialized. Use the Given step to load the CSV.")
    nan_count = context.analyser.nan_count(column)
    if nan_count > 0:
        raise AssertionError(f'Column "{column}" has {nan_count["nan-count"]} NaN values.')

@then(u'the key "{column}" should have no NaN values')
def check_nan_dict(context, column):
    if context.analyser is None:
        raise AssertionError("Analyser not initialized. Use the Given step to load the CSV.")
    nan_counts = context.analyser.get_nan_count_dict()
    if column not in nan_counts:
        raise AssertionError(f'Column "{column}" not found in NaN count dictionary.')
    if nan_counts[column]['nan-count'] > 0:
        raise AssertionError(f'Column "{column}" has {nan_counts[column]["nan-count"]} NaN values.')

@then(u'the key "{column}" should have NaN values')
def check_nan_dict(context, column):
    if context.analyser is None:
        raise AssertionError("Analyser not initialized. Use the Given step to load the CSV.")
    nan_counts = context.analyser.get_nan_count_dict()
    if column not in nan_counts:
        raise AssertionError(f'Column "{column}" not found in NaN count dictionary.')
    if nan_counts[column]['nan-count'] == 0:
        raise AssertionError(f'Column "{column}" has {nan_counts[column]} NaN values.')