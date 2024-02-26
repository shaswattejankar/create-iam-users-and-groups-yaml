import boto3
from botocore.exceptions import ClientError
import yaml

#access the iam service
iam = boto3.client('iam')

#read the config file:-
with open('02_data_config.yaml') as f:
    dict = yaml.safe_load(f)

#read the keys and values
print('\n------')
users = dict['Users']
print('users : ', users)
groups = dict['AssignmentGroups']
print('Groups : ', groups)

#creating user from Users key in yaml file
print('\n------')
for user in users:
    created_user = iam.create_user(
        UserName = user
    )
print('users created...')

#assigning groups from AssignmentGroups from yaml config files
for key, val in groups.items():
    for u in val:
        user_to_group = iam.add_user_to_group(
            GroupName=key,
            UserName=u
        )
print('user groups attached...')
