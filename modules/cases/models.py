from django.db import models


class Case(models.Model):
    case_owner_id = models.IntegerField(db_column='caseOwnerId')
    case_owner_user_type = models.CharField(max_length=20, null=True, blank=True, db_column='caseOwnerUserType')
    state_id = models.IntegerField(db_column='stateId')
    county_id = models.IntegerField(null=True, blank=True, db_column='countyId')
    city_id = models.IntegerField(null=True, blank=True, db_column='cityId')
    service_type_id = models.IntegerField(db_column='serviceTypeId')
    sub_service_type_id = models.IntegerField(db_column='subServiceTypeId')
    case_description = models.TextField(null=True, blank=True, db_column='caseDescription')
    status = models.CharField(max_length=20, default='init', db_column='status')
    is_active = models.BooleanField(default=True, db_column='isActive')
    is_deleted = models.BooleanField(default=False, db_column='isDeleted')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'cases'
        managed = True


class Quote(models.Model):
    case_id = models.IntegerField(db_column='caseId')
    provider_id = models.IntegerField(null=True, blank=True, db_column='providerId')
    quote_amount = models.FloatField(null=True, blank=True, db_column='quoteAmount')
    status = models.CharField(max_length=20, default='pending', db_column='status')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'quotes'
        managed = True
