from django.shortcuts import render,redirect
from django.contrib import messages
from events.forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You have to logout first!!!')
        return redirect('/')
    else:
        form = CustomUserForm()
        if request.method == 'POST':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                messages.success(request, f"Account has been created for {username}! Login to continue")
                return redirect('/login')
                                
        context = {'form': form}
    return render(request, 'events/auth/register.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/login')
        else:
            return render(request, 'events/auth/login.html')
    
# def logoutpage(request):
#     logout(request)
#     if 'username' in request.session:
#         del request.session['username']
#         messages.success(request, 'Logged out successfully')
#     return redirect('/')
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out successfully')
    return redirect('loginpage')
    