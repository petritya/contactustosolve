from django.contrib import admin

from .models import Office, Customer, Provider, Profile, Solutions

class CustomerAdmin(admin.ModelAdmin):
    list_display=('customerName', 'customerPhone', 'customerEmail',)
    search_fields=['customerName']
    
class ProviderAdmin(admin.ModelAdmin):
    list_display=('providerName', 'contactName', 'city', 'address',)
    search_fields=['providerName']
    
admin.site.register(Office)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Profile)
admin.site.register(Solutions)