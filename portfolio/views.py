from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.contrib import messages

from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods

from .models import Contact

from django.db import IntegrityError

# Create your views here.

def home(request):

    rq_old_input = ''

    if 'old_input' in request.session.keys():
        rq_old_input = request.session['old_input']

    context = {
        'rvalues': rq_old_input
    }

    if 'old_input' in request.session.keys():
        del request.session['old_input']

    return render(request, 'home.html', context)

@require_http_methods(["POST"])
def contact_us(request):

    status = False
    msg = ''
    invalid_field = ''

    # get old input 
    request.session['old_input'] = request.POST

    # get all the request 
    rq_name = request.POST['name']
    rq_email = request.POST['email']
    rq_subject = request.POST['subject']
    rq_message = request.POST['message']

    # save in the database 
    contact = Contact(name=rq_name, email=rq_email, subject=rq_subject, message=rq_message)
    
    try:
        contact.save()
        status = True
    except IntegrityError as e:
        status = False
        msg = str(e.__cause__)
        invalid_field = msg.split('.')[1]
        msg = msg.split('.')[1] + ' is already exit'

    if status:
        # send email 
        email_send = send_mail(
            rq_subject,
            rq_message,
            'kyawhtet.today@gmail.com',
            [rq_email],
        )

        if not email_send:
            msg = 'Your email is invalid'
            status = False
        else:
            msg = 'You just send successfully!'
            status = True

    if not status:
        messages.error(request, msg)
        return redirect('home')
    else:
        # messages.success(request, msg)
        return redirect('contact_complete')


def contact_complete(request):
    
    context = {}
    return render(request, 'contact_complete.html', context)
