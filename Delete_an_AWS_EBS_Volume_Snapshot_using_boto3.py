import boto3
ec2_boto3=boto3.client("ec2")

# Delete AWS EVS spanshot
ec2_boto3.describe_snapshots(SnapshotIds='snap-04573b7949c0deea7')
    
