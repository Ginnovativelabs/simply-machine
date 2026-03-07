import os

def before_all(context):
    context.project_root = os.getcwd()

def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")

def before_scenario(context, scenario):
    context.analyser = None