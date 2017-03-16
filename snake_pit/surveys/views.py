from django.shortcuts import render
from django.http import HttpResponse


def find_survey_page(request):
	return render(request, 'Find_Survey.html')

def take_survey_page(request):
	return render(request, 'TakeASurvey.html')

def my_survey_page(request):
	return render(request, 'MySurveys.html')

def create_survey_page(request):
	return render(request, 'Create_Survey.html')

def survey_results_page(request):
	survey = {'surveyChoice1': 1, 'surveyChoice2':2}
	results = {'resultsChoice1': 1, 'resultsChoice2':2}


	return render(request, 'Survey_Result.html', {'survey':survey,'results': results})