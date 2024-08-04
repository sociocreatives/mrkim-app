from django.db import models
from accounts.models import User
from datetime import time, date, timedelta
# Create your models here.


class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)  # Default to today's date
    end_date = models.DateField(default=date.today() + timedelta(days=7))  # Default to 7 days later
    start_time = models.TimeField(default=time(9, 0))  # Default start time at 9:00 AM
    end_time = models.TimeField(default=time(17, 0))   # Default end time at 5:00 PM
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Availability Calendar"
    
    def __str__(self):
        return (f"{self.user.username} - {self.start_date} to {self.end_date} "
                f"{self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')} - "
                f"{'Available' if self.available else 'Unavailable'}")