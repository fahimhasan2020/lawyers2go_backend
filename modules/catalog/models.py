from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, db_column='name')
    image = models.CharField(max_length=500, null=True, blank=True, db_column='image')
    is_active = models.BooleanField(default=True, db_column='isActive')
    is_deleted = models.BooleanField(default=False, db_column='isDeleted')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'categories'
        managed = True
