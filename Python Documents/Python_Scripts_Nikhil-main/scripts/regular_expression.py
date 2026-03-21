import re

email_id="nikhilpatil <nikhilpatil027@gmail.com>, <abc123@gmail.com>"
result=re.search(r"nikh", email_id)
print(result)

result=re.search(r"nikhil", email_id)
print(result)

print("---------------------------------------------------")
result=re.search(r"nikhiln", email_id)
print(result)

result=re.findall(r"nikh", email_id)
print(result)

result=re.search(r"nik[h,l]", email_id)
print(result)

print("---------------------------------------------------")
result=re.search(r"nik[a-z]", email_id)
print(result)
result=re.search(r"nik[a-z]{3}", email_id)
print(result)

result=re.search(r"nik[a-z]+", email_id)
print(result)

print("--------------------------------------------------")

result=re.search(r"[A-Za-z0-9_]+@[A_Za-z0-9]+\.[a-z]+", email_id)    #with search command
print(result)

result=re.findall(r"[A-Za-z0-9_]+@[A_Za-z0-9]+\.[a-z]+", email_id)
print(result)

print("----------------------------------------------------")
result=re.search(r"\w+@\w+\.\w+", email_id)
print(result)
