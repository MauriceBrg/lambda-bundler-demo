import pandas as pd

def lambda_handler(event, context):
    print(f"pandas version: {pd.__version__}")