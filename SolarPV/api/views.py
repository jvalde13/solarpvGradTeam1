from rest_framework import generics
from .. models import *
from . serializers import UserSerializer, ClientSerializer, LocationSerializer, ServiceSerializer, TestStandardSerializer, ProductSerializer, PerformanceDataSerializer, TestSequenceSerializer, CertificateSerializer

class UserListView(generics.ListAPIView): 
	queryset = User.objects.all() 
	serializer_class = UserSerializer
class UserDetailView(generics.RetrieveAPIView): 
	queryset = User.objects.all() 
	serializer_class = UserSerializer

class ClientListView(generics.ListAPIView): 
	queryset = Client.objects.all() 
	serializer_class = ClientSerializer
class ClientDetailView(generics.RetrieveAPIView): 
	queryset = Client.objects.all() 
	serializer_class = ClientSerializer

class LocationListView(generics.ListAPIView): 
	queryset = Location.objects.all() 
	serializer_class = LocationSerializer
class LocationDetailView(generics.RetrieveAPIView): 
	queryset = Location.objects.all() 
	serializer_class = LocationSerializer

class ServiceListView(generics.ListAPIView): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer
class ServiceDetailView(generics.RetrieveAPIView): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer

class TestStandardListView(generics.ListAPIView): 
	queryset = TestStandard.objects.all() 
	serializer_class = TestStandardSerializer
class TestStandardDetailView(generics.RetrieveAPIView): 
	queryset = TestStandard.objects.all() 
	serializer_class = TestStandardSerializer

class ProductListView(generics.ListAPIView): 
	queryset = Product.objects.all() 
	serializer_class = ProductSerializer
class ProductDetailView(generics.RetrieveAPIView): 
	queryset = Product.objects.all() 
	serializer_class = ProductSerializer

class PerformanceDataListView(generics.ListAPIView): 
	queryset = PerformanceData.objects.all() 
	serializer_class = PerformanceDataSerializer
class PerformanceDataDetailView(generics.RetrieveAPIView): 
	queryset = PerformanceData.objects.all() 
	serializer_class = PerformanceDataSerializer

class TestSequenceListView(generics.ListAPIView): 
	queryset = TestSequence.objects.all() 
	serializer_class = TestSequenceSerializer
class TestSequenceDetailView(generics.RetrieveAPIView): 
	queryset = TestSequence.objects.all() 
	serializer_class = TestSequenceSerializer

class CertificateListView(generics.ListAPIView): 
	queryset = Certificate.objects.all() 
	serializer_class = CertificateSerializer
class CertificateDetailView(generics.RetrieveAPIView): 
	queryset = Certificate.objects.all() 
	serializer_class = CertificateSerializer