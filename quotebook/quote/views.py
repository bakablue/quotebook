from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.utils import timezone

from .models import Quote
from .models import Author
from .forms import QuoteForm

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

#def add_quote(request):
#    template = loader.get_template('form/add_quote.html')
#    context = RequestContext(request)
#    return HttpResponse(template.render(context))

# View to add quotes
def add(request):
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
                author = Author(author_text=a)
                author.save()
                q.authors.add(author)
            return HttpResponse("Thanks.")
    else:
        form = QuoteForm()
    return render(request, 'quote/add.html', { 'form' : form })
