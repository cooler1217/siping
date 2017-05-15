$(function(){ 
	  $('#train').addClass('current');
				 resize_win();
	
	/*导航固定*/
	$(window).scroll(function(){
		//当滚动距离顶部50px时就固定,可自行更改
		if ($(window).scrollTop()>480){
			$("#left-nav").css({'position':'fixed','top':'0', 'margin-left':'auto', 'margin-right':'auto', 'width':'160px'});
		} else 	{//到达顶部时恢复
			$("#left-nav").css({'position':'absolute','top':'0px', 'margin-left':'auto', 'margin-right':'auto', 'width':'160px'});
		}
	});
	
	
	
	
	//自适应窗口拖拽
	$(window).resize(function(){
		resize_win();
	});

   $('#navigation').children('li').eq(0).children('div').eq(0).click();
   
   
   $("#iframe").load(function(){
		var mainheight = $(this).contents().find("body").height()+30;
		$(this).height(mainheight);
	});
		
});
 
 //跳转href
function subgo(){
	$("html,body").animate({scrollTop:$("#right").offset().top},10);
}
			//自动调整left区域和right区域宽高				
   function resize_win(){
				var top_box_H = $('#top_box').height();
				var top_bar_H = $('.top_bar').height();
				var foot_box_H = $('#foot_box').height();
				var DH = $(window).height();
				//左右高度
				$('#left_box').css({'height' : DH - (top_box_H + top_bar_H + foot_box_H) - 10});
			//	$('#right').css({'height' : DH - (top_box_H + top_bar_H + foot_box_H) - 10});
				//右边宽度
				var left_box_W = $('#left_box').width();
				var DW = $(window).width();
				//$('#right').css({'width' : DW - left_box_W - 40});
	}
			
			
 
 