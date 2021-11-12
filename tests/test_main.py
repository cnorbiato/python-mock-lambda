import json

import boto3
from moto import mock_lambda, mock_iam
from conftest import get_test_zip_file
import main


@mock_lambda
@mock_iam
def test_lambda_behaviour():
    lambda_client = boto3.client("lambda", region_name='us-west-2')
    iam_client = boto3.client("iam", region_name='us-west-2')

    iam_client.create_role(
        RoleName='test',
        AssumeRolePolicyDocument=json.dumps({
            "Version": "2012-10-17",
            "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}],
        }),
        Description='testrole',
    )

    lambda_client.create_function(
        FunctionName='test-func',
        Runtime='python3.8',
        Role='arn:aws:iam::123456789012:role/test',
        Handler='lambda_function.lambda_handler',
        Code={
            'ZipFile': get_test_zip_file(),
        },
        Description='test lambda function',
        Timeout=3,
        MemorySize=128,
        Publish=True
    )

    main.print_hi("caio")
