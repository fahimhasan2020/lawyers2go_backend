from django.db import models


class Settings(models.Model):
    key = models.CharField(max_length=255, db_column='key')
    value = models.TextField(null=True, blank=True, db_column='value')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'settings'
        managed = True
        verbose_name_plural = 'Settings'
