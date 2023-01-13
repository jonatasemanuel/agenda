from django.contrib import admin
from .models import Contact, Status


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'phone', 'email',
                    'creation_date', 'status', 'show')
    list_display_links = ('id', 'name', 'last_name')
    list_per_page = 10
    search_fields = ('name', 'last_name', 'phone', 'email')
    # list_filter = ('name', 'last_name')
    list_editable = ('phone', 'show')


admin.site.register(Status)
admin.site.register(Contact, ContactAdmin)
