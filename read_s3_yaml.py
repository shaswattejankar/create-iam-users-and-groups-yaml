import boto3
import yaml

#Paste your bucket name
bucket_name = 'myyamlconfigfile'
#Paste your Object name
key_name = 'data_config.yaml'

#access s3 objects
s3 = boto3.client('s3')
resobj = s3.get_object(
    Bucket=bucket_name, 
    Key=key_name, 
)

#read the .yaml file and save it's contents in a variable of type dict
yaml_data = resobj['Body'].read().decode('utf-8')
dict = yaml.safe_load(yaml_data)

#CHECK if yaml file read correctly
#read the keys and values
print('\n------')
users = dict['Users']
print('users : ', users)
groups = dict['AssignmentGroups']
print('Groups : ', groups)

#access iam client
iam = boto3.client('iam')

#creating user from Users key in yaml file saved in dict
print('\n------')
for user in users:
    created_user = iam.create_user(
        UserName = user
    )
print('users created...')

#assigning groups from AssignmentGroups key's value from yaml config files
for key, val in groups.items():
    for u in val:
        user_to_group = iam.add_user_to_group(
            GroupName=key,
            UserName=u
        )
print('user groups attached...')