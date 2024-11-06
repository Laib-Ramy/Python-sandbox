from django.contrib import admin
from coop.models import Tool

class ToolAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tool, ToolAdmin)
