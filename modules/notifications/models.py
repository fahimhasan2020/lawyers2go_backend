from django.db import models


class Notification(models.Model):
    user_id = models.IntegerField(db_column='userId')
    title = models.CharField(max_length=255, null=True, blank=True, db_column='title')
    body = models.TextField(null=True, blank=True, db_column='body')
    is_read = models.BooleanField(default=False, db_column='isRead')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'notifications'
        managed = True
