# Building-data-pipelines-in-AWS
In this repo lets take a dive into building short data pipe lines in AWS by using python &amp; terraform!

Problem statment:
To create an automated data pipe-line using AWS servies(S3,Lambda,CloudWatch), Where we need to create an automated data flow(trigger) when ever a file is uploaded in the S3 bucket and process the raw data for further insights and store them(results) to another S3 bucket.

Approach & Workflow Explanation

1. CSV File Upload to S3 Bucket:
The workflow begins with a CSV file being uploaded to an Amazon S3 bucket. This bucket acts as the data storage layer where raw files are stored. The uploaded file is the input for further processing.

2. S3 Event Trigger:
The upload of the file to the S3 bucket generates an event. This event automatically triggers an AWS Lambda function. This is set up using an S3 event trigger, which notifies the Lambda function whenever a file is uploaded to the bucket.

3. IAM Role for Access Control:
An IAM Role is used to ensure secure and authorized access between the S3 bucket and the Lambda function. This role provides the necessary permissions for the Lambda function to read the file from the S3 bucket.

4. Lambda Function for Data Processing:
The AWS Lambda function is the heart of this workflow. It performs the following actions:

Reads the CSV file from the S3 bucket.
Processes the file's data (e.g., aggregating salary data for "India" and "US").
Creates an output or result file containing the aggregated data.
5. Output Logs to CloudWatch:
The Lambda function logs important details such as the file processing status, errors (if any), and debug information to Amazon CloudWatch Logs. This makes it easier to monitor and troubleshoot the workflow.

6.Store Processed File in Another S3 Bucket:
After processing the data, the Lambda function writes the output file (containing the aggregated salary data) to a different Amazon S3 bucket. This separation ensures a clean workflow where raw and processed data are stored in distinct locations, improving data organization and management.

Key Benefits of This Workflow:

Automation: The entire process is automated, from file upload to data processing and storage.
Scalability: Leveraging S3 and Lambda ensures the system can handle large volumes of data efficiently.
Security: IAM roles enforce controlled access, maintaining the security of the data.
Monitoring: CloudWatch logs provide visibility into the workflow for easy debugging and performance tracking.
