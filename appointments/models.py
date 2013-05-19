from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from practices.models import Practice


class Appointment(models.Model):
	practice = models.ForeignKey(Practice)
	visit_date = models.DateTimeField()
	comment = models.TextField(blank=True)
	is_complete = models.BooleanField("Completed?")
	sales_rep = models.ForeignKey(User)

	
"""
	def check_visit_date_and_comment(self):
        if not visit_date and comment:
            raise ValidationError('Comment must be null')

    def clean(self):
        check_visit_date_and_comment()
"""

	


