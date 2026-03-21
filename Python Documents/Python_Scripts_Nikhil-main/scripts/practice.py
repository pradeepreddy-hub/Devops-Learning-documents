mydict={
"name": "Nikhil",
"id": 1234,
"domain": ["devops", "cloud engineer", "SRE"],
"tools": {"os": ["linux", "windows"],"cloud": "AWS"}
}

print(mydict)
print(mydict["name"])
print(mydict["id"])
print(mydict["domain"])
print(mydict["domain"][0])
print(mydict["tools"]["os"][1])
mydict1={
"name1": "John"
}

mydict.update(mydict1)
print(mydict)
