from django.db import models
from django.contrib.auth.models import User

#Model for Orders
class Order(models.Model):
    SUPPER_PLACES = [
        ('Mac','MacDonalds'),
        ('KFC','Kentucky'),
        ('BK', 'Burger King')
    ]

    supper_places = models.CharField(max_length = 3, choices = SUPPER_PLACES)
    food = models.CharField(max_length = 50)
    #one to many relationship: 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.author.username
