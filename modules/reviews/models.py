from django.db import models


class Review(models.Model):
    case_id = models.IntegerField(null=True, blank=True, db_column='caseId')
    provider_id = models.IntegerField(db_column='providerId')
    rating = models.IntegerField(null=True, blank=True, db_column='rating')
    comment = models.TextField(null=True, blank=True, db_column='comment')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'reviews'
        managed = True
