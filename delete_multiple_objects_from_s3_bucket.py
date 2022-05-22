import os #Provides functions for interacting with the operating system
import glob #The glob module is used to retrieve files/pathnames matching a specified pattern
import boto3

s3_client=boto3.client("s3")

#Find all the objects in the bucket
objects=s3_client.list_objects(Bucket="mybucketmdc05212021")["Contents"]

len(objects) # provides the number of objects in the bucket before deleting them

#Iteration
for object in objects: #For loop to delete the objects in the bucket
    s3_client.delete_object(Bucket='mybucketmdc05212021',
      Key=object["Key"])
    