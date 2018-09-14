from django.urls import path
from . import views
app_name = 'test_4u'

urlpatterns = [
    path('', views.index, name='index'),
]