from django.db import models


class User(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id=models.IntegerField(primary_key=True)
    real_name=models.CharField(max_length=35)
    tz = models.CharField(max_length=32, choices=TIMEZONES,default='UTC')

class activity_periods(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='activity_periods')
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
