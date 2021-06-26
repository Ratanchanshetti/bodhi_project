from django.shortcuts import render,redirect
from django.conf import settings as set 
#for sending emails
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# to send e-mails
from django.contrib import messages
from socket import gaierror
#for exceptions
from smtplib import SMTPAuthenticationError, SMTPDataError
# modael imported and using it 
from webapp.models import carousel,functionality,cleints,About_us
from webapp.forms import ContactForm
#global variable to set the title from the object and that btech given to value
from django.http import request
btech=set.CNAME
#s=set.FIRST



# Create your views here.
def hompage(request):
    return render(request,"layout/weblayout.html")\

def webapp_homepage(request):
    #the class carousel is saved in one object
    car=carousel.objects.all()
    #the class functionality is saved in two object
    func=functionality.objects.all()
    #the class clients is saved in three object
    c=cleints.objects.all()
    obj=About_us.objects.all()
    page_title="indexpage"
    text="homepage"
    one="Bodhi Technology"
    second="Why You Choose Us?"
    third="Our clients"
    fourth="About Us"
    context={'title':page_title,
    'text':text,
    'o':btech,
    'p':second,
    'r':third,
    's':fourth,'carousel':car,'fun':func,'cleint':c,'about':obj}
    return render(request,"webpages/index.html",context)



def web_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            person_name=form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            user_number=form.cleaned_data['number']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message_send="\n Name : "+person_name+"\n User Email : "+user_email+"\n user_number :"+ user_number + "\n Subject : "+subject +"\n Message : "+message
            from_email=set.EMAIL_HOST_USER
            try:
                send_mail(subject,message_send,from_email, ['ratanchanshetti99@gmail.com'])
            except (BadHeaderError,gaierror,SMTPAuthenticationError,SMTPDataError):
                messages.error(request,"Check your Internet connection... Try again")
                return redirect('mycontact')
            messages.success(request,"Thank you for contacting school! Your form successfully submited")
            return redirect('mycontact')
    context = {
         'form': form,
        
             }             
    return render(request, "webpages/contact.html",context)
