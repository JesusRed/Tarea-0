from django.contrib import admin
from .models import Pqrs

# Register your models here.
class PqrAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('title',)

admin.site.register(Pqrs)