from django.shortcuts import render

# Create your views here.
def default(request):
	return render(request, 'SolarPV/ift598_pd1.html')

def home(request):
	return render(request, 'SolarPV/ift598_pd1.html')

def login(request):
	return render(request, 'SolarPV/Login.html')

def email(request):
	return render(request, 'SolarPV/email.html')

def JoinUS(request):
	return render(request, 'SolarPV/JoinUS.html')

#def login(request):
#	form = LoginForm()
#	return render(request, 'class_demo/html', {'form' : form }) 