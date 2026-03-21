mydict = {
    "name": "nikhil",
    "age": 25,
    "city": "Bengaluru"
          }

if "name" in mydict:
    print("key found")
else:
    print("key not found")

if mydict["name"] == "Hello":
    print("key contains the value")
else:
    print("value not found")

if "nikhil" in mydict.values():
    print("value found")
else:
    print("value not found")

found = True
if found:
    print("True")
else:
    print("false")
