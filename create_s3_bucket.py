import boto3

def create_bucket(bucket_name, region="ap-south-1"):
    s3 = boto3.client("s3", region_name=region)
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": region}
    )
    print("Bucket created:", bucket_name)

if __name__ == "__main__":
    create_bucket("harish-s3-bucket-demo-001")
