from django.contrib import admin
from formapp.models import FormDetails
# Register your models here.

class FormDetailsAdmin(admin.ModelAdmin):
    '''
        Admin View for FormDetails
    '''
    list_display = ('usn','name','age','stream','section')
    
admin.site.register(FormDetails, FormDetailsAdmin)