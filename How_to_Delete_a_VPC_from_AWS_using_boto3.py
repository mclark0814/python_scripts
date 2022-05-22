import boto3
client=boto3.client("ec2") #identifying the aws service being used with the boto3 client

# How to delete a vpc form an AWS account

client.delete_vpc(VpcId="vpc-0d2625bb85be3119a") # Delete the specified VPC and it cannot have any dependencies prior to deleting it.



