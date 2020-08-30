from django.db import models

# Create your models here.
class dummy(models.Model):
	dummy_stuff = models.CharField(max_length=10,verbose_name='dummy')


	class Meta:
		db_table = '临时DB'

	def __str__(self):
		return self.dummy_stuff