import pytz

def lambda_handler(event, context):
    print(f"pytz version: {pytz.__version__}")
