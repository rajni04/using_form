from django.shortcuts import render
from django.contrib.auth import login,logout
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def register(request):
    '''Create '''
    form=StudentForm()
    if request.method=='POST':
        user=request.user
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            student_data=form.save(commit=False)
            student_data.save()
            messages.success(request,'Hi , thank you registration!')

            return redirect('/sign_in')
        else:
            messages.success(request,'Hi , Something wrong you registration!')

    context={
        'form':form,
    }
    return render(request,'app/registration.html',context)

@login_required(login_url="/sign_in")
def update_std(request,pk):
    '''Edit blog'''
    try:
        student=CustomUser.objects.get(id=pk)

        form=StudentForm(instance=student)
        if request.method=='POST':
            form=StudentForm(request.POST,instance=student)
            if form.is_valid():
                form.save()
                return redirect(request.META.get("HTTP_REFERER"))

        context={
            'form':form
        }
    except Exception as e:
        print(e)
    return render(request,'app/edit.html',context)
@csrf_exempt
@login_required(login_url="/sign_in")
def addClass(request):
    '''Create blog'''
    form=ClassForm()
    if request.method=='POST':
        if request.user.is_superuser:
            form=ClassForm(request.POST)
            if form.is_valid():
                stdcls=form.save(commit=False)
                stdcls.save()
                return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.success(request,f'Sorry ,{request.user.first_name},you do not have this permission!')
    context={
        'form':form,
    }
    return render(request,'app/class.html',context)
@csrf_exempt
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'app/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        logging.error("Exception occurred:")
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            logging.error("Exception---- occurred: %s", str(phone_number))
            password = form.cleaned_data['password']
            if phone_number and password:
                user = CustomUser.objects.get(phone_number=phone_number,password=password)
                print("user--",user.status)
                logging.error("Exception))) occurred---: %s", str(user))
                if user.status==2:
                    login(request, user)
                    #messages.success(request,f'Hi{user.first_name} , welcome back!')
                    return redirect('/')
                else:
                    messages.success(request,'You are not activated')
        messages.error(request,f'Invalid username or password')
        return render(request,'app/login.html',{'form': form})
def home(request):
    return render(request, "app/home.html")

def logout_view(request):
    logout(request)
    return redirect('/sign_in')