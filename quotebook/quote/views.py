from django.shortcuts           import render
from django.http                import HttpResponse
from django.template            import RequestContext, loader
from django.shortcuts           import render
from django.utils               import timezone
from django.contrib.auth        import authenticate, logout
from django.contrib.auth.models import User

from .models                    import Quote
from .models                    import Author
from .forms                     import QuoteForm
from .forms                     import UserForm
from .forms                     import LoginForm
from .tools                     import *

# Index page
def index(request, page_index=None):
    index = 0
    if page_index and int(page_index) > 0:
        index = (int(page_index) - 1) * 5
    quote_list = Quote.objects.order_by('-pub_date')
    latest_quote_list = quote_list[index:index + 5]
    template = loader.get_template('quote/index.html')
    context = RequestContext(request,
            { 'latest_quote_list' : latest_quote_list,
              'index'             : int(index / 5) + 1,
              'max_page'          : int(len(quote_list) / 5) + 1
            })
    return HttpResponse(template.render(context))

# Test
def detail(request, quote_id):
    return HttpResponse("You're looking at quote %s." % quote_id)

# View to add quotes
def add(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            # Form instance
            form = QuoteForm(request.POST)

            if form.is_valid():
                authors = form.cleaned_data['author']
                context = form.cleaned_data['context']
                quote = form.cleaned_data['quote']
                q = Quote(quote_text=quote,
                          context_text=context,
                          pub_date=timezone.now())
                q.save()

                list_authors = authors.split(', ')
                for a in list_authors:
                    if a not in Author.objects.all():
                        author = Author(author_text=a)
                        author.save()
                q.authors.add(author)
                return HttpResponse("Thanks.")
        else:
            form = QuoteForm()
        return render(request, 'quote/add.html', { 'form' : form })
    else:
        # The user must log in
        return HttpResponseRedirect('/quote/login/')

def vote(request, quote_id, vote_type):
    if request.user.is_authenticated():
        q = Quote.objects.get(id=quote_id)
        if vote_type == 'like' and request.user not in q.auth_likes.all():
            if request.user in q.auth_hates.all():
                q.auth_hates.remove(request.user)
            q.auth_likes.add(request.user)
        elif vote_type == 'hate' and request.user not in q.auth_hates.all():
            if request.user in q.auth_likes.all():
                q.auth_likes.remove(request.user)
            q.auth_hates.add(request.user)
    else:
        pass
    return HttpResponseRedirect('/quote/')

# User management

# FIXME: error management
def signup(request):
    if request.method == 'POST':
        # Form instance
        form = UserForm(request.POST)

        if form.is_valid():
            login = form.cleaned_data['login']
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            pass_confirmation = form.cleaned_data['pass_confirmation']
            if password == pass_confirmation:
                user = User.objects.create_user(login, mail, password)
                user.save()
                #send_validation_mail(login, mail)
    else:
        form = UserForm()
    return render(request, 'quote/signup.html', { 'form' : form })


def login(request):
    if request.method == 'POST':
        # Form instance
        form = LoginForm(request.POST)

        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=login, password=passwd)
            if user is not None:
                # User exist
                if user.is_active:
                    # Enabled account
                    pass
                else:
                    # Disabled account
                    pass
            else:
                # Incorrect password/user
                pass
    else:
        form = LoginForm()
    # FIXME: errors etc
        return render(request, 'quote/login.html', { 'form' : form })

def disconnect(request):
    logout(request)
    return HttpResponseRedirect('/quote/')
