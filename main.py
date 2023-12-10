import boto3
from botocore.exceptions import NoCredentialsError
import os
import sys
from PIL import Image
from dotenv import load_dotenv

def is_valid_image(file_path):
    try:
        with Image.open(file_path) as _:
            return True
    except Exception as e:
        print(f"Error opening image: {e}")
        return False

def main(image_path):
    s3 = boto3.client('s3')
    bucket = os.getenv('S3_BUCKET')

    try:
        s3.upload_file(image_path, bucket, image_path)
        print(f"File '{image_path}' uploaded to '{bucket}/{image_path}' successfully.")
    except NoCredentialsError:
        print("Credentials not available.")

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

    main(image_path)
