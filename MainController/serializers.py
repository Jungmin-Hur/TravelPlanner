from rest_framework import serializers
from MainController.models import Mcontroller, User, PricePlan, PricePlanDetail, TripPlan, TripPlanDetail, FlightInfo, HotelInfo, PriceInfo

class MainControllerSerializer(serializers.ModelSerializer):
    # ModelSerializer 를 이용해서 아래와 같이 짧은 코드로 직렬화 필드를 정의할 수 있다
    class Meta:
        model = Mcontroller
        fields = ('id','title','author','pw','content')

    # 신규  instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Mcontroller.objects.create(**validated_data)

    # 생성되어 있는  instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.pw = validated_data.get('pw', instance.pw)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

class PriceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceInfo
        fields = ('price_info_id','regs_id','type','headers','querystring','price')

    def create(self, validated_data):
        return PriceInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.price_info_id = validated_data.get('price_info_id', instance.price_info_id)
        instance.regs_id = validated_data.get('regs_id', instance.regs_id)
        instance.type = validated_data.get('type', instance.type)
        instance.headers = validated_data.get('headers', instance.headers)
        instance.querystring = validated_data.get('querystring', instance.querystring)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId','email','userName')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.email = validated_data.get('email', instance.email)
        instance.userName = validated_data.get('userName', instance.userName)
        instance.save()
        return instance

class PricePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePlan
        fields = ('tripPlanId','active','lowestPrice')

    def create(self, validated_data):
        return PricePlan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tripPlanId = validated_data.get('tripPlanId', instance.tripPlanId)
        instance.active = validated_data.get('active', instance.active)
        instance.lowestPrice = validated_data.get('lowestPrice', instance.lowestPrice)
        instance.save()
        return instance

class PricePlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePlanDetail
        fields = ('pricePlanId','seqNo','flightPrice','hotelPrice')

    def create(self, validated_data):
        return PricePlanDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pricePlanId = validated_data.get('pricePlanId', instance.pricePlanId)
        instance.seqNo = validated_data.get('seqNo', instance.seqNo)
        instance.fightInfoId = validated_data.get('fightInfoId', instance.fightInfoId)
        instance.hotelInfoId = validated_data.get('hotelInfoId', instance.hotelInfoId)
        instance.save()
        return instance

class TripPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPlan
        fields = ('tripPlanId','userId','pricePlanId','startTripDate','endTripDate','origin','destination')

    def create(self, validated_data):
        return TripPlan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tripPlanId = validated_data.get('tripPlanId', instance.tripPlanId)
        instance.userId = validated_data.get('userId', instance.userId)
        instance.pricePlanId = validated_data.get('pricePlanId', instance.pricePlanId)
        instance.startTripDate = validated_data.get('startTripDate', instance.startTripDate)
        instance.endTripDate = validated_data.get('endTripDate', instance.endTripDate)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.save()
        return instance

class TripPlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPlanDetail
        fields = ('tripPlanId','gps','locationName','tripDate')

    def create(self, validated_data):
        return TripPlanDetail.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tripPlanId = validated_data.get('tripPlanId', instance.tripPlanId)
        instance.gps = validated_data.get('gps', instance.gps)
        instance.locationName = validated_data.get('locationName', instance.locationName)
        instance.tripDate = validated_data.get('tripDate', instance.tripDate)
        instance.save()
        return instance

class FlightInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightInfo
        fields = ('flightInfoId','outboundOrigin','outboundDestination','outboundDepartureDate','inboundOrigin','inboundDestination','inboundDepartureDate','price')

    def create(self, validated_data):
        return FlightInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.flightInfoId = validated_data.get('flightInfoId', instance.flightInfoId)
        instance.outboundOrigin = validated_data.get('outboundOrigin', instance.outboundOrigin)
        instance.outboundDestination = validated_data.get('outboundDestination', instance.outboundDestination)
        instance.outboundDepartureDate = validated_data.get('outboundDepartureDate', instance.outboundDepartureDate)
        instance.inboundOrigin = validated_data.get('inboundOrigin', instance.inboundOrigin)
        instance.inboundDestination = validated_data.get('inboundDestination', instance.inboundDestination)
        instance.inboundDepartureDate = validated_data.get('inboundDepartureDate', instance.inboundDepartureDate)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class HotelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelInfo
        fields = ('hotelInfoId','destination','destinationDate','hotelName','hotelGrade','price')

    def create(self, validated_data):
        return HotelInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.hotelInfoId = validated_data.get('hotelInfoId', instance.hotelInfoId)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.destinationDate = validated_data.get('destinationDate', instance.destinationDate)
        instance.hotelName = validated_data.get('hotelName', instance.hotelName)
        instance.hotelGrade = validated_data.get('hotelGrade', instance.hotelGrade)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
