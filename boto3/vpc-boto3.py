import boto3 
ec2 = boto3.client('ec2')
response = ec2.create_vpc(
    CidrBlock='10.10.0.0/18',
    DryRun=True,
    InstanceTenancy='default',
    TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'VPC_boto3'
                },
            ]
        },
    ]
)