from django.db import models


class Order(models.Model):
    case_id = models.IntegerField(db_column='caseId')
    quote_id = models.IntegerField(db_column='quoteId')
    quote_amount = models.FloatField(null=True, blank=True, db_column='quoteAmount')
    service_fee = models.FloatField(null=True, blank=True, db_column='serviceFee')
    total_price = models.FloatField(null=True, blank=True, db_column='totalPrice')
    status = models.CharField(max_length=20, default='ongoing', db_column='status')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'orders'
        managed = True
