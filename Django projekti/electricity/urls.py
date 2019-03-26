from django.urls import path
from . import views

urlpatterns = [
    #path('electricity/', views.electricity, name='electricity-tuotto'),
    path('electricity/', views.timeline, name='electricity-tuotto'),
]

