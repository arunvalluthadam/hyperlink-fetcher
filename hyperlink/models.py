from django.db import models

# Create your models here.
class HyperlinkField(models.Model):
	address = models.CharField(max_length=500)
	hylink = models.TextField()

	def __unicode__(self):
		return self.address