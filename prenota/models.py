from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Prenotazione(models.Model):
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "Prenotazione di :" + self.user.username

class Piatti(models.Model):
    CHOICES = (
        ('antipasti', 'antipasti'),
        ('primi', 'primi piatti'),
        ('secondi', 'secondi piatti'),
        ('dessert', 'dessert'),

    )
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    category = models.CharField(max_length=32,choices=CHOICES,default='antipasti',)

    def __str__(self):
        return self.name

class Ordini(models.Model):
    piatto = models.ForeignKey(Piatti, on_delete=models.CASCADE, blank=True, null=True)
    prenota = models.ForeignKey(Prenotazione, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.user.username
