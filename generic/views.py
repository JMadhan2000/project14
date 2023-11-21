from django.shortcuts import render

# Create your views here.
def crusher(request):
    return render(request,'crusher.html')

def alludu(request):
    return render(request,'alludu.html')