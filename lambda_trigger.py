import csv
import json
import boto3

def lambda_handler(event, context):
    # Extract bucket and file key from the event
    event_params = event["Records"][0]
    source_bucket = event_params["s3"]["bucket"]["name"]
    key = event_params["s3"]["object"]["key"]
    
    # Define the destination bucket name (replace with your bucket name)
    destination_bucket = "your-destination-bucket-name"
    
    # Read the uploaded CSV file
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object(source_bucket, key)
    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()
    
    # Parse the CSV content
    lines = csv.reader(data)
    headers = next(lines)
    list_data = list(lines)
    
    # Calculate salary spend by country
    india = []
    us = []
    for row in list_data:
        if row[3] == 'India':
            india.append(int(row[2]))
        else:
            us.append(int(row[2]))
    
    # Create the output content
    print(f"Total India salary spend: {sum(india)}")
    print(f"Total US salary spend: {sum(us)}")
    file_content = f"Total salary spend - India: {sum(india)}, US: {sum(us)}"
    
    # Upload the output to the destination bucket
    s3 = boto3.client('s3')
    output_key = "aggregated-salary.csv"
    s3.put_object(Body=file_content, Bucket=destination_bucket, Key=output_key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Output successfully written to another S3 bucket!')
    }
