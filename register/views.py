from django.shortcuts import render
from .models import User
# Create your views here.
def index_page(request):
    return render(request,"register/index.html")


def register_page(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # User.objects.create(username = username,password = password)
        # obj, created = User.objects.get_or_create(username = username,password = password)
        # print(obj,created)
        if User.objects.filter(username=username).exists():
            if User.objects.filter(username=username,password = password).exists():
                return render(request,"register/further.html")
            else:
                # context = {}
                return render(request,"register/register.html")
        else:
            User.objects.create(username = username,password = password)
            return render(request,"register/further.html")
    else:
        return render(request,"register/register.html")

def further_view(request):
    return render(request,"register/further.html")













# User.objects.create()
