from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_text = models.CharField('Author', max_length=300)
    def __str__(self):
        return self.author_text

class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    quote_text = models.CharField('Quote', max_length=1000)
    authors = models.ManyToManyField(Author, verbose_name='List of authors')
    context_text = models.CharField('Context', max_length=500, default="None")
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.quote_text
