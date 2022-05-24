import boto3
ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-04573b7949c0deea7') # Delete AWS EVS spanshot