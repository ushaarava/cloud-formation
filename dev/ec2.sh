#!/bin/bash

/usr/local/bin/aws ec2 run-instances \
    --image-id $Image \
    --instance-type $Instancetype \
    --subnet-id $Subnets \
    --security-group-ids $SecurityGroup \
    --key-name $keypair \
    --region $region \
    --count 1 \
    --no-dry-run


