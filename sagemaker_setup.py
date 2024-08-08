
import sagemaker
from sagemaker import get_execution_role
from sagemaker.amazon.amazon_estimator import get_image_uri
import boto3

from sklearn.model_selection import train_test_split

s3 = boto3.resource('s3')

sagemaker_session = sagemaker.Session()
role = get_execution_role()

BUCKET = sagemaker_session.default_bucket()

# This references the AWS managed XGBoost container
XGBOOST_IMAGE = get_image_uri(boto3.Session().region_name, 'xgboost', repo_version='1.0-1')

DATA_PREFIX = 'XGBOOST_BOSTON_HOUSING'
MULTI_MODEL_ARTIFACTS = 'multi_model_artifacts'

TRAIN_INSTANCE_TYPE = 'ml.m4.xlarge'
ENDPOINT_INSTANCE_TYPE = 'ml.m4.xlarge'

ENDPOINT_NAME = 'mme-xgboost-housing'
MODEL_NAME = ENDPOINT_NAME
