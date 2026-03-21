import boto3

def get_ec2_instance_tags(region):
    ec2_client = boto3.client("ec2", region_name=region)
    response = ec2_client.describe_instances()

    instance_tags = {}

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            tags = instance.get("Tags", [])
            instance_tags[instance_id] = {tag["Key"]: tag["Value"] for tag in tags}

    return instance_tags

if __name__ == "__main__":
    region = "ap-south-1"
    tags = get_ec2_instance_tags(region)

    for instance_id, tag_dict in tags.items():
        print(f"Instance ID: {instance_id}")
        for key, value in tag_dict.items():
            print(f"  {key}: {value}")
        print("-")
