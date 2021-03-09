from django.shortcuts import render
def index(request):
    return render(request, 'loginRegister/index.html')
def styleform(request):
    return render(request, 'loginRegister/styleform.css')
