
# create-iam-users-and-groups-yaml

read_data_config.py -> python program to read the yaml config file for the purpose of creating iam users and attaching user groups to it

read_s3_yaml.py -> reads the yaml file from the s3 bucket with the provided Bucket and Key names and creates users and attaches user groups

To create the zip file for the lambda layer with required dependencies, run the following commands:

```sh
mkdir layer/python/lib/python3.11/site-packages/
cd layer
pip install --no-user -t .\python\lib\python3.11\site-packages\ pyyaml
```

then to zip the python folder: 
```
zip -r my_layer.zip python 
```
or right-click and zip it.
rename the zipped folder to lambda_layer and done
