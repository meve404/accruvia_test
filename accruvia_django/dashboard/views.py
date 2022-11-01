from django.shortcuts import render
from django.http import HttpResponse

def dash_home(request):

    return HttpResponse('''<h1>Hello Accruvia Team</h1>
                            <h3>Please go to /admin to see the tweets</h3>
                            <h3>Please go to /accruvia-api to see the routes''')