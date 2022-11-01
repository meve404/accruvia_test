from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('get-tweets/', views.get_tweets),

    #-----------POST-----------------
    path('make-tweet/<str:name>/<str:tweeText>', views.make_tweet)
]