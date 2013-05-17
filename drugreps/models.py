from django.db import models
from core.models import Contact


class DrugCompany(models.Model):
	name = models.CharField(max_length=200,unique=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Drug Companies" 


class Drug(models.Model):
	name = models.CharField(max_length=200,unique=True)
	is_brand = models.BooleanField()

	def __unicode__(self):
		return self.name


class DrugNDC(models.Model):
	opus_key = models.IntegerField(unique=True)
	drug = models.ForeignKey(Drug,null=True,blank=True)
	ndc = models.CharField(max_length=50,unique=True)
	strength = models.IntegerField(null=True)
	strength_units = models.CharField(max_length=100,null=True)

	def __unicode__(self):
		return self.drug + ' ' + self.strength + ' ' + self.strength_units

	class Meta:
		verbose_name_plural = "Drug NDC" 


class Division(models.Model):
	name = models.CharField(max_length=200)
	drug = models.ManyToManyField(Drug)
	company = models.ForeignKey(DrugCompany)

	def __unicode__(self):
		return self.name


class Manager(Contact):
	division = models.ForeignKey(Division)
	territory = models.CharField(max_length=100,blank=True)


class DrugRep(Contact):
	manager = models.ForeignKey(Manager)
	regions = models.CharField(max_length=255,blank=True)

	class Meta:
		verbose_name_plural = "Drug Reps" 
