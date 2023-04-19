from django.urls import path
from.views import *

urlpatterns=[
    path('studentregister/',student),
    path('studentdetail/',studentdetail)
]