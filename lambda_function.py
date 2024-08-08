
import os
import io
import boto3
import json
import csv
from sklearn import preprocessing
import sklearn
import pandas as pd
import s3fs
import numpy as np

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')
bucket = 'sagemaker-eu-west-2-074439793145'
DATA_PREFIX = 'XGBOOST_POLLUTANT_238829'

# Your remaining code here
