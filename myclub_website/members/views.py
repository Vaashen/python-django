from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterUserForm

# Create your views here.
def login_user(request):
    """This function will allow the user to login if they already have a account, it will call the userame ad password 
    from the database and check if it matches the details entered by the user, if it does, use the login build-in
    function and redirect them back to the home page, else redirect back to the login page
    
    :return: redirect back to the home page if details are valid 
    :rtype: redirect
    
    :return: if logins details are incorrect, return the login page
    :rtype: redirect 
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, Try again.')
            return redirect('login')
    
    else:
        return render(request, 'authenticate/login.html', {})
    

def logout_user(request):
    """This function will be used whne the user wants to logout of the website.
    It will display a message telling the user that they have been logged out
    
    :return: return them back to the home page
    :rtype: redirect
    """
    logout(request)
    messages.success(request, 'You were logged out.')
    return redirect('home')


def register_user(request):
    """This function will be used to register a new user, it will render in the register form,
    once the user enters all the required details in , and if they are valid, the form will be saved to the database,
    and the user will be logged in and a message will be displayed 
    
    :return: once logged in they will be redirected to the home page
    :rtype: redirect
    
    :return: load the register_user.html file with the form 
    :rtype: render
    """
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful!')
            return redirect('home')
    
    else:
        form = RegisterUserForm()
    
    return render(request, 'authenticate/register_user.html', 
                  {'form': form})
    