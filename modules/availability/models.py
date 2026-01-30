from django.db import models


class Availability(models.Model):
    provider_id = models.IntegerField(db_column='providerId')
    day_of_week = models.IntegerField(null=True, blank=True, db_column='dayOfWeek')
    start_time = models.TimeField(null=True, blank=True, db_column='startTime')
    end_time = models.TimeField(null=True, blank=True, db_column='endTime')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'availabilities'
        managed = True
