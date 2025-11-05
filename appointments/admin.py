from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # list_display = ('patient', 'user', 'date', 'created_at')
    # list_filter = ('date', 'user')
    # search_fields = ('patient__user__name', 'user__name')
    # date_hierarchy = 'date'
    # ordering = ('-date',)

    fieldsets = (
        (None, {
            'fields': ('user', 'patient', 'date')
        }),
        ('Detalhes Adicionais', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
