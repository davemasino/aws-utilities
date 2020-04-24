#!/usr/bin/env python

import boto3

session = boto3.Session(profile_name='mfa')
client = session.client('ec2')

response = client.describe_snapshots(
    # Filters=[
    #     {
    #         'Name': 'string',
    #         'Values': [
    #             'string',
    #         ]
    #     },
    # ],
)

snapshots = response['Snapshots']

if(snapshots):
    print("!!! WARNING !!!\n"
          "You are about to delete {} snapshots".format(len(snapshots)))

for snap in snapshots:
    pass
    # print(snap['SnapshotId'])
