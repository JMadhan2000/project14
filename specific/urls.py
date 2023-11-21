from django.urls import path
from specific.views import *
app_name='specific'
urlpatterns=[
    path('sunil/',sunil,name='sunil'),
    path('sanju/',sanju,name='sanju'),
]