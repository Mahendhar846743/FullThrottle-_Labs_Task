from django.core.management.base import BaseCommand
from task.models import *


class Command(BaseCommand):
    help = 'create users'
    def handle(self, *args, **kwargs):
        User.objects.create(id=1,real_name='mahendhar',tz='Asia/Kolkata')
        User.objects.create(id=2, real_name='Rakesh', tz='America/Los_Angeles')
        activity_periods.objects.create(user_id=1,start_time='2020-03-28 04:34:00.000000-08:00',end_time='2020-03-28 04:40:00.000000-08:00')
        activity_periods.objects.create(user_id=1, start_time='2020-03-28 04:45:00.000000-08:00',end_time='2020-03-28 04:50:00.000000-08:00')
        activity_periods.objects.create(user_id=1, start_time='2020-03-28 05:00:00.000000-08:00',end_time='2020-03-28 05:10:00.000000-08:00')
        activity_periods.objects.create(user_id=2, start_time='2020-03-28 04:20:00.000000-08:00',end_time='2020-03-28 04:28:00.000000-08:00')
        activity_periods.objects.create(user_id=2, start_time='2020-03-28 06:34:00.000000-08:00',end_time='2020-03-28 06:40:00.000000-08:00')
        activity_periods.objects.create(user_id=2, start_time='2020-03-28 07:34:00.000000-08:00',end_time='2020-03-28 07:40:00.000000-08:00')

        return "Successfully users are created"