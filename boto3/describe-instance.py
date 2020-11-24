import boto3
from pprint import pprint
client = boto3.client('ec2')
response = client.describe_instances(
    Filters=[],
    InstanceIds=[
        'i-yteyshhwusj1276492',
    ],
    DryRun=True
    
)

pprint(response)