from django.shortcuts import render


def find_survey_page(request):
	return render(request, 'Find_Survey.html')

def take_survey_page(request):
	return render(request, 'TakeASurvey.html')

def my_survey_page(request):
	return render(request, 'MySurveys.html')

def create_survey_page(request):
	return render(request, 'Create_Survey.html')

def survey_results_page(request):
	return render(request, 'Survey_Result.html')