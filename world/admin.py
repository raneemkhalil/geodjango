# Register your models here.

from django.contrib.gis import admin
from .models import WorldBorder, WorldBorderJson, LeakHotspot, Point

admin.site.register(WorldBorder, admin.ModelAdmin)
admin.site.register(WorldBorderJson, admin.ModelAdmin)
admin.site.register(LeakHotspot, admin.ModelAdmin)
admin.site.register(Point, admin.ModelAdmin)

