from django.shortcuts import render

def index(request):
    return render(request, 'test_4u/index.html')
