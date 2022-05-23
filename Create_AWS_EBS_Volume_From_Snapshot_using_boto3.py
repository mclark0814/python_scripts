import boto3
ec2_client=boto3.client("ec2")

#ec2_client.create_snapshot(Description='snapshot from basevolume using python', VolumeId='vol-0e11304d6c3544ed3')

ec2_client.create_volume(AvailabilityZone='us-east-1e',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-09a3aa81d08d5d129',
      VolumeType='gp2')

