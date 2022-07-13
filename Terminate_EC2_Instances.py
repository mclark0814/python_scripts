import boto3
ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"]

li=[]
for instances in data: #(List comprehensive collecting of all instances on the account)
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)

#Terminate EC2 instances
        
ec2_client.terminate_instances(InstanceIds=li) #Terminate instances that are not protected from accidential termination
