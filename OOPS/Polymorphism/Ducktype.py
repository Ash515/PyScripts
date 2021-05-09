class Vscode():
    def execute(self):
        print("code is compiling and code is running")
class Pycharm():
    def execute(self):
        print("code is compiling and code is running")
class python():
    def execute(self):
       print("python is using")
class CPP():
    def execute(self):
       print("C++ is using")


class Laptop():
    def code(self,ide,lang):
        ide.execute(self)
        lang.execute(self)


lap1=Laptop()
lap1.code(Vscode,python)
lap1.code(Pycharm,CPP)



