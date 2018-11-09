from django.conf.urls import url, include
from django.contrib import admin

from app import views

urlpatterns = [
    url(r"^home/",views.home,name="home"),
    url(r"^market/",views.market,name="market" ),
    url(r"^exit/", views.exit, name="exit"),
    url(r"^marketwithParam/(\d+)/(\d+)/(\d+)", views.marketwithParam, name="marketwithParam"),
    url(r"^cart/",views.cart,name="cart" ),
    url(r"^mine/", views.mine, name="mine"),
    url(r"^CheckUserUnique/", views.CheckUserUnique, name="CheckUserUnique"),
    url(r"^register/", views.register, name="register"),
    url(r"^login/", views.login, name="login"),
    url(r"^check/", views.check, name="check"),
url(r"^getprice/", views.getprice, name="getprice"),
url(r"^getprice2/", views.getprice2, name="getprice2"),


    url(r"^addToCart/", views.addToCart, name="addToCart"),
    url(r"^subToCart/", views.subToCart, name="subToCart"),
    url(r"^addCartNum/", views.addCartNum, name="addCartNum"),
    url(r"^subCartNum/", views.subCartNum, name="subCartNum"),
    url(r"^changeSelectStatu/", views.changeSelectStatu, name="changeSelectStatu"),
    url(r"^changeManySelectStatu/", views.changeManySelectStatu, name="changeManySelectStatu"),
]