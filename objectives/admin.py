from django.contrib import admin
from .models import Objective
# Register your models here.
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'completed', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('completed', 'created_at')

admin.site.register(Objective, ObjectiveAdmin)