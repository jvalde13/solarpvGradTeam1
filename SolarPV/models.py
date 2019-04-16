from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    userID = models.AutoField(max_length=100, primary_key=True)
    clientID = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    officephone = models.CharField(max_length=15)
    cellphone = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    prefix = models.CharField(max_length=8, choices=(('Dr.', ('DR.')), ('Mr.', ('MR.')), ('Mrs.', ('MRS.'))))

    def __str__(self):
          return self.firstname

class Client(models.Model):
    clientID= models.AutoField(max_length=100, primary_key=True)
    clientname = models.CharField(max_length=50)
    clientType = models.CharField(max_length=50)

class Location(models.Model):
    locationID= models.AutoField(max_length=100, primary_key=True)
    clientID= models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    address1 = models.TextField(max_length=200)
    address2 = models.TextField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postalcode = models.IntegerField()
    country = models.CharField(max_length=50)   
    phonenumber = models.CharField(max_length=15)
    faxnumber = models.CharField(max_length=15)   

class Service(models.Model):
    serviceID= models.AutoField(max_length=100, primary_key=True)
    serviceName = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    isFIrequired = models.CharField(max_length=50)
    FIfrequency = models.CharField(max_length=50)
    standardID= models.ForeignKey('TestStandard', on_delete=models.SET_NULL, null=True)

class TestStandard(models.Model):
    standardID = models.AutoField(max_length=100, primary_key=True)
    serviceName = models.CharField(max_length=50)	
    description = models.CharField(max_length=200)
    publisheddate = models.DateField(null=True, blank=True)

class Product(models.Model):
    modelNum = models.AutoField(max_length=100, primary_key=True)
    productname = models.CharField(max_length=50)	
    celltechnology = models.CharField(max_length=200)
    cellmanufacture = models.DateField(null=True, blank=True)	
    numberofcells = models.IntegerField()
    numberofcellsinseries = models.IntegerField()   
    numberofseriesinstrings = models.IntegerField() 
    numberofdiodes = models.IntegerField()
    productlength = models.CharField(max_length=50)
    productwidth = models.CharField(max_length=50)     
    productweight = models.CharField(max_length=50)
    productweight = models.CharField(max_length=50)
    superstratetype = models.CharField(max_length=50)
    superstratemanufacturer = models.CharField(max_length=50)
    substratetype = models.CharField(max_length=50)
    substratemanufacturer = models.CharField(max_length=50)    
    frametype = models.CharField(max_length=50)
    frameadhesive = models.CharField(max_length=50)
    encapsulanttype = models.CharField(max_length=50)
    encapsulantmanufacturer = models.CharField(max_length=50)
    junctionboxtype = models.CharField(max_length=50)
    junctionboxmanufacturer = models.CharField(max_length=50)

class PerformanceData(models.Model):
    modelNum = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    sequenceID = models.ForeignKey('TestSquence', on_delete=models.SET_NULL, null=True)
    maxsystemvoltage = models.CharField(max_length=50)   
    opencircuitvoltage = models.CharField(max_length=50)
    shortcircuitcurrent = models.CharField(max_length=50)
    voltageatmaxpower = models.CharField(max_length=50)
    currentatmaxpower = models.CharField(max_length=50)
    maxpoweroutput = models.CharField(max_length=50)  
    fillfactor = models.CharField(max_length=50)  

class TestSquence(models.Model):
    sequenceID= models.AutoField(max_length=100, primary_key=True)
    sequencename = models.CharField(max_length=50)

class Certificate(models.Model):
    certificateID = models.AutoField(max_length=100, primary_key=True)
    certnumber = models.CharField(max_length=50)
    locationID= models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    reportnumber = models.CharField(max_length=50)
    userID= models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    standardID= models.ForeignKey('TestStandard', on_delete=models.SET_NULL, null=True)
    modelNum = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    issuedate = models.DateField(null=True, blank=True)

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
