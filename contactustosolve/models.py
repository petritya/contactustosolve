from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Office(models.Model):
    officeName = models.CharField("Iroda", max_length=100)
    
    def __str__(self):
        return self.officeName

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)    
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Customer(models.Model):
    customerName = models.CharField("Ügyfél neve", max_length=100)
    customerPhone = models.CharField("Ügyfél telefonszáma", max_length=15)
    customerEmail = models.EmailField("Ügyfél e-mail címe", max_length=50, blank=True, null=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.customerName

class Provider(models.Model):
    providerName = models.CharField("Szolgáltató neve", max_length=100)
    contactName = models.CharField("Kapcsolattartó neve", max_length=100, blank=True)
    city = models.CharField("Város", max_length=100)
    address = models.CharField("Cím", max_length=100)
    phoneNumber = models.CharField("Telefonszám", max_length=15)
    email = models.EmailField("E-mail", blank=True)
    activity = models.TextField()
    night = models.BooleanField()
    rating = models.FloatField(blank=True, null=True)
    monOp = models.TimeField(blank=True, null=True)
    monCl = models.TimeField(blank=True, null=True)
    tueOp = models.TimeField(blank=True, null=True)
    tueCl = models.TimeField(blank=True, null=True)
    wedOp = models.TimeField(blank=True, null=True)
    wedCl = models.TimeField(blank=True, null=True)
    thuOp = models.TimeField(blank=True, null=True)
    thuCl = models.TimeField(blank=True, null=True)
    friOp = models.TimeField(blank=True, null=True)
    friCl = models.TimeField(blank=True, null=True)
    satOp = models.TimeField(blank=True, null=True)
    satCl = models.TimeField(blank=True, null=True)
    sunOp = models.TimeField(blank=True, null=True)
    sunCl = models.TimeField(blank=True, null=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.providerName
    
    def __unicode__(self):
        return self.providerName
    
class Solutions(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    solutionDateTime = models.DateTimeField(auto_now_add=True)
    closingDateTime = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    sendToProvider = models.BooleanField(default=False)