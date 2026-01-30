from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, db_column='name')
    email = models.EmailField(null=True, blank=True, db_column='email')
    subject = models.CharField(max_length=255, null=True, blank=True, db_column='subject')
    message = models.TextField(null=True, blank=True, db_column='message')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'contacts'
        managed = True
