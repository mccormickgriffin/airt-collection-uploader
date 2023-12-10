import boto3
import os
import sys
from dotenv import load_dotenv

def main():
    aws_profile = os.getenv('AWS_PROFILE')
    session = boto3.Session(profile_name=aws_profile)
    s3 = session.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Verify image path argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.isfile(image_path):
        print("provided image path is not a file")
        sys.exit(1)
    
    main()
    