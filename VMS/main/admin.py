from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'status', 'check_in', 'check_out')  # Fields to display in the admin list view
    list_filter = ('status', 'check_in', 'check_out')  # Filters for easy navigation
    search_fields = ('name', 'contact', 'email', 'purpose')  # Searchable fields
    readonly_fields = ('check_in', 'check_out')  # Fields that should not be editable in the admin form

    fieldsets = (
        (None, {
            'fields': ('name', 'contact', 'email', 'address', 'purpose', 'status', 'img')
        }),
        ('Timestamps', {
            'fields': ('check_in', 'check_out'),
        }),
    )
