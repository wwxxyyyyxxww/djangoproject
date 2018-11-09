// $(function () {
//     //    点击 + 按钮,将购物车中商品数量加1
//
//     $(".addCart").click(function () {
//         $this = $(this)
//         cartid = $this.parents("li").attr("cartid")
//         // alert(cartid)
//         addUrl = "/axf/addCart";
//
//
//         //    ajax请求
//         $.getJSON(addUrl, {"cartid": cartid}, function (data) {
//             if (data["code"] == 200) {
//                 // alert(data["num"])
//                 //    修改数量
//                 $this.prev("span").html(data["num"])
//             }
//         })
//     })
//
//
//     //    点击 + 按钮,将购物车中商品数量加1
//
//     $(".subCart").click(function () {
//         $this = $(this)
//
//         cartid = $this.parents("li").attr("cartid")
//         // alert(cartid)
//
//         addUrl = "/axf/subCart";
//
//
//         //    ajax请求
//         $.getJSON(addUrl, {"cartid": cartid}, function (data) {
//             if (data["code"] == 200) {
//                 // alert(data["num"])
//                 //    修改数量
//                 $this.next("span").html(data["num"])
//             }
//             else if (data["code"] == 300) { //移除该整个商品记录
//                 $this.parents("li").remove()
//
//             }
//         })
//     })
//
//
//     //勾选按钮的点击事件
//     $(".selectButton").click(function () {
//         $this = $(this)
//         cartid = $this.parents("li").attr("cartid")
//
//         urlPath = "/axf/chanageSelect"
//         $.getJSON(urlPath, {"cartid": cartid}, function (data) {
//             if (data["code"] == 200) {//修改状态成功
//                 // alert(data["isselect"])
//                 if (data["isselect"]) { //选中
//                     $this.html("<span>√</span>")
//                     $this.attr("isselect", "True")
//
//                 } else {  //不选中
//                     $this.html("<span></span>")
//                     $this.attr("isselect", "False")
//                 }
//
//                 //   是否全选
//                 if (data["isAllSelect"]) {
//                     $("#allSelectButton").html("<span>√</span>")
//                 } else {
//                     $("#allSelectButton").html("<span></span>")
//                 }
//
//             }
//         })
//     })
//
//
//     //给全选按钮设置点击事件
//     $("#allSelectButton").click(function () {
//         /*
//         * 1.加上勾  只要有一个商品没有被选中, 点击全选按钮, 全选按钮应该变成  选中 按钮, 所有的商品应该变成选中状态
//         *
//         * 2.去掉勾   当所有商品都被选中的时候,点击全选按钮,全选按钮应该变成  未选中  状态,所有的商品应该变成未选中状态
//         * */
//
//
//         // 获取到所有商品的选中状态---解决: 前端,服务器
//         //   未选中的
//         var noSelectList = [];
//         //所有选中的
//         var selectList = [];
//
//         $(".selectButton").each(function () { //遍历每一个selectbutton
//             //获得选中状态
//             isselect = $(this).attr("isselect")
//             //获得当前的cartid
//             cartid = $(this).parents("li").attr("cartid")
//             console.log(isselect)
//             if (String(isselect) == "True") {//选中  python中 True,False    js中 false,true
//                 selectList.push(cartid)
//             } else {
//                 noSelectList.push(cartid)
//             }
//         })
//         //     测试:
//
//         console.log(noSelectList)
//         console.log(selectList)
//
//         if (noSelectList.length == 0 && selectList.length >= 1) {//全部选中---条件2---全选按钮应该变成  未选中  状态,所有的商品应该变成  未选中  状态
//             urlPath = "/axf/changeManySelect"
//             console.log(selectList)
//             $.getJSON(urlPath, {"cartidList": selectList.join("#"), "flag": 2}, function (data) {
//                 if (data["code"] == 200) {//状态修改成功
//                     //    将所有的商品变为选中效果
//                     $(".selectButton").each(function () {
//                         $(this).html("<span></span>")
//                         $(this).attr("isselect", "False")
//                     })
//                     $("#allSelectButton").html("<span></span>")
//                 }
//             })
//
//         } else { //存在没有被选中的  条件1 ---- 选按钮应该变成  选中 按钮, 所有的商品应该变成选中状态
//
//             urlPath = "/axf/changeManySelect"
//             //将未选中的变成选中的
//             console.log(noSelectList)
//             $.getJSON(urlPath, {"cartidList": noSelectList.join("#"), "flag": 1}, function (data) {
//                 if (data["code"] == 200) {//状态修改成功
//                     //    将所有的商品变为选中效果
//                     $(".selectButton").each(function () {
//                         $(this).html("<span>√</span>")
//                         $(this).attr("isselect", "True")
//                     })
//                     $("#allSelectButton").html("<span>√</span>")
//                 }
//             })
//
//
//         }
//     })
//
//
// //  点击选好了按钮,生成一个订单
//     $("#greate_order").click(function () {
//         //    获取所有的选中的 cartid 购物车记录
//         var selectList = [];
//         $(".selectButton").each(function () {
//             isselect = $(this).attr("isselect")
//             cartid = $(this).parents("li").attr("cartid")
//             if (String(isselect) == "True") {//选中的
//                 selectList.push(cartid)
//             }
//         })
//
//         if (selectList.length == 0) {//没有选中
//             alert("没选中任何商品")
//         } else {
//             // console.log(selectList)
//             // 发送给服务器,让服务器生成订单
//             urlPath = "/axf/createOrder"
//             $.getJSON(urlPath, {"selectList": selectList.join("#")}, function (data) {
//                 if(data["code"] == 200){
//                     orderNumber  = data["orderNumber"]
//
//                 //    订单创建成功--调到订单页面
//                     window.open("/axf/orderInfo/" + orderNumber ,target="_self")
//
//                 }
//             })
//         }
//
//
//     })
//
// })
//


// $.getJSON("/app/add",{"a":1},function (data) {
// console.log(data)
// })

$(function () {
    //    点击商品的 + 按钮,将该商品购物车数量 +1
    $(".add_cart_num_button").click(function () {

        $this =  $(this)
        //获得购物车id 即cartid
        cartid = $this.parents("li").attr("cartid")

        var urlPath = '/app/addCartNum'
        var paramData =  {'cartid':cartid}

    //    请求服务器,
        $.getJSON(urlPath,paramData,function (data) {
            if (data['code'] == 200){
                // alert(data['num'])
            //    变数字
                $this.prev("span").html(data['num'])
            }
        })
    })


     //    点击商品的 - 按钮,将该商品购物车数量 -1
    //  如果数量为0,需要删除该条记录
    $(".sub_cart_num_button").click(function () {

        $this =  $(this)
        //获得购物车id 即cartid
        cartid = $this.parents("li").attr("cartid")

        var urlPath = '/app/subCartNum'
        var paramData =  {'cartid':cartid}

    //    请求服务器,
        $.getJSON(urlPath,paramData,function (data) {
            if (data['code'] == 200){
                // alert(data['num'])
            //    变数字
                $this.next("span").html(data['num'])
            }else if(data['code'] == 201){ //表示减为0,应该删除该条记录li
                $this.parents("li").remove()
            }
        })
    })



    //给每个 选中 按钮设置点击事件,
    //    点击后改变选中状态
    $(".select_button").click(function () {



       var  $this = $(this)
       var cartid = $this.parents("li").attr("cartid");

        urlpath = "/app/changeSelectStatu"
        dataParam = {'cartid':cartid}









    //    修改服务器的选中状态
        $.getJSON(urlpath,dataParam,function (data) {

            if (data['code'] == 200){//请求成功
                if(data["isselect"]){ //选中 --- 加上 勾
                    $this.html("<span>√</span>")
                    //修改属性的状态
                    $this.attr("isselect","True")
                }else{ //未选中 ---去掉勾
                    $this.html("<span></span>")
                    //修改属性的状态
                    $this.attr("isselect","False")
                }
                // console.log(data["select"])
                if(data["select"]=="not"){
                    console.log("not")


                    $("#all_select_button").html("<span></span>")
                }
                else if(data["select"]=="true") {
                    console.log("yes")

                    $("#all_select_button").html("<span>√</span>")
                }
            }

        })
    })


//    全选按钮
    /*
      服务器,前端
    * 1.勾选全选按钮 ---- 只要有一个购物车记录没有被选中,则勾选上全选按钮, 同时所有的购物车记录都因该变成选中
    * 2.去掉全选按钮的勾----只有所有购物车记录都是选中状态时才会显示勾,此时点击全选按钮可以去掉全选前的勾, 同时所有的购物车记录都因该变成 未选中状态
    * */

    $("#all_select_button").click(function () {

    //    数组记录所有选中的cart记录
        var allSelectArray = []
        //数组记录所有没有选中的cart记录
        var noSelectArray = []


    //    获取每一条cart记录的选中状态
        $('.select_button').each(function () {
            // $(this) 当前遍历的一个对象
           var $this = $(this);
           var isselect = $this.attr("isselect");
            //获得cartid
           var  cartid = $this.parents("li").attr("cartid");

            if(String(isselect) == "True"){ //选中
                allSelectArray.push(cartid)
            }else{ //未选中
                noSelectArray.push(cartid)
            }
        })

        console.log(allSelectArray)
        console.log(noSelectArray)

    //    判断当前是否是全选
       if(noSelectArray.length==0 && allSelectArray.length >=1){
            //当前是所有的购物车记录都是选中状态,
           //--应该将全选按钮的勾去掉,同事每条购物车记录的勾都得去掉
            //请求服务器修改
           //全选---全部不选中
           urlpath = '/app/changeManySelectStatu'
           dataParam = {"selectArray":allSelectArray.join("#"),"flag":1}
           $.getJSON(urlpath,dataParam,function (data) {
                if(data['code'] = 200){
                    $(".select_button").each(function () {
                        $(this).html("<span></span>")
                        $(this).attr("isselect","False")
                    })

                    $("#all_select_button").html("<span></span>")

                }
           })



       }else{
            //当前购物车中不是全部都是选中状态
           //---应该将全选按钮的勾加上,同事每条购物车记录的勾都得加上
           urlpath = '/app/changeManySelectStatu'
           dataParam = {"selectArray":noSelectArray.join("#"),'flag':2}
           $.getJSON(urlpath,dataParam,function (data) {
                  if(data['code'] = 200){
                    $(".select_button").each(function () {
                        $(this).html("<span>√</span>")
                        $(this).attr("isselect","True")
                    })

                      $("#all_select_button").html("<span>√</span>")
                }
           })

       }



    })


})




 // $(".select_button").click(function () {
 //     url="/app/check"
 //     data=
 // $.getJSON()
 // })
 //

// $(function(){
//      list=[]
//     $(".select_button").each(function () {
//
//
//         if($(this).attr("isselect")=="True") {
//             param = $(this).parents("li").attr("cartid")
//             list.push(param)
//         }
//             url="/app/getprice"
//             data={"param":list.join("#")}
//
//             $.getJSON(url,data,function (data) {
//                 $("#greate_order").prev("p").children().eq(2).html(data["sum"])
//                 }
//             )
//
//     })
// })
//
// $(".select_button").click(function(){
//     id=$(this).parents("li").attr("cartid")
//     price= $("#greate_order").prev("p").children().eq(2).html()
//
//     url="/app/getprice2"
//     data={"id":id,"price":price}
//     $.getJSON(url,data,function (data) {
//    $("#greate_order").prev("p").children().eq(2).html(data["sum"])
//     })
//
// })


$(function(){
    $(".select_button") .each(function () {
        
    })
})
