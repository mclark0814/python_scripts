#!/usr/bin/env python3.7
import boto3

#Create a AWS s3 bucket

s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket="mybucketmdc05182021b") #New bucket's name


