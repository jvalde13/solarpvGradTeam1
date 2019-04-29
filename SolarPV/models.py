from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    userID = models.CharField(max_length=100, primary_key=True)
    clientID = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    officephone = models.CharField(max_length=15, blank=True)
    cellphone = models.CharField(max_length=100, blank=True)
    prefix = models.CharField(max_length=8, choices=(('Dr.','Dr.'),('Mr.', 'Mr.'),('Mrs.', 'Mrs.'),('Miss', 'Miss')))
 
    def __str__(self):
          return self.userID

class Client(models.Model):
    clientID= models.CharField(max_length=100, primary_key=True)
    clientname = models.CharField(max_length=50)
    clientType = models.CharField(max_length=50)

    def __str__(self):
          return self.clientID

class Location(models.Model):
    locationID= models.CharField(max_length=100, primary_key=True)
    clientID= models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    address1 = models.TextField(max_length=200)
    address2 = models.TextField(max_length=200, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True)
    postalcode = models.CharField(max_length=50) 
    country = models.CharField(max_length=50)   
    phonenumber = models.CharField(max_length=15, blank=True)
    faxnumber = models.CharField(max_length=15, blank=True)   

    def __str__(self):
          return self.locationID    

class Service(models.Model):
    serviceID= models.CharField(max_length=100, primary_key=True)
    serviceName = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True)
    isFIrequired = models.CharField(max_length=50)
    FIfrequency = models.CharField(max_length=50)
    standardID= models.ForeignKey('TestStandard', on_delete=models.SET_NULL, null=True)


    def __str__(self):
          return self.serviceID 

class TestStandard(models.Model):
    standardID = models.CharField(max_length=100, primary_key=True)
    standardName = models.TextField(max_length=150)	
    description = models.TextField(max_length=400)
    publisheddate = models.DateField(null=True, blank=True)

    def __str__(self): 
        return self.standardID

class Product(models.Model):
    modelNum = models.CharField(max_length=100, primary_key=True)
    productname = models.CharField(max_length=50)
    celltechnology = models.CharField(max_length=200, blank=True)
    cellmanufacture = models.CharField(max_length=50, null=True, blank=True)
    numberofcells = models.CharField(max_length=50, blank=True)
    numberofcellsinseries = models.CharField(max_length=50, blank=True)
    numberofseriesinstrings = models.CharField(max_length=50, blank=True)
    numberofdiodes = models.CharField(max_length=50, blank=True)
    productlength = models.CharField(max_length=50, blank=True)
    productwidth = models.CharField(max_length=50, blank=True)
    productweight = models.CharField(max_length=50, blank=True)
    superstratetype = models.CharField(max_length=50, blank=True)
    superstratemanufacturer = models.CharField(max_length=50, blank=True)
    substratetype = models.CharField(max_length=50, blank=True)
    substratemanufacturer = models.CharField(max_length=50, blank=True)    
    frametype = models.CharField(max_length=50, blank=True)
    frameadhesive = models.CharField(max_length=50, blank=True)
    encapsulanttype = models.CharField(max_length=50, blank=True)
    encapsulantmanufacturer = models.CharField(max_length=50, blank=True)
    junctionboxtype = models.CharField(max_length=50, blank=True)
    junctionboxmanufacturer = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.modelNum

class TestSequence(models.Model):
    sequenceID = models.CharField(max_length=100, primary_key=True)
    sequencename = models.CharField(max_length=50)     

    def __str__(self):
        return self.sequenceID       

class PerformanceData(models.Model):
    modelNum = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    sequenceID = models.ForeignKey('TestSequence', on_delete=models.SET_NULL, null=True)
    maxsystemvoltage = models.CharField(max_length=50, blank=True)   
    opencircuitvoltage = models.CharField(max_length=50, blank=True)
    shortcircuitcurrent = models.CharField(max_length=50, blank=True)
    voltageatmaxpower = models.CharField(max_length=50, blank=True)
    currentatmaxpower = models.CharField(max_length=50, blank=True)
    maxpoweroutput = models.CharField(max_length=50, blank=True) 
    fillfactor = models.CharField(max_length=50, blank=True)
  


class Certificate(models.Model):
    certificateID = models.CharField(max_length=100, primary_key=True)
    certnumber = models.CharField(max_length=50)
    locationID= models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    reportnumber = models.CharField(max_length=50)
    userID= models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    standardID= models.ForeignKey('TestStandard', on_delete=models.SET_NULL, null=True)
    modelNum = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    issuedate = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.certificateID 
#class Department(models.Model):
#    name= models.CharField(max_length=50, help_text="Enter the department name.")
#    number= models.CharField(max_length=10, primary_key= True)
#    mgr_ssn = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
#    mgr_startdate = models.DateField(null=True, blank=True)

#    def __str__(self):
#           return self.number

#class Project(models.Model):
#    name= models.CharField(max_length=50)
 #   number= models.CharField(max_length=10, primary_key=True)
 #   location= models.TextField()
  #  dnum= models.ForeignKey(Department,on_delete=models.CASCADE)
   
#    class Meta:
 #   ordering ['-number']

#    def __str__(self):
 #       return self.name

#class Workson(models.Model):
 #   project = models.ForeignKey(Project, on_delete=models.CASCADE)
 #   essn = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
 #   hours = models.IntegerField()
   
#class Contact(models.Model):
 #   username = models.CharField(max_length=10)
  #  firstname = models.CharField(max_length=50)
  #  lastname =models.CharField(max_length=50)
  #  address = models.TextField()
  #  email = models.EmailField()
  #  phone = models.CharField(max_length=15)

   # def __str__(self):
   #     return "Name : %s %s, Address: %s, Email: %s, Phone: %s, Username:%s" % (self.firstname, self.lastname, self.address, self.email, self.phone, self.username)
#class Response(models.Model):
 #   name = models.CharField(max_length=50)
  #  def __str__(self):
   #     return "Response : %s"

#class Message(models.Model):
 #   name = models.CharField(max_length=50)
  #  email = models.EmailField()
   # Message = models.TextField()
    #message_date = models.DateTimeField(default=timezone.now)
    #user = models.ForeignKey(Contact, on_delete= models.CASCADE)

 #   response = models.ManytoManyField(Response)

  #  def __str__ (self):
  #      return "Name: %s, Email: %s, Date: %s, \n%s" %(self.name, self.email, self.message, self.message_date, self.message )
