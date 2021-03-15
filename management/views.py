from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Vtrainer, Vdetails
from .models import Trainer, Details


# Create your views here.
def homepage(request):
    return render(request, 'mainpage.html', {})


def login_management(request):
    u = 'magesh'
    p = '0003'
    un = request.POST.get('user')
    up = request.POST.get('pswd')
    if request.method == 'POST':
        if u == un and p == up:
            return HttpResponseRedirect('/create_account/')
        else:
            return HttpResponse('Invalid username and password')
    return render(request, 'login.html', {})


def create_account(request):
    if request.method == 'POST':
        name = request.POST['your_name']
        email = request.POST['your_email']
        password = request.POST['your_pwd']
        role = request.POST['your_role']
        Trainer.objects.create(name=name, email=email, password=password, role=role)
        return HttpResponseRedirect('/send_mail/')
    return render(request, 'account.html', {})


def created(request):
    return HttpResponse('successfully registered')


def trainer(request):
    if request.method == 'POST':
        ut = request.POST.get('username')
        pt = request.POST.get('pwd')
        rt = request.POST.get('role')
        data = Trainer.objects.all().filter(name=ut, password=pt, role=rt)
        print(data)
        if data:
            return HttpResponseRedirect("/dashboard/")
        else:
            return HttpResponse("Invalid username or password")

    return render(request, 'trainerlogin.html', {})


def dashboard(request):
    if request.method == 'POST':
        t_name = request.POST.get('tname')
        s_name = request.POST.get('sname')
        mob_num = request.POST.get('mob_num')
        course = request.POST.get('course')
        duration = request.POST.get('duration')
        time = request.POST.get('time')
        radio = request.POST.get('confirm')
        Details.objects.create(trainer_name=t_name, student_name=s_name, mob_no=mob_num, course=course,
                               duration=duration, time_slot=time)
        if radio is not None:
            record = {"StudentsInformation": Details.objects.all().filter(trainer_name=t_name)}
            return render(request, 'register.html', record)
    return render(request, 'db.html', {})


def management(request):
    u = 'maahi'
    p = '3000'
    mn = request.POST.get('users')
    mp = request.POST.get('pswds')
    if request.method == 'POST':
        if u == mn and p == mp:
            return HttpResponseRedirect('/search/')
    return render(request, 'mlogin.html', {})


def search(request):
    if request.method == 'POST':
        data = request.POST.get('searchs')
        print(data)
        record = {"StudentsInformation": Details.objects.all().filter(trainer_name=data)}
        print(record)
        return render(request, 'register.html', record)
    return render(request, 'search.html', {})


def send_mail(request):
    form_class = Vtrainer  # class not a instance
    context = {'form': form_class}

    # POST REQUEST
    if request.method == 'POST':
        form = Vtrainer(request.POST)

        your_name = request.POST['your_name']
        contact_email = request.POST['your_email']
        password = request.POST['your_pwd']
        role = request.POST['your_role']

        subject = "A new contact or lead - {}".format(your_name)
        content = your_name + '\n' + contact_email + '\n' + str(
            password) + '\n' + role
        email = EmailMessage(subject, content, to=['magesh1699 @gmail.com'])
        email.send()
        return HttpResponseRedirect('/homepage/')

    return render(request, 'account.html', context)


def logout(request):
    return HttpResponseRedirect('/homepage/')
