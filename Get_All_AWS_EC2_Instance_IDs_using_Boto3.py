import boto3
ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances() #
data=x["Reservations"][0] # Entry from within a the EC2 dictionary
data_instance=data["Instances"]
for i in range (len(data_instance)):  #Print output showing the EC2 instance name(s)
    print(f"instance id is {data_instance[i]['InstanceId']}")
    
    