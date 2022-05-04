#closure functions
def getmarks(rollno):
    print("validate the roll no")
    def submarks(subname):
        print("subject name is",subname,"roll num is",rollno)
    return submarks

r=getmarks(1)
r('python')
r('computer')        