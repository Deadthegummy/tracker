from django.db import models


# Create your models here.
class Event(models.Model):
    date = models.DateTimeField('date published')
    exercise_type = models.ForeignKey('Exercise', on_delete=models.PROTECT)

    def format_data(self):
        return {'date': self.date.isoformat(), 'exercisetype': self.exercise_type.type, 'id': self.pk}


class Exercise(models.Model):
    type = models.CharField(max_length=25)


class Attribute(models.Model):
    type = models.ForeignKey('AttributeType', on_delete=models.PROTECT)
    value = models.CharField(max_length=255)
    event = models.ForeignKey('Event', on_delete=models.PROTECT)


class AttributeType(models.Model):
    unit = models.CharField(max_length=12)
    name = models.CharField(max_length=25)