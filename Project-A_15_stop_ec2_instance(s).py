import boto3
ec2_client=boto3.client('ec2') #Connecting to AWS ec2

#Process to stop the 3x ec2 instances running
response=ec2_client.stop_instances(
    InstanceIds=[
        'i-039b1017edbf312da','i-0b24b9c8e760f1f51','i-0d49d4623d6f9ed49'
        ],
        DryRun=False  #DryRun verifies if you have the necessary permission(s) to execute an action
)
print(response)


#Notes from DryRun (test) prior to submitting project results

#Traceback (most recent call last):
#  File "/home/ec2-user/environment/python_scripts/stop_ec2_a_single_instance.py", line 9, in <module>
#    DryRun=True,
#  File "/home/ec2-user/.local/lib/python3.7/site-packages/botocore/client.py", line 508, in _api_call
#    return self._make_api_call(operation_name, kwargs)
#  File "/home/ec2-user/.local/lib/python3.7/site-packages/botocore/client.py", line 911, in _make_api_call
#    raise error_class(parsed_response, operation_name)
#botocore.exceptions.ClientError: An error occurred (DryRunOperation) when calling the StopInstances operation: Request would have succeeded, but DryRun flag is set.


#Result of executing this python script to stop 3x instances
#{'StoppingInstances': [{'CurrentState': {'Code': 64, 'Name': 'stopping'}, 'InstanceId': 'i-039b1017edbf312da', 'PreviousState': {'Code': 16, 'Name': 'running'}}, {'CurrentState': {'Code': 64, 'Name': 'stopping'}, 
#'InstanceId': 'i-0d49d4623d6f9ed49', 'PreviousState': {'Code': 16, 'Name': 'running'}}, {'CurrentState': {'Code': 64, 'Name': 'stopping'}, 
#'InstanceId': 'i-0b24b9c8e760f1f51', 'PreviousState': {'Code': 16, 'Name': 'running'}}], 'ResponseMetadata': {'RequestId': '47a2807c-fed2-4c28-a2f8-25d31f09a7e8', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '47a2807c-fed2-4c28-a2f8-25d31f09a7e8', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '1257', 'date': 'Tue, 24 May 2022 03:33:24 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}




