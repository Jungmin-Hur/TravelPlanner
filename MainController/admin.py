from django.contrib import admin
from MainController.models import Mcontroller, PriceInfo

# Register your models here.
#class MainControllerAdmin(admin.ModelAdmin):
#    list_display = ('title', 'author', 'created',)

#class PriceInfoAdmin(admin.ModelAdmin):
#    list_display = ('price_info_id','email','price_sum','flight_url','hotel_url','flight_price','hotel_price','flight_data','hotel_data',)

#admin.site.register(Mcontroller, MainControllerAdmin)

admin.site.register(PriceInfo)
