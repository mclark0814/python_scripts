import boto3
ec2_client=boto3.client("ec2")

#ec2_client.create_snapshot(Description='snapshot from basevolume using python', VolumeId='vol-0e11304d6c3544ed3')

ec2_client.create_volume(AvailabilityZone='us-east-1e',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-0f4a791ad466d1634',
      VolumeType='gp2')

