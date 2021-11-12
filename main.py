# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import boto3


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    lambda_client = boto3.client("lambda", region_name='us-west-2')
    response = lambda_client.invoke(
        FunctionName="test-func",
        InvocationType='Event',
        Payload=json.dumps({'hello': 'airflow'})
    )
    print('Hi')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
