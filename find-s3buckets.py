#!/usr/bin/env python3.7
import boto3

#Generate a list of S3 buckets and printout the names of each bucket

s3_client = boto3.client('s3') 

bucket_list = s3_client.list_buckets() #List all of the existing buckets for the AWS account and assign them to the string

print(len(bucket_list)) # Display how many buckets are in the account

print('\nPrint a list of the existing buckets:\n')

for bucket in bucket_list['Buckets']: # Output the bucket names
    print(f' {bucket["Name"]}')
    