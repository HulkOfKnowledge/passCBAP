from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            try:
                existing_user = User.objects.get(username=username)
                messages.error(request, 'Incorrect password! ')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist. Please sign up!')

    return render(request, 'FormsInterface/sign-in.html', {'messages': messages.get_messages(request)})

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['sname']
        password = request.POST['password1']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists! Please choose a different username.')
            return render(request, 'FormsInterface/sign-up.html')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists! Please use a different email address.')
            return render(request, 'FormsInterface/sign-up.html')

        # Create the user
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return render(request, 'FormsInterface/sign-in.html')

    return render(request, 'FormsInterface/sign-up.html')

def sign_out(request):
    logout(request)
    return redirect('home')