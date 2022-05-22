#!/usr/bin/env python3.7
import boto3

#How to delete single object in an AWS s3 bucket

s3_client=boto3.client("s3")
s3_client.delete_object(Bucket='mybucketmdc05212021', 
    Key='5-21-2022b.png')


