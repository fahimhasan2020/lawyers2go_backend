from django.apps import AppConfig


class GeoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.geo'
    label = 'geo'
    verbose_name = 'Geo (Country, State, County, City)'
