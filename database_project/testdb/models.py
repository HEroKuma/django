from django.db import models

# Create your models here.

class testList(models.Model):
	name = models.CharField(max_length = 20)
	description = models.CharField(max_length = 200)

	permissions = (
            ("can_watch", "Can watch"),
        )

	def __unicode__(self):
		return self.name

class testForeign(models.Model):
	name = models.CharField(max_length = 20)
	text = models.CharField(max_length = 200, default = 'foreign')
	ref_list = models.ForeignKey(testList)

	def __unicode__(self):
		return self.name