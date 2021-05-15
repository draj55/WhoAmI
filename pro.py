class Patient:
    def __init__(self, Code,Name,age,docterName,billAmmount):
        self.Code=Code
        self.Name=Name
        self.age=age
        self.docterName=docterName
        self.billAmmount=billAmmount
    def myfunc(self):
        print("Hello my name is ",self.Code,self.Name,self.age,self.docterName,self.billAmmount)
class Docter(Patient):
    def __init__(self,Docter,plist):
        self.Docter=Docter
        self.plist=plist
    def findPatientWithMaximumAge(self):
        age=[]
        for i in range(5):
           age.append(self.plist[i]["age"])
        print(max(age))
    def sortPatientByBillAccount(self):
        billAmmount=[]
        for i in range(5):
           billAmmount.append(self.plist[i]["billAmmount"])
        print(sorted(billAmmount))
           
data=[
    {
        "code":1,
        "name": "Arman Singh",
        "age": 23,
        "docterName":"Dr.Akul Kumar",
        "billAmmount":3000
    },
     {
        "code":2,
        "name": "Aksay Kumar",
        "age": 25,
        "docterName":"Dr.ankith raj",
        "billAmmount":2000
    },
    {
        "code":3,
        "name": "Mamatha ",
        "age": 55,
        "docterName":"Dr.Akash",
        "billAmmount":500
    },
    {
        "code":4,
        "name": "Kulkarni",
        "age": 38,
        "docterName":"Dr.anirudd",
        "billAmmount":1000
    },
    {
        "code":5,
        "name": "anupama",
        "age": 18,
        "docterName":"Dr.anusha",
        "billAmmount":200
    },
]
if __name__=="__main__":
    p2=Docter("raj",data)
    p2.findPatientWithMaximumAge()
    p2.sortPatientByBillAccount()

