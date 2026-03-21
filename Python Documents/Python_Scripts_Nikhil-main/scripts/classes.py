class example:
    def __init__ (self, str1, str2):
        self.name1=str1
        self.name2=str2
        self.name3="Devops"
        self.name4="Nikhil"
    def print_value(self):
        print(self.name1, self.name2, self.name3, self.name4)

    def display_value(self, str2):
        print(str2)



    

var=example('Hello welcome', 'to devops class')
var.print_value()
var.display_value("Training")
