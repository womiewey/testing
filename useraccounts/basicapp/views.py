from django.shortcuts import render
from django.http import HttpResponse
from basicapp.forms import FormName
# Create your views here.


def index(request):
    return render(request,'index.html')

def form_name_view(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('error')           
    return render(request,'signup.html',{'form':form})