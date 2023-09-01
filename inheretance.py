#task 1  Defining a Person class and its properties and method 
# 1- Create a class called Person have constructor (name, age, gender, habit)
# 2- Create a child class called Student inhereted from parent class Person
# 3- Student has courses so add it in class Student constructor and call parent super constructor by using super() keyword and add same lecture data
# 4- use encabsulation concept by using get all data and set all data in Student class.
# 5- create method in Student class display all data of this student
# 6- Create another child class called Teacher inhereted from parent class Person
# 7- Teacher has subject so add it in class teacher constructor and call parent super constructor by using super() keyword
# 8- use encabsulation concept by using get subject and set subject in teacher class
# 9- create method in teacher class display all data of this teacher

class person :
     #protected data member
    _age = None
     #private data member
    __gpa=None
     
    def __init__(self,name,email ,age ,gpa):
        
        self.name=name #public data members
        self.email=email #public data members
        self._age= age
        self.__gpa=gpa
        
      #public member function
    def print_info(self):
        print('name:' ,self.name,end='\n ')
        print('email:',  self.email ,end='\n' )
        
      #protected member function
    def _displayAge(self):
        print("age:" , self._age ,end ="    " )
        
     # private member function
    def __display_gpa(self):
        print("gpa:",self.__gpa)

class student(person):
    _address= None
    def __init__(self, name,email,age,gpa , year):
         student.__init__(self, name, email,age ,gpa,year)
         super().__init__(name, email)
         self.graduationyear =year
        
        #public member function
    def welcome(self):
        print("Welcome", self.name,self.email,self._age,self.__gpa, self.graduationyear ,end='\n') 
    
        # protected member function
    def _displayAddress(self):
        print('address :', self._address)
x = student("Manar", "m@gamil.com", 20 , 4 ,2019)       
obj=person('manar','mm@gamil.com',20,4)
obj.print_info()
x.welcome()
x._displayAddress()