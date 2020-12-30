import logging
import boto3
from botocore.exceptions import ClientError

# Configure the Logger
logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def lambda_handler(event, context):
    return "It works!"
