from django.db import models
from django.contrib.auth.models import User


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class WinterLevel(models.Model):
    level = models.CharField(max_length=255)


class SpringLevel(models.Model):
    level = models.CharField(max_length=255)


class SummerLevel(models.Model):
    level = models.CharField(max_length=255)


class AutumnLevel(models.Model):
    level = models.CharField(max_length=255)


class PerevalAreas(models.Model):
    areas = models.CharField(max_length=255)


class ActivitiesType(models.Model):
    activity = models.CharField(max_length=255)


class PerevalAdded(models.Model):

    CHOICES =[
        ('new', 'Новая'),
        ('pending', 'В работе'),
        ('accepted', 'Одобрено'),
        ('rejected', 'Отклонено'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    beauty_title = models.CharField(max_length=255,unique=True)
    title = models.CharField(max_length=255)
    other_title = models.CharField(max_length=255)
    connect = models.BooleanField()
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)
    winter_level = models.ForeignKey(WinterLevel, on_delete=models.CASCADE)
    spring_level = models.ForeignKey(SpringLevel, on_delete=models.CASCADE)
    summer_level = models.ForeignKey(SummerLevel, on_delete=models.CASCADE)
    autumn_level = models.ForeignKey(AutumnLevel, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=CHOICES,
                              default='new')
    areas = models.ForeignKey(PerevalAreas, on_delete=models.CASCADE)
    activities_types = models.ManyToManyField(ActivitiesType, through='PerevalActivitiesType')


class PerevalImages(models.Model):
    pereval_id = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField()


class PerevalActivitiesType(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    activities_type = models.ForeignKey(ActivitiesType, on_delete=models.CASCADE)