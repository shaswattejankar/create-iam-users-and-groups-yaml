# create-iam-users-and-groups-yaml

python program to read the yaml config file for the purpose of creating iam users and attaching user groups to it

read_s3_yaml.py -> reads the yaml file from the s3 bucket with the provided Bucket and Key names and creates users and attaches user groups

To create the zip file for the layer run the following commands:

mkdir layer/python/lib/python3.11/site-packages/
cd layer
pip install --no-user -t .\python\lib\python3.11\site-packages\ pyyaml

then use: zip -r my_layer.zip python 
to zip the python folder or right-click and zip it