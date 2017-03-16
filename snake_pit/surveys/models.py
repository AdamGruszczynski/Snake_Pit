from django.db import models
from django.utils import timezone
from users.models import User

class Survey(models.Model):
    private = models.BooleanField()
    title = models.CharField(max_length=200, help_text="Enter Survey Title")
    description = models.TextField(max_length=1000, help_text="Enter Survey Description")
    choices =  models.FileField(upload_to='uploads/survey_files', null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

class Result(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE,)
    result = models.CharField(max_length=200)
    surveyID = models.ForeignKey(Survey, on_delete=models.CASCADE,)

    def __str__(self):
        return (str(self.surveyID) + " - " + str(self.userID) + " results")

class Pending(models.Model):
    
    userID = models.ForeignKey(User, on_delete=models.CASCADE,)
    expire =  models.DateField()
    surveyID = models.ForeignKey(Survey, on_delete=models.CASCADE,)

    def __str__(self):
        return (str(self.surveyID) +" : " + str(self.expire))
