import boto3
from pprint import pprint
ec2 = boto3.client('ec2')
response = ec2.create_subnet(
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'subnet1'
                },
            ]
        },
    ],
    AvailabilityZone='ap-southeast-2a',
    
    CidrBlock='10.10.0.0/28',
    
    
    VpcId='vpc-01950d921db113d39',
    DryRun=True
)

pprint(reponse)