from django.db import models

# Create your models here.

class Pairname(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)

    def __str__(self):
         return self.name

class Currency(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    pairname = models.ManyToManyField(Pairname)

    def __str__(self):
        return self.name

class Exchange(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    currency = models.ManyToManyField(Currency)
    pairname = models.ManyToManyField(Pairname)

    def __str__(self):
        return self.name

class Datablock(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    pairname = models.ManyToManyField(Pairname)
    currency = models.ManyToManyField(Currency)
    exchange = models.ManyToManyField(Exchange)
    bid = models.CharField(max_length=63)
    ask = models.CharField(max_length=63)

    def __str__(self):
         return "{} [{}, {}, {}, {}] in exchange {}".format(
         self.name,
         self.pairname,
         self.currency,
         self.bid,
         self.ask,
         self.exchange
         )
