from django.contrib import admin
from django.contrib.auth.models import User

from .models import Cart,Order
# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)

class PersonAdmin(admin.ModelAdmin):
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        url ='templates/admin/person/?pks=' + ','.join(str([q.pk for q in queryset]))
       
    actions = [generatePDF]