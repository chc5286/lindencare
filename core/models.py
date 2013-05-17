from django.db import models

class Person(models.Model):
    first_name = models.CharField("First Name",max_length=30)
    last_name = models.CharField("Last Name",max_length=30)

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name #getting error when trying to do return self.full_name

    class Meta:
        abstract = True


class Contact(Person):
    email = models.EmailField(blank=True)
    is_inactive = models.BooleanField("Inactive?")
    comment = models.CharField(max_length=255,blank=True)

    class Meta:
        abstract = True

		
class Address(models.Model):
    address = models.CharField(max_length=50,blank=True)
    address2 = models.CharField("address",max_length=50,blank=True)
    city = models.CharField(max_length=30,blank=True)
    state = models.CharField(max_length=2,blank=True)
    zipCode = models.CharField(max_length=5,blank=True)

    class Meta:
        abstract = True
