from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect

#login
def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            context['login_failed'] = True
    return render(request, 'useraccounts/login.html', context)
#logout
def user_logout(request):
    logout(request)
    return redirect('frontpage')
#register
def user_register(request):
    context = {}
    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.set_password(request.POST.get('password'))
        user.save()
        context['user_saved_successfully'] = True
    return render(request, 'useraccounts/register.html', context)

# for editing account information on user
def user_account(request):
    context = {}
    if request.method == "POST":
        user = request.user
        if User.objects.filter(email=request.POST['email']).exclude(pk=user.id).exists():
            context['email_exist'] = True
        else:
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.email = request.POST.get('email')
            user.save()
            context['user_saved_successfully'] = True
    return render(request, 'useraccounts/account.html', context)