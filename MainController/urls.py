from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from MainController import views

urlpatterns = [
    # url(r'^priceinfo/$', views.priceinfo_list),
    # url(r'^priceinfo/(?P<pk>[0-9]+)/$', views.priceinfo_detail),
    url(r'^price/info/$', views.set_price_info),
    # url(r'^price/flightinfo/n/$', views.get_flight_price_info),
    # url(r'^price/hotelinfo/n/$', views.get_hotel_price_info),
    url(r'^price/info/msg/$', views.search_lowest_price),
    url(r'^price/info/remove/$', views.remove_price_info),

    #url(r'^$', views.mcontroller_list),
    #url(r'^(?P<pk>[0-9]+)/$', views.mcontroller_detail),
    #url(r'^user/$', views.user_list),  #user list
    #url(r'^user/(?P<userId>[0-9]+)/$', views.user_detail),

    #url(r'^user/activate/(?P<userId>[0-9]+)/$', views.activate_user),
    #url(r'^user/deactivate/(?P<userId>[0-9]+)/$', views.deactivate_user),
    #url(r'^trip/$', views.get_trip_plan_all), #계획조회(userId없음)
    #url(r'^tripplan/(?P<userId>[0-9]+)/(?P<start_trip_date>[0-9]+)/(?P<end_trip_date>[0-9]+)/$', views.get_trip_plan), #계획조회(userId있음)
]

urlpatterns = format_suffix_patterns(urlpatterns)
