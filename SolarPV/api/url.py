from django.urls import path
from . import views

app_name = 'SolarPV'
urlpatterns = [ 
	path('Users/', views.UserListView.as_view(), name='User_list'), 
	path('Users/<pk>/', views.UserDetailView.as_view(), name='User_detail'),
	path('Clients/', views.ClientListView.as_view(), name='Client_list'), 
	path('Clients/<pk>/', views.ClientDetailView.as_view(), name='Client_detail'),
	path('Locations/', views.LocationListView.as_view(), name='Location_list'), 
	path('Locations/<pk>/', views.LocationDetailView.as_view(), name='Location_detail'),
	path('Services/', views.ServiceListView.as_view(), name='Service_list'), 
	path('Services/<pk>/', views.ServiceDetailView.as_view(), name='Service_detail'),
	path('TestStandards/', views.TestStandardListView.as_view(), name='TestStandard_list'), 
	path('TestStandards/<pk>/', views.TestStandardDetailView.as_view(), name='TestStandard_detail'),
	path('Products/', views.ProductListView.as_view(), name='Product_list'), 
	path('Products/<pk>/', views.ProductDetailView.as_view(), name='Product_detail'),
	path('PerformanceDatas/', views.PerformanceDataListView.as_view(), name='PerformanceData_list'), 
	path('PerformanceDatas/<pk>/', views.PerformanceDataDetailView.as_view(), name='PerformanceData_detail'),
	path('TestSequences/', views.TestSequenceListView.as_view(), name='TestSequence_list'), 
	path('TestSequences/<pk>/', views.TestSequenceDetailView.as_view(), name='TestSequence_detail'),
	path('Certificates/', views.CertificateListView.as_view(), name='certificate_list'), 
	path('Certificates/<pk>/', views.CertificateDetailView.as_view(), name='certificate_detail'),
] 