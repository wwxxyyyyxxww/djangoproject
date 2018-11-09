from django.db import models

# Create your models here.


# 定义一个父模型
class Home(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=50)

    class Meta:
        abstract = True





# 设置轮播图模型 ---- id,图片地址,描述信息,时间
# insert into axf_wheel(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg","酸奶女王","21870"),("http://img01.bqstatic.com//upload/activity/2017031710450787.jpg@90Q.jpg","优选圣女果","21869"),("http://img01.bqstatic.com//upload/activity/2017030714522982.jpg@90Q.jpg","伊利酸奶大放价","21862"),("http://img01.bqstatic.com//upload/activity/2017032116081698.jpg@90Q.jpg","鲜货直供－窝夫小子","21770"),("http://img01.bqstatic.com//upload/activity/2017032117283348.jpg@90Q.jpg","鲜货直供－狼博森食品","21874");
class Wheel(Home):

    # 改名字
    class Meta:
        db_table = "axf_wheel"



#        nav导航
# insert into axf_nav(img,name,trackid)
# values("http://img01.bqstatic.com//upload/activity/2017032016495169.png","每日必抢","21851"),("http://img01.bqstatic.com//upload/activity/2016121920130294.png","每日签到","21753"),("http://img01.bqstatic.com//upload/activity/2017010517013925.png","鲜货直供","21749"),("http://img01.bqstatic.com//upload/activity/2017031518404137.png","鲜蜂力荐","21854");

class Nav(Home):
    class Meta:
        db_table = "axf_nav"
class Mustbuy(Home):
    class Meta:
        db_table='axf_mustbuy'
class shop(Home):
    class Meta:
        db_table="axf_shop"
class mainshow(models.Model):

    trackid=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    img=models.CharField(max_length=200)
    categoryid=models.CharField(max_length=50)
    brandname=models.CharField(max_length=50)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=50)
    longname1 = models.CharField(max_length=100)
    productid1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=50)
    marketprice1 = models.CharField(max_length=50)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=50)
    productid2 = models.CharField(max_length=50)
    longname2=models.CharField(max_length=100)
    price2 = models.CharField(max_length=50)
    marketprice2 = models.CharField(max_length=50)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=50)
    productid3 = models.CharField(max_length=50)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=50)
    marketprice3 = models.CharField(max_length=50)
    class Meta:
        db_table="axf_mainshow"
        # axf_foodtypes(typeid, typename, childtypenames, typesort)
class foodtype(models.Model):
        typeid = models.CharField(max_length=50)
        typename = models.CharField(max_length=50)
        childtypenames = models.CharField(max_length=200)
        typesort = models.IntegerField(max_length=50)
        class Meta:
            db_table="axf_foodtypes"

class Goods(models.Model):
    productid=models.CharField(max_length=100)
    productimg=models.CharField(max_length=200)
    productname=models.CharField(max_length=50)
    productlongname=models.CharField(max_length=200)
    isxf=models.BooleanField(default=0)
    pmdesc=models.IntegerField(default=0)
    specifics=models.CharField(max_length=50)
    price=models.FloatField(default=0)
    marketprice=models.FloatField(default=0)
    categoryid=models.CharField(max_length=50)
    childcid=models.CharField(max_length=50)
    childcidname=models.CharField(max_length=100)
    dealerid=models.CharField(max_length=50)
    storenums=models.IntegerField(default=0)
    productnum=models.IntegerField(default=0)
    class Meta:
        db_table="axf_goods"
class UserModel(models.Model):
    u_name=models.CharField(max_length=32,unique=True)
    u_sex=models.BooleanField(default=1)
    u_pass=models.CharField(max_length=200)
    u_img=models.ImageField(upload_to="img")
    u_mail=models.CharField(max_length=40,unique=True)
    class Meta:
        db_table="axf_user"
class  CartModel(models.Model):
    c_goods=models.ForeignKey(Goods)
    c_num=models.IntegerField(default=1)
    c_isselect=models.BooleanField(default=1)
    c_user=models.ForeignKey(UserModel)
    class Meta:
        db_table="axf_cart"
class OrderModel(models.Model):
    o_number=models.CharField(max_length=128)
    o_user=models.ForeignKey(UserModel)
    o_status=models.DateField(auto_now=True)
    class Meta:
        db_table="axf_order"
class OrderAndGoods(models.Model):
    o_number=models.ForeignKey(OrderModel)
    o_goods=models.ForeignKey(Goods)
    o_count=models.IntegerField(default=1)
    class Meta:
        db_table="axf_orderandgoods"

















