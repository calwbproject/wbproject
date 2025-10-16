from django.shortcuts import render

# Create your views here.
def logoutTest(request):
    return render(request, 'common/index.html')