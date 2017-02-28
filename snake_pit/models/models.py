from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class SurveyPrivacy(models.Model):
    pType = models.CharField(max_length=20)

    def __str__(self):
        return self.pType

class MemberType(models.Model):
    mType = models.CharField(max_length=20)

    def __str__(self):
        return self.mType

##class User(models.Model):
##    memberType = models.ForeignKey(MemberType, on_delete=models.CASCADE,)
##    username = models.CharField(max_length=50, help_text="Username", unique=True)
##    password = models.CharField(max_length=50, help_text="Password")
##
##    def __str__(self):
##        return self.username

class Survey(models.Model):
    privacyID = models.ForeignKey(SurveyPrivacy, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200, help_text="Enter Survey Title")
    description = models.TextField(max_length=1000, help_text="Enter Survey Description")
    choices =  models.FileField(upload_to='uploads/survey_files', null=True)

    def __str__(self):
        return self.title

class Result(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE,)
    result = models.CharField(max_length=200)
    surveyID = models.ForeignKey(Survey, on_delete=models.CASCADE,)

    def __str__(self):
        return self.userID + self.result

class Pending(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE,)
    expire =  models.DateField()
    surveyID = models.ForeignKey(Survey, on_delete=models.CASCADE,)

    def __str__(self):
        return self.surveyID + self.expire

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    memberType = models.ForeignKey(MemberType, on_delete=models.CASCADE,)
    race = models.CharField(max_length=20, help_text="Race", null=True, blank=True)
    gender = models.CharField(max_length=20, help_text="Gender", null=True, blank=True)
    country = models.CharField(max_length=50, help_text="Country", null=True, blank=True)
    city = models.CharField(max_length=50, help_text="City", null=True, blank=True)
    state = models.CharField(max_length=50, help_text="State", null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

