$(function () {
//    设置默认位隐藏
    $("#type_container").hide()
    $("#allsortrule").hide()

//    给全部类型设置点击事件
    $("#alltypes").click(function () {
        //    显示  子分类
        //    找到 子分类的 div
        $("#type_container").show()
        //    将箭头变成向上
        $("#glyphiconTypes").removeClass().addClass("glyphicon glyphicon-chevron-up")

        //    让 所有排序 隐藏
        $("#allsortrule").hide()
        $("#glyphiconSort").removeClass().addClass("glyphicon glyphicon-chevron-down")

    })


//    点击子分类容器中的的任何一个位置,隐藏该子分类界面
    $("#type_container").click(function () {
        $(this).hide()
        //    将箭头变成向下
        $("#glyphiconTypes").removeClass().addClass("glyphicon glyphicon-chevron-down")
    })

    // 点击显示排序规则
    $("#allsort").click(function () {
        $("#allsortrule").show()
        //   改变箭头方向
        $("#glyphiconSort").removeClass().addClass("glyphicon glyphicon-chevron-up")

        $("#type_container").hide()
        //    将箭头变成向下
        $("#glyphiconTypes").removeClass().addClass("glyphicon glyphicon-chevron-down")


    })

    $("#allsortrule").click(function () {
        $(this).hide()
        $("#glyphiconSort").removeClass().addClass("glyphicon glyphicon-chevron-down")
    })
})











//
// //    点击 + 按钮,将商品加入到购物车
//
//     $(".addToCart").click(function () {
//
//         //获得goodsid (给该button动态添加了 goodsid属性)
//         goodsid = $(this).attr("goodsid")
//
//         addUrl = "/axf/addToCart";
//
//         $this = $(this)
//
//
//     //    ajax请求
//         $.getJSON(addUrl,{"goodsid":goodsid},function (data) {
//             if(data["code"] == 302){//需要重定向登录
//                //打开登录页面
//                 window.open("/axf/login",target="_self")
//             }else if(data["code"] == 200){
//                 // alert(data["num"])
//             //    修改数量
//
//                 $this.prev("span").html(data["num"])
//             }
//         })
//     })
//
// //    点击 - 按钮,将商品的购物车数量减去一个
//     $(".subToCart").click(function () {
//          //获得goodsid (给该button动态添加了 goodsid属性)
//         goodsid = $(this).attr("goodsid")
//
//         addUrl = "/axf/subToCart";
//
//         $this = $(this)
//
//         //    ajax请求
//         $.getJSON(addUrl,{"goodsid":goodsid},function (data) {
//             if(data["code"] == 302){//需要重定向登录
//                //打开登录页面
//                 window.open("/axf/login",target="_self")
//             }else if(data["code"] == 200){
//                 // alert(data["num"])
//             //    修改数量
//                 $this.next("span").html(data["num"])
//             }
//         })
//     })
//
//
//
// })
$(function () {
//    让全部分类默认隐藏
    $("#type_container").hide();
//    让排序的容器隐藏
    $("#sort_container").hide();



//    点击全部分类按钮显示 所有子分类
    $("#alltype_button").click(function () {
        $("#type_container").show();
    //    更改箭头方向
        $("#alltype_arrow").removeClass().addClass("glyphicon glyphicon-chevron-up");

    //   将排序容器隐藏
        $("#sort_container").hide();
        $("#sort_arrow").removeClass().addClass("glyphicon glyphicon-chevron-down");


    })


//    点击 所有子分类 的任意区域,所有子分类隐藏
    $("#type_container").click(function () {
        $(this).hide()
         //    更改箭头方向
        $("#alltype_arrow").removeClass().addClass("glyphicon glyphicon-chevron-down");

    })

//    点击 综合排序 按钮显示 排序的容器
    $("#sort_button").click(function () {
        $("#sort_container").show();
         //    更改箭头方向
        $("#sort_arrow").removeClass().addClass("glyphicon glyphicon-chevron-up");

    //    将分类容器隐藏
        $("#type_container").hide();
        $("#alltype_arrow").removeClass().addClass("glyphicon glyphicon-chevron-down");


    })

//    点击 排序容器的 任意区域, 排序容器隐藏
    $("#sort_container").click(function () {
         $(this).hide()
          //    更改箭头方向
         $("#sort_arrow").removeClass().addClass("glyphicon glyphicon-chevron-down");
    })


})

// $(".addToCart").click(function(){
//
//     a=$(this).siblings().eq(1).text()
//
//     num=parseInt(a)
//     num+=1
//     $(this).siblings().eq(1).text(num)
//     good=$(this).attr("goodsid")
//
//     // $id=$(this)[0].attributes[0]
//     // console.log(good)
//     if (num>0){
//         $.getJSON('/app/add',{'id':good},function(data) {
//         if(data['code']==304){
//             //调到登录页面
//             console.log(data)
//             window.open('/app/login',target='_self')
//
//         }
//         })
//     }
//
//
//
//
// })
//
// $(".subToCart").click(function(){
//     a=$(this).siblings().eq(0).text()
//     if(a>0){
//         num-=1
//         a=$(this).siblings().eq(0).text(num)
//         console.log(num)
//     }
// }
//
//
//
// )
$(".add_to_cart_button").click(function () {

        $this =  $(this)
        //获得商品id
        goodsId = $this.attr("goodsid")

        var urlPath = '/app/addToCart'
        var paramData =  {'goodsid':goodsId}

    //    请求服务器,
        $.getJSON(urlPath,paramData,function (data) {
              // alert("+")
            if(data['code'] == 304){//跳到登录页
                window.open('/app/login',target='_self')
            }else if (data['code'] == 200){
                // alert(data['num'])
            //    变数字
                $this.prev("span").html(data['num'])
            }
        })
    })

    //将购物车中的商品数量-1

    $(".sub_to_cart_button").click(function () {

        $this =  $(this)
        //获得商品id
        goodsId = $this.attr("goodsid")

        var paramData =  {'goodsid':goodsId}
        var  urlPath = '/app/subToCart'

        $.getJSON(urlPath,paramData,function (data) {
                   // alert("+")
            if(data['code'] == 304){//跳到登录页
                window.open('/axf/login',target='_self')
            }else if (data['code'] == 200){
                // alert(data['num'])
            //    变数字
                $this.next("span").html(data['num'])
            }
        })


    })

































