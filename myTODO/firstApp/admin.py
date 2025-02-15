from django.contrib import admin
from .models import TODO


@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    list_display = ('title', 'status', 'user', 'date')

