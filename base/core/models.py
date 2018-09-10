from django.db import models

# Create your models here.
class Human(models.Model):
	name = models.CharField('Name', max_length=60)
	lightning = models.BooleanField('Available', default=True)
	current = models.BooleanField('Current', default=False)
	is_active = models.BooleanField('Active', default=True)

	class Meta:
		verbose_name = u'Human'
		verbose_name_plural = 'Humans'

	def __str__(self):
		return self.name

class Talks(models.Model):
	human = models.ForeignKey('Human')
	name = models.CharField(max_length=200)
	link = models.URLField()
	cicle = models.IntegerField('Cicle')
	date = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = u'Talk'
		verbose_name_plural = 'Talks'

	def __str__(self):
		return self.name