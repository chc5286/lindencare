from django.db import models
from practices.models import Practice


class Appointment(models.Model):
	practice = models.ForeignKey(Practice)
	visit_date = models.DateTimeField()
	comment = models.TextField(blank=True)
	is_complete = models.BooleanField()
	#sales_rep = models('salesrep.models.SalesRep')

	

	

	


