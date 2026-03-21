def display(filename):
    with open(filename,"r") as fh:
        print(fh.read())
    return filename
filename = "1.txt"
var  = display(filename)
print(f"{var}")


