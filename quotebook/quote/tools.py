from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def send_validation_mail(login, to_email):
    # FIXME: html + confirmation
    subject = "Welcome " + login
    message = login + ", welcome to quotebook application."
    from_email = "admin@quotebook.fr"

    try:
        send_mail(subject, message, from_email, [to_email])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponse('Thanks.')


