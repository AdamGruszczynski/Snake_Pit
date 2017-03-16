from django.contrib import admin

from .models import Survey, Result, Pending

admin.site.register(Survey)
admin.site.register(Result)
admin.site.register(Pending)

