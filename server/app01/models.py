from django.db import models

# Create your models here.


class a(models.Model):
    # name = models.CharField(max_length=32)
    cnt = models.IntegerField(default=1)


class air_set(models.Model):
    mode = models.IntegerField(default=1)
    temp = models.IntegerField(default=25)
    speed = models.IntegerField(default=4)
    if_on = models.IntegerField(default=0)
    pref = models. IntegerField(default=0)
    on_off = models.IntegerField(default=0)


class week_set(models.Model):
    # on_1 = models.TimeField()
    # off_1 = models.TimeField()
    if_on = models.IntegerField(default=0)
    time = models.TimeField()
    day = models.IntegerField()


# class week_time(models.Model):
#     timestart = models.IntegerField(default=0)
#     time_week = models.IntegerField(default=0)
#     if_on = models.IntegerField(default=0)

class week_time(models.Model):
    times_start = models.IntegerField(default=1)
    week_num = models.CharField(max_length=20, default="周一")
    if_on = models.IntegerField(default=0)
    times_start_show = models.CharField(max_length=20, default="00:00")
