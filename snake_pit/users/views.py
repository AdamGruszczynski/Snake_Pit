from django.shortcuts import render


def profile_page(request):
	return render(request, 'Profile_Page.html')

def profile_edit_page(request):
	return render(request, 'Edit_Create_Profile.html')

def login_register_page(request):
	return render(request, 'register.html')