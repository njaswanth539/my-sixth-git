from django.shortcuts import render

# Create your views here.

def jasu(request):
    d={'name':'jasu'}
    return render(request,'jasu.html', d )


