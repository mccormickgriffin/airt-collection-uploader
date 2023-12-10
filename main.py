import boto3
import os
import sys
from PIL import Image
from dotenv import load_dotenv

def is_valid_image(file_path):
    try:
        with Image.open(file_path) as img:
            return True
    except Exception as e:
        print(f"Error opening image: {e}")
        return False

def main():
    aws_profile = os.getenv('AWS_PROFILE')
    session = boto3.Session(profile_name=aws_profile)
    s3 = session.resource('s3')
    
    for bucket in s3.buckets.all():
        print(bucket.name)

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Verify the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    
    # Verify the provided path is a file
    if not os.path.isfile(image_path):
        print(f"Error: {image_path} is not a valid file path.")
        sys.exit(1)

    # Verify the file is a valid image
    if not is_valid_image(image_path):
        print(f"Error: {image_path} is not a valid image file.")
        sys.exit(1)

    main()
