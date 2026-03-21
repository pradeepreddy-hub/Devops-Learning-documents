import boto3
import os

ec2 = boto3.client("ec2")
key_pair_name = "pyuser2"

response = ec2.create_key_pair(KeyName=key_pair_name)
local_key = "pyuser2.pem"

with open(local_key, "w") as f:
  f.write(response['KeyMaterial'])
f.close()

print(f"Key {key_pair_name} created on AWS.")
print(f"Key {local_key} created on local VM.")

os.chmod(local_key,0o400)
print(f"Key {local_key} permission changed to 400")
