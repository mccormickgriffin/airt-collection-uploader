import boto3
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    aws_profile = os.getenv('AWS_PROFILE')
    session = boto3.Session(profile_name=aws_profile)
    s3 = session.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
