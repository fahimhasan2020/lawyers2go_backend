from django.db import models


class Payment(models.Model):
    user_id = models.IntegerField(db_column='userId')
    stripe_customer_id = models.CharField(max_length=255, null=True, blank=True, db_column='stripeCustomerId')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'payments'
        managed = True
