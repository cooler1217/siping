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
	$(".titles .tabs li").click(function(){
        $(".tabs li").eq($(this).index()).addClass("current").siblings().removeClass('current');
		$(".main .tab-content").hide().eq($(this).index()).show();
	});
	
});
 
 