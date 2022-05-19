#!/usr/bin/env python3.7
import boto3

s3_client=boto3.client('s3')
s3_client.list_buckets()["Buckets"][0]["Name"] #Starting at position 1, assigning the bucket's name to the string

creation_date=s3_client.list_buckets()["Buckets"][0]["CreationDate"] #Starting at position 1, assigning the bucket's creation date to the string

creation_date.strftime("%dd%mm%yy_% H:%M:%s")  #Formatting the creation date and time

for bucket in s3_client.list_buckets()["Buckets"]: #Iterating through the list and printing out the names and creation dates for each bucket
    print("\n")
    print(bucket["Name"])
    print(bucket["CreationDate"])
