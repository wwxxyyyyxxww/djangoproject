//   function chushihua(){
//    var mySwiper = new Swiper ('.swiper-container', {
//     direction: 'vertical', // 垂直切换选项
//     loop: true, // 循环模式选项
//
//     // 如果需要分页器
//     pagination: {
//       el: '.swiper-pagination',
//     },
//
//     // 如果需要前进后退按钮
//     navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev',
//     },
//
//     // 如果需要滚动条
//     scrollbar: {
//       el: '.swiper-scrollbar',
//     },
//   })
//   }
// $(document).ready(function () {
// chushihua()
// })
$(function () {
//轮播图
    wheelJs()
//  必买商品轮播图驱动


})

//顶部轮播图驱动
function wheelJs() {
 var mySwiper = new Swiper ('#topSwiper', {
    // direction: 'vertical', // 垂直切换选项
    loop: true, // 循环模式选项

    // 如果需要分页器
    pagination: '.swiper-pagination',
    // 如果需要前进后退按钮
    // navigation: {
    //   nextEl: '.swiper-button-next',
    //   prevEl: '.swiper-button-prev',
    // },

    // 如果需要滚动条
    // scrollbar: {
    //   el: '.swiper-scrollbar',
    // },
  })
}