from django.db import models
from account.models import User

# Create your models here.

AVAILABILITY = [
    ('Available', 'Available'),
    ('Given', 'Given'),

]


class Stock(models.Model):
    CATEGORY = [
        ('Computer Laptop', 'Computer Laptop'),
        ('Computer Desktop', 'Computer Desktop'),
        ('4G Router', '4G Router'),
        ('Printer', 'Printer'),
        ('Scanner', 'Scanner'),
        ('Television', 'Television'),
        ('Decoder', 'Decoder'),

    ]

    name = models.CharField(max_length=200, null=True)
    serialNumber = models.CharField(max_length=200, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    code = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    availability = models.CharField(max_length=20, choices=AVAILABILITY, default='Available')

    def __str__(self):
        return self.serialNumber


class Item(models.Model):
    STATUS = [
        ('Work', 'Work'),
        ('Not Work', 'Not Work'),
        ('Submitted', 'Submitted'),

    ]

    device = models.OneToOneField(Stock, max_length=200, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='work')
    description = models.TextField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    person = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, max_length=200, null=True, on_delete=models.SET_NULL)
    counting = models.CharField(max_length=20, choices=AVAILABILITY, default='Given')
    # counting = models.ForeignKey(Stock, max_length=20, default='Given', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.device.name
