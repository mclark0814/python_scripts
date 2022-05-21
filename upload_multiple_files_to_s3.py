#!/usr/bin/env python3.7
import boto3

#How to upload multiple files into AWS s3 bucket
import os
import glob

cwd=os.getcwd()  # Assign the variable the location of the current working directory
cwd=cwd+"/python_scripts/upload/" # Assigns the path of the folder with the files

files=glob.glob(cwd+"*.png") #Used to return all file paths that match a specific pattern

for file in files: # For loop to read the names of the files and then upload them o the bucket
    s3_client=boto3.client("s3")
    s3_client.upload_file(
    Filename=file,
    Bucket="mybucketmdc05212021",
    Key=file.split("/")[-1])
    print(files)