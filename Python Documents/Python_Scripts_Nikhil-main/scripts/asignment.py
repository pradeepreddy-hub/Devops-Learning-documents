mydict1={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect": "Allow",
      "Action": ["iam:ChangePassword"],
      "Resource": "*"
    },
    {
      "Sid": "SecondStatement",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "ThirdStatement",
      "Effect": "Allow",
      "Action": [
        "s3:List*",
        "s3:Get*"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data",
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data/*"
      ],
      "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
    }
  ]
}
print(mydict1)
print(mydict1["Version"])
print(mydict1["Statement"][1]["Sid"])
#print(mydict1["Statement"][2]["Resource"][1])
#print(mydict1["Statement"][2]["Action"][0])
#print(mydict1["Statement"][2]["Condition"]["Bool"])
#print(mydict1["Statement"][2]["Sid"])
