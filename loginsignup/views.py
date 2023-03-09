from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib import messages # in order for us to display messages
# Create your views here.
from django.contrib.auth import authenticate,login
from rest_framework import viewsets, permissions
from .serializers import UserSerializer,GroupSerializer

def index(request):
    if request.session.get('UserLogin',False):
        del request.session['UserLogin']
        return redirect('mainapp:home')
    else:
        return render(request,'loginsignup/login.html')

def signup(request):
    return render(request,'loginsignup/signup.html')

def handleLogin(request):
     if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser = authenticate(request,username=uname,password=pass1)
        # checking is myuser value is prompt as boolean or not or if user does not exist
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"login Success")
            request.session['UserLogin']=True
            request.session.set_expiry(60)
            return redirect('mainapp:home')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    #  return render(request,'loginsignup/login.html')

def handleSignup(request):
    if(request.method=="POST"):
        uname=request.POST.get("username")
        em=request.POST.get("email")
        pass1=request.POST.get("pass1")
        cpass=request.POST.get("pass2")
        print(uname,em,pass1,cpass)
        if pass1 != cpass:
            # return HttpResponse("password donot match")
            messages.warning(request,"Password incorrect") #
            return redirect("signup")
        
        try:
            if User.objects.get(username=uname):
                messages.info(request,"Username is taken") #
                return redirect("signup")
            
            if User.objects.get(email=em):
                messages.info(request,"Email is taken") #
                return redirect("signup")
        except:
            pass
        myuser = User.objects.create_user(uname,em,pass1)
        myuser.save()
        messages.success(request,"Signup success") #
        return redirect('index')
    
    #  (del) request.session['key'] = value
    #  request.session.get('key','default value') == ? 
        

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

