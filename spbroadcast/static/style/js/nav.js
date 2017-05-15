// 如果想要使一个元素运动起来，一般情况下这个元素须要具有position属性absolute/relative
$(function(){ 
   
	 
$(".logodiv ul .navitem").hover(function(){ //mouse enter
		//console.log("logodiv ul hover");
			$(".logodiv ul li").removeClass('select');
		 	$(this).addClass('select');
			var index = $(".logodiv ul li").index(this);
			var _o = index+1;
			  $("#con_nav_"+_o).css('display','block').siblings('div').css('display','none');
			
				//$(".banner-con .banner_item:eq("+nNum+")").fadeOut();
		},function(){
				  var index = $(".logodiv ul li").index(this);
				  var _o = index+1;
			//  $("#con_nav_"+_o).css('display','none');
		});
		   	
		   	
	$(".logodiv div.nav").hover(function(){
	},function(){
		$(this).css('display','none');
	});	   	
		
});

 