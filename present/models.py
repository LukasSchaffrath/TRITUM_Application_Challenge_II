from django.db import models


class  data(models.Model):

		distance_travelled = models.DecimalField(max_digits=4, decimal_places=2)
		time = models.IntegerField()
		kcal_burned = models.IntegerField()
		avg_heart_beat = models.IntegerField()
		def __str__(self):
			return self.distance_travelled