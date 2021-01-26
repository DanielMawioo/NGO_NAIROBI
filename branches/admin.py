from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Main_Office, Issues_Addressed, Regional_Office, Field_Offices

@admin.register(Main_Office)
class Main_OfficeAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


admin.site.register(Issues_Addressed)


@admin.register(Regional_Office)
class Regional_OfficeAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


@admin.register(Field_Offices)
class Field_OfficesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')