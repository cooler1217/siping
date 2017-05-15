// 如果想要使一个元素运动起来，一般情况下这个元素须要具有position属性absolute/relative
function timeline(){
}
function product_center(){
	//产品中信
	//$('.header-con ul li a').hover(function(){
	//		$(this).addClass('current');
	// } ,function(){
	//		$(this).removeClass('current');
	//});
	//调整我们的产品 鼠标hover效果
	 $('.product-cell').hover(function(){
			$(this).addClass('colored');
			$(this).siblings().removeClass('colored');
	 }, function() {
			$(this).removeClass('colored');
	});   	 
	
}




var switchTime;
function change(cur){
		 var tNum=$(".banner .banner-con .banner-item").length-1;
	
 		$(".banner-con .banner-item:eq("+cur+")").css({"display": 'block'})
	   											.siblings().css({"display": 'none'});
		//底部nav切换
		$('.banner .rolling-nav a:eq('+cur+')').addClass('active')
												.siblings().removeClass('active');
        if ((adnext = cur+1) > tNum) adnext = 0;
        switchTime=setTimeout("change("+adnext+")", 2000);
}
		
function bannerScroll(){
	switchTime = setTimeout("change(1)", 2000);
	$('.banner .rolling-nav a').click(function(){
			//$(this).addClass('active').siblings().removeClass('active');
			clearTimeout(switchTime);
			var cur = parseInt($(this).attr("data-id"));
			change(cur);
	});
} 


$(function(){ 
	/*1.banner转得动*/
	bannerScroll();
	/*2.新闻区点击tab做切换*/
	
	$(".news-con .tab-nav li").click(function(){
		var _index = $(this).index();
        $(".news-con .tab-nav li").eq(_index).addClass("current").siblings().removeClass('current');
		$(".news-con .tab-conts .tab-item").hide().eq($(this).index()).show();
	});
	
	
	$(".video .tab-nav li").click(function(){
		var _index = $(this).index();
        $(".video .tab-nav li").eq(_index).addClass("current").siblings().removeClass('current');
		$(".video .tab-conts .tab-item").hide().eq($(this).index()).show();
	});
	
	$(".presenter .tab-nav li").click(function(){
		var _index = $(this).index();
        $(".presenter .tab-nav li").eq(_index).addClass("current").siblings().removeClass('current');
		$(".presenter .tab-conts .tab-item").hide().eq($(this).index()).show();
	});
});
