import hashlib

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import Wheel, Nav, Mustbuy, shop, mainshow, foodtype, Goods, UserModel, CartModel


# from axfhz1805.app.models import Wheel, Nav, Mustbuy


def home(request):
    wheels=Wheel.objects.all()
    nav=Nav.objects.all()
    mustbuy=Mustbuy.objects.all()
    shops=shop.objects.all()
    main=mainshow.objects.all()

    shop1=shops[0]
    shop2_3=shops[1:3]
    shop4_7=shops[3:7]
    shop8_ = shops[7:]

    data={"title":"主页",
          "all":wheels,
          "navs":nav,
          "mustbuy":mustbuy,
          "shop1":shop1,
          "shop2_3":shop2_3,
          "shop4_7":shop4_7,
          "shop8":shop8_,
          "main":main
          }
    return render(request, "home/home.html",context=data)



def market(request):
    # 查询所有的商品类型信息
    # foodtypes = FoodType.objects.all().order_by("typesort")
    # # 查询所有的商品数据
    # goodses =  goods.objects.all()
    #
    # data = {
    #     "title": "闪购",
    #     'foodtypes':foodtypes,
    #     'goodses':goodses,
    # }
    #
    # return  render(request,'market/market.html',context=data)
    # 默认104749表示显示热销榜   0 默认是全部分类    0默认是综合排序
    return  redirect(reverse('app:marketwithParam',args=(104749,0,0)))




def marketwithParam(request,typeid,childid,sortType):
    # 查询所有的商品类型信息
    foodtypes = foodtype.objects.all().order_by("typesort")

    # 查询所有的商品数据
    # 根据商品类型来查询数据
    goodses = Goods.objects.filter(categoryid=typeid)

    if not str(childid) == "0":  #如果不是全部分类,需要再次筛选
        #再次根据子分类id进行数据筛选
        goodses = goodses.filter(childcid=childid)

    #再已经查询结果集上在 排序
    # 0 综合排序,  1 销量排序(降序)  2价格升序    3价格降序
    if int(sortType) == 0:
        pass
    elif int(sortType) == 1:
       goodses = goodses.order_by("-productnum")
    elif int(sortType) == 2:
       goodses = goodses.order_by("price")
    elif int(sortType) == 3:
       goodses = goodses.order_by("-price")



    # 根据类型查询出所有的子分类信息
    foodType = foodtype.objects.filter(typeid=typeid).first()
    # foodType =FoodType()
    # 全部分类:0#进口水果:103534#国产水果:103533
    childtypenames = foodType.childtypenames.split("#")
    # [全部分类:0,进口水果:103534,国产水果:103533]

    allChild = []
    for child in childtypenames: #全部分类: 0
        allChild.append(child.split(":"))

    print(allChild)


    data = {
        "title": "闪购",
        'foodtypes': foodtypes,
        'goodses': goodses,
        'typeid':str(typeid),
        'allChild':allChild,
        'childid':int(childid),
    }

    return render(request, 'market/market.html', context=data)


def cart(request):
    userid = request.session.get("user_id")
    if userid:  # 登录
        user = UserModel.objects.filter(pk=userid).first()
    else:  # 未登录
        return redirect(reverse('app:login'))

    # 根据用户查询该用户所有的cart记录
    carts = CartModel.objects.filter(c_user=user)
    isAllSelect = True
    for cart in carts:
        # 只要cart中有一条是记录没有被选中,则全选一定是false
        if not cart.c_isselect: #没有被选中的
             isAllSelect = False
             break

    data = {
        "title": "购物车",
        'carts':carts,
        'isAllSelect':isAllSelect,
    }

    return  render(request,'cart/cart.html',context=data)
def mine(request):
    userid=request.session.get("user_id")
    if userid:
        user=UserModel.objects.filter(pk=userid).first()
        # user=UserModel()
        username=user.u_name
        img=user.u_img
        print(img)
        data = {"title": "我的",
                "user":user,

                "username":username,
                "imgpath":'/static/upload/'+img.url
                }
    else:
         data = {"title": "我的",
            }

    return render(request,"mine/mine.html",context=data)

def register(request):
    method=request.method
    if method=="GET":
        return render(request, "user/user_register.html")
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        img=request.FILES.get("imgFile")
        user=UserModel()
        user.u_img=img
        user.u_mail=email
        user.u_name=username
        # m=hashlib.md5()
        # m.update(password.encode(encoding='utf-8'))
        # password2= m.hexdigest()
        user.u_pass=password
        user.save()
        return redirect(reverse("app:login"))
def login(request):
    if request.method=="GET":
        return render(request,"user/user_login.html")
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(password)
        user=UserModel.objects.filter(u_name=username).first()
        if user:
            if user.u_pass==password:
                #保留登陆成功的状态
                request.session["user_id"] = user.id
                return redirect(reverse("app:mine"))

        else:
            return  HttpResponse("用户名或者密码输入不正确!")

        # print(user.u_pass)
        # n = hashlib.md5()
        # n.update(password.encode(encoding='utf-8'))
        # password2 = n.hexdigest()




def CheckUserUnique(request):
    username=request.GET.get("username")
    user=UserModel.objects.filter(u_name=username).first()
    if user:
        code=200
        message="用户名存在"
    else:
        code=404
        message="用户名合法"
    data={
        "username":username,
        "code":code,
        "message":message
    }
    print(username)
    return JsonResponse(data)
def exit(request):
    request.session.flush()
    return redirect(reverse("app:login"))
# def addgoods(request):
#
#     userid = request.session.get("user_id")
#     if userid:
#         user=UserModel.objects.filter(pk=userid).first()
#         id=request.GET.get("id")
#
#     # username=UserModel.objects.filter(pk=userid)
#         food=Goods.objects.filter(pk=id).first()
#         print("Dddddddddddddddddddddddddddddddddddddddddddd")
#         print(food)
#         find=CartModel.objects.filter(c_goods_id=food.id)
#         if find:
#             print("Y")
#             return HttpResponse("y")
#         else:
#             cart=CartModel()
#             cart.c_goods_id=food.id
#             cart.c_user_id=userid
#             cart.c_num=1
#             cart.c_isselect=True
#             print(food.id,userid,cart.c_num,cart.c_isselect)
#             cart.save()
#             obj =Goods.objects.filter(pk=food.id).first()
#             img=obj.productimg
#
#             data={
#             "code":200,
#             "img":img
#
#                 }
#     else:
#         data={
#             "code":304,
#             "message":"没有登录,需要登录!"
#         }
#         print(data)
#
#
#     return JsonResponse(data)


def addToCart(request):
#     目的: 网购物车中添加一条记录
#       1.用户
#         1.获取当前登录信息
#            1.登录了
#                1.获得登录的用户user
#            2.没有登录了
#               1.跳到登录页
#
#       2.商品
#         获得商品的id,并找到对应的商品对象
#       3.数量
#         0.根据用户,商品查询对应的记录
#         1.购物车中没有该记录
#            1.创建一条新的购物车记录,且数量为1
#         2.购物车中有该记录
#            1.在原有的记录上加1
#       4.是否选中-- 默认的

    userid = request.session.get("user_id")
    data = {}
    if userid:#登录
        user = UserModel.objects.filter(pk=userid).first()
    else: #未登录
        print("------------")
        # 在ajax请求中,不能进行重定向
        # return redirect(reverse('axf:login'))
    #   可以让js进行重定向
        data["code"] = 304  #需要重定向到登录页
        data["msg"] = "未登录,需要重新登录"
        return JsonResponse(data)

    goodsid = request.GET.get("goodsid")
    mygoods = Goods.objects.filter(pk=goodsid).first()

    # 查询cart记录
    res = CartModel.objects.filter(c_user=user).filter(c_goods=mygoods)
    if res.exists(): #有记录
        cart =  res.first()
        # cart = CartModel()
        cart.c_num += 1
        cart.save()

        data["code"] = 200 #操作成功
        data['msg'] = "添加到购车成功"
        data['num'] = cart.c_num

    else: #没有记录
        cart = CartModel()
        cart.c_user = user
        cart.c_goods = mygoods
        cart.c_num = 1

        cart.save()
        data["code"] = 200  # 操作成功
        data['msg'] = "添加到购车成功"
        data['num'] = 1

    return JsonResponse(data)


# 将购物车中的商品数量-1
def subToCart(request):
    userid = request.session.get("user_id")
    data = {}
    if userid:  # 登录
        user = UserModel.objects.filter(pk=userid).first()
    else:  # 未登录
        print("------------")
        # 在ajax请求中,不能进行重定向
        # return redirect(reverse('axf:login'))
        #   可以让js进行重定向
        data["code"] = 304  # 需要重定向到登录页
        data["msg"] = "未登录,需要重新登录"
        return JsonResponse(data)

    goodsid = request.GET.get("goodsid")
    mygoods = Goods.objects.filter(pk=goodsid).first()
    # 查询cart记录
    res = CartModel.objects.filter(c_user=user).filter(c_goods=mygoods)

#    商品数量
#     1.cart记录不存在
#        直接返回 0
#     2.cart记录存在
#        1.数量等于 1
#            删除该记录,并返回数量0
#        2.数量大于1
#            当前数量 -1, 修改之后,保存
    if res.exists():
        cart = res.first()
        # cart = CartModel()
        num = cart.c_num
        if num == 1:
            cart.delete()
            data['code'] = 200
            data['msg'] = '购物车记录已经删除'
            data['num'] = 0

        elif num > 1:
            cart.c_num -= 1
            cart.save()

            data['code'] = 200
            data['msg'] = '购物车记录已经删除'
            data['num'] = cart.c_num

    else:
        data['code'] = 200
        data['msg'] = '购物车没有该记录'
        data['num'] = 0

    return  JsonResponse(data)


# 修改购物车商品数量  加操作 +1
def addCartNum(request):
#     获取商品id
    cartid = request.GET.get('cartid')
    cart =  CartModel.objects.filter(pk=cartid).first()
    # cart = CartModel()
    cart.c_num += 1
    cart.save()
    data = {}
    data['code'] = 200
    data['msg'] = '数量加操作成功'
    data['num'] = cart.c_num
    return JsonResponse(data)

def subCartNum(request):
    #     获取商品id
    cartid = request.GET.get('cartid')
    cart = CartModel.objects.filter(pk=cartid).first()
    # cart = CartModel()
    num = cart.c_num
    data = {}
    if num == 1: #如果数量减为0了,应该删除该条数据
        cart.delete()
        data['code'] = 201
        data['msg'] = '数量减操作成功'
        data['num'] = 0

    elif num > 1:
        cart.c_num -= 1
        cart.save()
        data['code'] = 200
        data['msg'] = '数量加操作成功'
        data['num'] = cart.c_num

    return  JsonResponse(data)



def changeSelectStatu(request):




#     获取购物车cartid
    cartid = request.GET.get('cartid')
#     根据购物车id查询出cart 购物车记录
    cart = CartModel.objects.filter(pk=cartid).first()
#      修改购物车的状态
#     cart = CartModel()
#       选中---未选中
#      未选中 ---选中
    cart.c_isselect = not cart.c_isselect

    cart.save()

    data = {}

    data["code"] = 200 # 状态修改成功
    data['msg'] = '状态修改成功'
    data['isselect'] = cart.c_isselect


    user = request.session.get("user_id")
    array = CartModel.objects.filter(c_user=user)
    data["select"]="true"
    for i in array:
        print(i.c_isselect)
        if i.c_isselect==False:
            data["select"]="not"
            break
    print(data["select"])
    print("no")

    return  JsonResponse(data)


# changeManySelectStatu  点击全选按钮时修改多条数据的选中状态
def changeManySelectStatu(request):
    # pass
    # 获取到需要改变状态的所有cartid
    # "".split()

        # if i.c_isselect==







    selectList = request.GET.get("selectArray").split("#")
    print(selectList)

    flag = request.GET.get('flag')


    carts  = CartModel.objects.filter(id__in=selectList)
    data = {}
    for cart in carts:

        if flag == "1":#全改为false
            cart.c_isselect = False
            print("------------1")

        elif flag == "2": #全改为true
            cart.c_isselect = True
            print("------------2")

        cart.save()

    data["code"]  = 200

    return  JsonResponse(data)





def check(request):
    user=request.session.get("user_id")
    print(user)
    # array=CartModel()
    array=CartModel.objects.filter(c_user=user)
    print("sssssssss")
    print(array)
    for i in array:
        print(i.c_isselect)

    res=request.GET.get("flag")
    if str(res) =="1":
        data={
            "select":1
        }
    else:
        data={
            "select":2
        }


    #


    return JsonResponse(data)
    # result=CartModel.objects.filter(pk=res).first()

    # print(result)
    # if result:
    #     isselect=result.




def getprice(request):
    return HttpResponse("ffff")
#     param=request.GET.get("param")
#
#     newparam=param.split("#")
#     print("ssssssssss")
#     print(newparam)
#     sum=0
#     for i in newparam:
#         print(i)
#         print(type(i))
#         b=int(i)
#         a=CartModel.objects.filter(id=b).first()
#
#         price = a.c_goods.price
#         sum+=price
#
#     #
#     print(sum)
#     data={"sum":sum}
#
#     return JsonResponse(data)









def getprice2(request):
    param2=request.GET.get("id")
    param3 = request.GET.get("price")
    print(param2)
    a=CartModel.objects.filter(pk=int(param2)).first()
    b=a.c_goods.price



    param4=int(param3)
    param4 += b
    print(param4)

    data={

        "sum":param4
    }
    return  JsonResponse(data)

