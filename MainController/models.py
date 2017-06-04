from django.db import models

# Create your models here.
class PriceInfo(models.Model):

    price_info_id = models.CharField(max_length=100)
    regs_id = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=10, default='')
    headers = models.CharField(max_length=2000, blank=True, default='')
    querystring = models.CharField(max_length=2000, default='')
    price = models.BigIntegerField(default=0)
    # {
    #     "regs_id": "4292a5e6-66f",
    #     "type": "(F/H)"
    #             "headers": "user-agent=''",
    # "querysting": "http://"
    # }
    # regs_id =

    class Meta:
        db_table = 'PRICE_INFO'

class Mcontroller(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=20, blank=True, default='')
    pw = models.CharField(max_length=12, blank=True, default='')
    content = models.TextField()
    class Meta:
        ordering = ('created',)

class User(models.Model):
    userId = models.CharField(max_length=30)
    email = models.CharField(max_length=100, blank=True, default='')
    userName = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        db_table = 'USER'

class PricePlan(models.Model):
    tripPlanId = models.CharField(max_length=30)
    active = models.BooleanField()
    lowestPrice = models.BigIntegerField()
    class Meta:
        db_table = 'PRICE_PLAN'

class PricePlanDetail(models.Model):
    pricePlanId = models.CharField(max_length=30)
    seqNo = models.BigIntegerField()
    flightInfoId = models.CharField(max_length=100)
    hotelInfoId = models.CharField(max_length=100)
    class Meta:
        db_table = 'PRICE_PLAN_DETAIL'

class TripPlan(models.Model):
    tripPlanId = models.CharField(max_length=30)
    userId = models.CharField(max_length=30)
    pricePlanId = models.CharField(max_length=30)
    startTripDate = models.DateTimeField()
    endTripDate = models.DateTimeField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    class Meta:
        db_table = 'TRIP_PLAN'

class TripPlanDetail(models.Model):
    tripPlanId = models.CharField(max_length=30, blank=True, default='')
    gps = models.CharField(max_length=50, blank=True, default='')
    locationName = models.CharField(max_length=100)
    tripDate = models.DateTimeField()
    class Meta:
        db_table = 'TRIP_PLAN_DETAIL'

class FlightInfo(models.Model):
    flightInfoId = models.CharField(max_length=30)
    outboundOrigin = models.CharField(max_length=100)
    outboundDestination = models.CharField(max_length=100)
    outboundDepartureDate = models.DateTimeField()
    inboundOrigin = models.CharField(max_length=100)
    inboundDestination = models.CharField(max_length=100)
    inboundDepartureDate = models.DateTimeField()
    price = models.BigIntegerField()
    class Meta:
        db_table = 'FLIGHT_INFO'

class HotelInfo(models.Model):
    hotelInfoId = models.CharField(max_length=30)
    destination = models.CharField(max_length=100)
    destinationDate = models.DateTimeField()
    hotelName = models.CharField(max_length=100)
    hotelGrade = models.CharField(max_length=100)
    price = models.BigIntegerField()
    class Meta:
        db_table = 'HOTEL_INFO'
