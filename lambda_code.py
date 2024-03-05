import json
import boto3
import yaml

def lambda_handler(event, context):
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
    
    users = dict['Users']
    groups = dict['AssignmentGroups']
    
    #access iam client
    iam = boto3.client('iam')
    
    #creating user from Users key in yaml file saved in dict
    print('\n------')
    for user in users:
        created_user = iam.create_user(
            UserName = user
        )
    print('users created...')
    
    #Listing iam users after creation of new users
    response = iam.list_users()
    ul = []
    
    #assigning groups from AssignmentGroups key's value from yaml config files
    for key, val in groups.items():
        for u in val:
            user_to_group = iam.add_user_to_group(
                GroupName=key,
                UserName=u
            )
    print('user groups attached...')
    
    for user in response['Users']:
        ul.append(user['UserName'])
        
    return {
        'statusCode': 200,
        'body': ul
    }
