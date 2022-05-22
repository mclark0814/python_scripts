# How to add a description to a vpc
import boto3
client=boto3.client("ec2") #identifying the aws service being used with the boto3 client

# How to describe all vpcs that are available in your account

x=client.describe_vpcs() # Describes one or more of your VPCs

no_of_vpcs=x["Vpcs"] 

len(no_of_vpcs) # Returns the number of VPCs

for vpc in no_of_vpcs: #Loop for displaying the VPC IDs
    print(vpc["VpcId"])