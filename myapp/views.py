from django.shortcuts import render,redirect
from django.http import HttpResponse # to sent a http response this is used
from django.contrib.auth.models import User, auth #required for user authentication
from django.contrib import messages  #required for user authentication
from .models import Feature
# Create your views here.

# this render request is sent to the templates folder of the base directory.
#multiple variables passing to html
def index(request):
    features =Feature.objects.all() #fetching all the instances of this feature table from the db
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            #check whether the email still exists
            if User.objects.filter(email=email).exists(): 
                #this shows the message if this is the case
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used.')
                return redirect('register')
            else:
                #creates new user 
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else: 
            messages.info(request, 'Password Not the same')
            return redirect('register')
    else:   
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user= auth.authenticate(username=username, password=password)
        
        #now checking whether is thier or not
        #if its None the user is asked to register
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
  
  
def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})
    
    
#single variable passing to html
def counter(request):
    words = request.POST['words'] # this will get the content submitted
    total_words = len(words.split())
    return render(request,'counter.html',{'total_words':total_words})
    