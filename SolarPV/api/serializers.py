from rest_framework import serializers
from .. models import *

class UserSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = User
		fields = ['userID', 'clientID', 'firstname', 'middlename', 'lastname', 'job_title', 'email', 'officephone', 'cellphone', 'password', 'prefix',]
class ClientSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Client
		fields = ['clientID', 'clientname', 'clientType',]
class LocationSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Location
		fields = ['LocationID', 'clientID', 'address1', 'address2', 'city', 'state', 'postalcode', 'country', 'phonenumber', 'faxnumber',]
class ServiceSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Service
		fields = ['serviceID', 'serviceName', 'description', 'isFIrequired', 'FIfrequency', 'standardID',]
class TestStandardSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = TestStandard
		fields = ['standardID', 'stnadardName', 'description', 'publisheddate',]
class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product			
		fields = ['modelNum', 'productname', 'celltechnology', 'cellmanufacture', 'numberofcells', 'numberofcellsinseries', 'numberofseriesinstrings', 'numberofdiodes', 'productlength',  'productwidth', 'productweight', 'superstratetype', 'superstratemanufacturer', 'frametype', 'frameadhesive', 'encapsulanttype', 'encapsulantmanufacturer', 'junctionboxtype', 'junctionboxmanufacturer',]	
class PerformanceDataSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = PerformanceData
		fields = ['modelNums', 'sequenceIDs', 'maxsystemvoltage', 'opencircuitvoltage', 'shortcircuitcurrent', 'voltageatmaxpower', 'currentatmaxpower', 'maxpoweroutput', 'fillfactor',]
class TestSequenceSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = TestSequence
		fields = ['sequenceID', 'sequencename',]
class CertificateSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Certificate
		fields = ['certificateID', 'certnumber', 'locationID', 'reportnumber', 'userID', 'standardID', 'modelNum', 'issuedate']		
