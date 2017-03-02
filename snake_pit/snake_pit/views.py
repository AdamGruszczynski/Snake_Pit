from django.shortcuts import render

def home_page(request):
	return render(request, 'HomePage.html')

	
def about_us(request):
	return render(request, 'AboutUs.html')

def help_page(request):
	return render(request, 'Help.html')