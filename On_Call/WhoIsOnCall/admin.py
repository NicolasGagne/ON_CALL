from django.contrib import admin
from .models import Organisation


class OrganisationAdmin(admin.ModelAdmin):  # add this
    list_display = ('name', 'description', 'private')  # add this


# Register your models here.
admin.site.register(Organisation, OrganisationAdmin)  # add this