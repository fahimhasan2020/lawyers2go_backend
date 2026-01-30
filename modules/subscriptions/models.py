from django.db import models


class Plan(models.Model):
    city_id = models.IntegerField(null=True, blank=True, db_column='cityId')
    name = models.CharField(max_length=255, null=True, blank=True, db_column='name')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'plans'
        managed = True


class SubscriptionTier(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    is_active = models.BooleanField(default=True, db_column='isActive')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'subscription_tiers'
        managed = True


class Package(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    is_active = models.BooleanField(default=True, db_column='isActive')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'packages'
        managed = True


class Coupon(models.Model):
    code = models.CharField(max_length=100, db_column='code')
    discount = models.FloatField(null=True, blank=True, db_column='discount')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'coupons'
        managed = True
