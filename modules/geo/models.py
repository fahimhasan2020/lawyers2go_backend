from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, db_column='name')
    code = models.CharField(max_length=50, db_column='code')
    latitude = models.FloatField(null=True, blank=True, db_column='latitude')
    longitude = models.FloatField(null=True, blank=True, db_column='longitude')
    is_active = models.BooleanField(default=True, db_column='isActive')
    is_deleted = models.BooleanField(default=False, db_column='isDeleted')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'countries'
        managed = True


class State(models.Model):
    name = models.CharField(max_length=255, unique=True, db_column='name')
    code = models.CharField(max_length=50, null=True, blank=True, db_column='code')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='countryId')
    is_active = models.BooleanField(default=True, db_column='isActive')
    is_deleted = models.BooleanField(default=False, db_column='isDeleted')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'states'
        managed = True


class County(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='countryId')
    state = models.ForeignKey(State, on_delete=models.CASCADE, db_column='stateId')
    is_active = models.BooleanField(default=True, db_column='isActive')
    is_deleted = models.BooleanField(default=False, db_column='isDeleted')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'counties'
        managed = True


class City(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='countryId')
    state = models.ForeignKey(State, on_delete=models.CASCADE, db_column='stateId')
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, blank=True, db_column='countyId')
    zip_code = models.CharField(max_length=20, null=True, blank=True, db_column='zipCode')
    is_active = models.BooleanField(default=True, db_column='isActive')
    is_deleted = models.BooleanField(default=False, db_column='isDeleted')
    created_at = models.DateTimeField(auto_now_add=True, db_column='createdAt')
    updated_at = models.DateTimeField(auto_now=True, db_column='updatedAt')

    class Meta:
        db_table = 'cities'
        managed = True
