from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d={'name':'jasu'}

    return render(request,'jinja_print.html',context=d)


def apple(request):
    d={'name':'good'}

    return render(request,'apple.html',d)