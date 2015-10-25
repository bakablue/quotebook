from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_text = models.CharField('Author', max_length=300)
    def __str__(self):
        return self.author_text

class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    quote_text = models.CharField('Quote', max_length=1000)
    authors = models.ManyToManyField(Author,
                                     verbose_name='List of authors',
                                     default=None)
    context_text = models.CharField('Context', max_length=500, default="None")
    pub_date = models.DateTimeField('date published')

    # like/hate votes
    auth_likes = models.ManyToManyField(User,
                                        verbose_name='List of the users that \
                                        liked this quote',
                                        related_name='%(class)s_authors_like',
                                        default=None)
    auth_hates = models.ManyToManyField(User,
                                        verbose_name='List of the users that \
                                        disliked this quote',
                                        related_name='%(class)s_authors_hate',
                                        default=None)

    # The quote has to validated by an admin
    validated = models.BooleanField('validated', default=False)
    def __str__(self):
        return self.quote_text
