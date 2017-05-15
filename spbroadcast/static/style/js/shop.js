//var g_URL = "http://localhost/web"; //"http://192.168.1.212/123boxcom"; ////
var g_URL = "http://www.123box.com"; 

//var g_URL = "http:"+window.location.hostname; 
//var g_URL ="http://192.168.1.36/123box";


function modifyNum(){
	 $.post(g_URL+'/front/user_purchase/getShopCartNum', {}, function(res){
	 				  var obj =  eval('('+res+')');
	 				 // console.log(obj);
				       $('#shopcartNum').text(obj['num']);
				       $('#shopcartPrice').text(obj['price']);
				       
				           
	});
} 


$(function(){ 
	    modifyNum(); 
	 
		$('.child').hover(function() {
			$(this).addClass('childHover').children('i').addClass('showAddCart');
		}, function() {
			$(this).removeClass('childHover') .children('i').removeClass('showAddCart');
		});
	 
			//弹窗口
			var popWindow = $('.popWindow'); //var popWindow = $('.pop_up'); //	
		   var oClose = $('.popWindow .close');
		   var browserWidth = $(window).width();
			//浏览器可视区域的高度
			var browserHeight = $(window).height();
			//浏览器纵向滚动条距离上边界的值
			var browserScrollTop = $(window).scrollTop();
			//浏览器横向滚动条距离左边界的值
			var browserScrollLeft = $(window).scrollLeft();
			//弹出窗口的宽度
			var popWindowWidth = popWindow.outerWidth(true);
			//弹出窗口的高度
			var popWindowHeight = popWindow.outerHeight(true);
			//left的值＝浏览器可视区域的宽度／2－弹出窗口的宽度／2+浏览器横向滚动条距离左边界的值
			var positionLeft = browserWidth/2 - popWindowWidth/2 +browserScrollLeft;
			//top的值＝浏览器可视区域的高度／2－弹出窗口的高度／2+浏览器纵向滚动条距离上边界的值
			var positionTop = browserHeight/2 - popWindowHeight/2 +browserScrollTop;
			
			var oMask = '<div class="mask"></div>';
			//遮照层的宽度
			//var maskWidth = $(document).width();//遮照层的高度
			var maskWidth = $(window).width();
			var maskHeight = $(document).height();
			
	
	$('.popWindow .close').click(function(){
		popWindow.hide(); $('.mask').remove();
	});
	
	$('.popWindow .pay_way .popfont').hover(function() {
		$(this).addClass('popFontHover');
	}, function() {
		$(this).removeClass('popFontHover');
	}); 
	
	var  g_curImgTargetElement = {};
 
	function popWindowMove(){
			var browserWidth = $(window).width();
			var browserHeight = $(window).height();
			var browserScrollTop = $(window).scrollTop();
			var browserScrollLeft = $(window).scrollLeft();
			var popWindowWidth = popWindow.outerWidth(true);
			var popWindowHeight = popWindow.outerHeight(true);
			var positionLeft = browserWidth/2 - popWindowWidth/2 +browserScrollLeft;
			var positionTop = browserHeight/2 - popWindowHeight/2 +browserScrollTop;
			
			var oMask = '<div class="mask"></div>';
			//遮照层的宽度
			//var maskWidth = $(document).width();//遮照层的高度
			var maskWidth = $(window).width();
			var maskHeight = $(document).height();
			popWindow.show().animate({
						'left':positionLeft+'px',
						'top':positionTop+'px'
			},100).dequeue();
	}
	
	$(window).scroll(function(){
		if(popWindow.is(':visible')){
			browserScrollTop = $(window).scrollTop();
			browserScrollLeft = $(window).scrollLeft();
			positionLeft = browserWidth/2 - popWindowWidth/2+browserScrollLeft;
			positionTop = browserHeight/2 - popWindowHeight/2+browserScrollTop;
			popWindow.animate({
						'left':positionLeft+'px',
						'top':positionTop+'px'
			},100).dequeue();
		}
	});
	
	 var id_val ,
	 	year_val,
	 	price_3mon,
	 	price_mon,
	 	product_name;
	 	
	  
		 
	 	
	$('.child').click(function() {
				
		if($(this).hasClass('SOFT')){
				
			  id_val = $(this).children('.id').eq(0).val();
		      year_val = $(this).children('.price_year').eq(0).val();
		  	  product_name   =  $(this).children('.name').eq(0).val();
		  	  
			  var CopyDiv = '<img src="'+g_URL+'/style/pro_img/soft_logo.png" id="cloneBoxSoft" style="width:81px; height:81px;position: absolute;top:' + $(this).offset().top + 'px;left:' + $(this).offset().left + 'px" />';
					
	 		    var data = {'id':''+id_val, 'y_m_t':'y', 'price':''+year_val, 'num':''+1, 'name':''+ product_name, 'product_type':'SOFT' };
				$.post(g_URL+'/front/user_purchase/addCartProduct', data, function(res){
					//  alert('SOFT添加购物车回值：'+res);
				      modifyNum();
				       $("body").append(CopyDiv); 
					 $("body").children("#cloneBoxSoft").animate(
					 	 {"width":'50px', "height":'50px',"top": $(".shopbody").offset().top, "left": $(".shopbody").offset().left, "opacity": .1 }, 
					 	 900,
					 	 function(){$(this).remove()}
					 );
				 }); 
			return ;
		} else { 
			 //获取当前值进行传参 post 
		    // 弹出框效果后延
	      id_val = $(this).children('.id').eq(0).val();
	      year_val = $(this).children('.price_year').eq(0).val();
		  price_3mon = $(this).children('.price_3mon').eq(0).val();
		  price_mon = $(this).children('.price_mon').eq(0).val();
	  	  product_name   =  $(this).children('.name').eq(0).val();
	 
		   g_curImgTargetElement = $(this).children('img');
		
			popWindowMove();
			$('body').append(oMask);
			$('.mask').width(maskWidth).height(maskHeight);
			
			return false;
		}
		
	});
	
	 
	$('.popWindow .pay_way .popfont').click(function() {
			  var buy_way = $(this).children('input').eq(0).val();
			  var y_m_t = buy_way;
			  var price_val = 0;
			  if(y_m_t=='m'){
			  	price_val = price_mon;
			  }else if(y_m_t=='3m'){
			  	price_val = price_3mon;
			  }else {
			  	price_val = year_val;
			  }
			  
			  
			  var data = {'id':''+id_val+'_'+buy_way, 'y_m_t':''+y_m_t, 'price':''+price_val, 'num':''+1, 'name':''+ product_name }; //alert('准备发送添加的数据 price:'+data.price+'id:'+data.id);
			  
			  $.post(g_URL+'/front/user_purchase/addCartProduct', data, function(res){
					  //alert('添加购物车回值：'+res); //  alert('添加购物车成功');
				 	 modifyNum(); 
				 	 popWindow.hide();
					 $('.mask').remove(); //关闭
					 
					 //飞入效果
					 var srcImg = $(g_curImgTargetElement).attr("src"); 	//alert(srcImg);
					if(typeof(srcImg)=="undefined") {
						//alert('没有图片标签');
					}else{
  					 var CopyDiv = '<img src="'+srcImg+'" id="cloneBox" style=" width:81px; height:81px;position: absolute;top:' + $(g_curImgTargetElement).offset().top + 'px;left:' + $(g_curImgTargetElement).offset().left + 'px" />';
					 $("body").append(CopyDiv); 
					 $("body").children("#cloneBox").animate(
					  	{"width":'50px', "height":'50px', "top": $(".shopbody").offset().top, "left": $(".shopbody").offset().left, "opacity": .1 }, 
					    900,
					   function(){$(this).remove()}
					  );	
					}
					  
					 
			  });
			 return false;
	});
		 
	
	

});


