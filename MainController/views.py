from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from MainController.models import Mcontroller, User, TripPlan, TripPlanDetail, PricePlan, PricePlanDetail, PriceInfo
from MainController.serializers import MainControllerSerializer, UserSerializer, TripPlanSerializer, TripPlanDetailSerializer, PricePlanSerializer, PricePlanDetailSerializer, PriceInfoSerializer
from MainController.TripService import TripService

# Create your views here.
@api_view(['POST'])
def set_price_info(request, format=None):
    regs_id = request.data['regs_id']
    type = request.data['type']
    # headers = request.data['headers']
    querystring = request.data['querystring']
    return Response(TripService.set_price_info(regs_id, type, querystring))

@api_view(['POST'])
def get_flight_price_info(request, format=None):
    price_info_id = request.data['price_info_id']
    page_no = request.data['page_no'] #1페이지당 15개씩 조회처리
    return Response(TripService.get_flight_price_info(price_info_id, page_no))

@api_view(['POST'])
def get_hotel_price_info(request, format=None):
    price_info_id = request.data['price_info_id']
    page_no = request.data['page_no'] #1페이지당 15개씩 조회처리
    return Response(TripService.get_hotel_price_info(price_info_id, page_no))

@api_view(['GET'])
def search_lowest_price(request, format=None):
    return Response(TripService.search_lowest_price())

# 요청 url 인 MainController/ 에 대해서 urls.py 에 정의된 view.MainController_list 가 호출된다.
@api_view(['GET', 'POST'])
def mcontroller_list(request, format=None):
    if request.method == 'GET':
        mcontroller = Mcontroller.objects.all()
        serializer = MainControllerSerializer(mcontroller, many=True) # many 값이 True 이면 다수의 데이터 instance를 직렬화할수 있다
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MainControllerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 요청 url 인 MainController/번호 에 대해서 urls.py 에 정의된 view.MainController_detail 이 호출된다
@api_view(['GET', 'PUT', 'DELETE'])
def mcontroller_detail(request, pk, format=None):
    try:
        mcontroller = Mcontroller.objects.get(pk=pk)
    except Mcontroller.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MainControllerSerializer(mcontroller)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MainControllerSerializer(mcontroller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mcontroller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, userId, format=None):
    try:
        #user = User.objects.get(userId=pk)
        user = User.objects.get(userId=userId)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def get_trip_plan_all(request, format=None):
    #request.... start_trip_date, end_trip_date, start
    #request.... tripplandetail -> list로 보내줘야 함.
    print(request)

    startTripDate = request.data['startTripDate']
    endTripDate = request.data['endTripDate']
    origin = request.data['origin']
    destination = request.data['destination']
    tripPlanDetails = TripPlanDetailSerializer(request.data['tripPlanDetails'], many = True)

    #POST
    #if request.method != 'POST':
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #return Response(request.data)
    return Response(TripService.old_get_trip_plan(startTripDate, endTripDate, origin, destination, tripPlanDetails))
    #return Response(TripService.get_trip_plan(start_trip_date, end_trip_date, request))


@api_view(['GET', 'POST'])
def priceinfo_list(request, format=None):
    if request.method == 'GET':
        priceinfo = PriceInfo.objects.all()
        serializer = PriceInfoSerializer(priceinfo, many=True) # many 값이 True 이면 다수의 데이터 instance를 직렬화할수 있다
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PriceInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def priceinfo_detail(request, pk, format=None):
    try:
        priceinfo = PriceInfo.objects.get(pk=pk)
    except PriceInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PriceInfoSerializer(priceinfo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PriceInfoSerializer(priceinfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        priceinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

