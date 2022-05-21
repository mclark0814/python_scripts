#!/usr/bin/env python3.7
import boto3

#How to upload single file into AWS s3 bucket

s3_client=boto3.client("s3")

s3_client.upload_file(
    Filename="TechSupport_Cookies.png",
    Bucket="mybucketmdc05212021",
    Key="TechSupport_Cookies.png")
