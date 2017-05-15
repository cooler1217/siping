// 按钮点击
$(function(){ 
		var wrapBox = $('#presenter-list');
		var oul = $('#presenter-list ul');
		var ali = $('#presenter-list ul li');
		var aliSize = ali.size();
		var spacing = 6; 
		var allNode = [];
		var ulWidth = 0;
		var t1, t2;
		if (aliSize > 0) {
			$.each(ali, function(index, data){ 
				var aliWidth = $(data).outerWidth();
				console.info(index+" "+data +":"+aliWidth);
				if (index === aliSize - 1) {
					allNode.push(aliWidth);
					ulWidth += aliWidth;
				} else {
					allNode.push(aliWidth+spacing);
					ulWidth += (aliWidth + spacing);
				}
			});
			console.info("total: "+ulWidth);
			console.info(allNode);
			oul.width(ulWidth);	//1600px
			
			// 默认left不可用 
			if(oul.width() < wrapBox.width() ) {
				$('#goRight').removeClass('hidden').addClass('hidden');
				$('#goLeft').removeClass('hidden').addClass('hidden');
			}
		}

		function allowLeft() {
			var left = oul.position().left;
			if(left >= 0) {
				console.log('no allow left move ');
				return false;
			}
			return true;
		}
		function leftMoveOp() {
			console.log('leftmoveOp --------');
			var left = oul.position().left; // left的宽度
			var remainWidth = Math.abs(left);
			console.log(remainWidth);
			var remainNodeNum = 0,
				remainNodeWidthTmp = 0,
				remainNodeWidth = 0,
				remainNode = [];
			for (var i = 0; i<= allNode.length-1; i++) {
				remainNodeWidthTmp += allNode[i];
				if (remainWidth >= remainNodeWidthTmp) {
					remainNodeWidth += allNode[i];
					remainNode.push(allNode[i]);
					remainNodeNum++;
				}
			}
			// 根据剩余节点个数进行移动，如果剩0个 直接left置顶， 如果剩余1个或者1个半直接left置顶；如果剩余两个置顶导数第二个
			if (remainNodeNum ==0 || remainNodeNum ==1) {
				//直接置顶left
				oul.css('left', '+='+remainWidth+'px');
				console.log('left move result1: '+remainWidth);
			} else if (remainNodeNum >= 2) {
				var spacing = remainWidth - remainNodeWidth;
				console.log('left remainWidth:'+remainWidth);
				console.log('left remainNodeWidth:'+remainNodeWidth);
				var nodeWidth = remainNode.pop(); //取一个
				var result = spacing + nodeWidth;
				oul.css('left', '+='+result+'px');
				console.log('left move result2: '+result+' spacing:'+spacing+" nodewidth:"+nodeWidth);
			}
		}
		
		$('#goLeft').mousedown(function(){
			if (allowLeft()) {
				t1 = window.setInterval(function(){
					if (allowLeft()) {	
						leftMoveOp();					
					}
				},100);
			}
		});
		$('#goLeft').mouseup(function(){
			window.clearInterval(t1); 
		});
		function allowRight() {
			var left = oul.position().left;
			var result = left + oul.width();
			if (result <= wrapBox.width()) {
				console.log(' no allow right');
				return false;
			}
			return true;
		}
		
		function rightMoveOp() {
			var left = oul.position().left;
			var remainWidth = oul.width() + left - wrapBox.width();
			// 倒序计算剩余宽度中包含的剩余条件个数，如果小于1个，则全部移动；如果1个则全部移动，如果小于两个则全部移动；
			// 如果等于两个 则移动一个，如果等于三个，则移动一个
			var remainNodeNum = 0,
				remainNodeWidthTmp = 0,
				remainNodeWidth = 0,
				remainNode = [];
			for (var i= allNode.length-1; i>=0; --i) {
				remainNodeWidthTmp += allNode[i];
				if (remainWidth >= remainNodeWidthTmp) {
					remainNodeWidth += allNode[i];
					remainNode.push(allNode[i]);
					remainNodeNum++;
				}
			}
			// 根据剩余节点个数进行移动，如果剩0个 直接left置顶， 如果剩余1个或者1个半直接left置顶；如果剩余两个置顶导数第二个
			if (remainNodeNum ==0 || remainNodeNum ==1) {
				//直接置顶left
				oul.css('left', '-='+remainWidth+'px');
				console.log('move result1: '+remainWidth);
			} else if (remainNodeNum >= 2) {
				var spacing = remainWidth - remainNodeWidth;
				var nodeWidth = remainNode.shift(); //取一个
				var result = spacing + nodeWidth;
				oul.css('left', '-='+result+'px');
				console.log('move result2: '+result+' spacing:'+spacing+" nodewidth:"+nodeWidth);
			}
		}
		
		$('#goRight').mousedown(function(){
			if (allowRight()) {
				t2 = window.setInterval(function(){
					if (allowRight()) {
						// 计算宽度
						rightMoveOp();
						//oul.css('left', '-='+spacing+'px');
					}
				},100);	
			}
		});
		$('#goRight').mouseup(function(){
			window.clearInterval(t2); 
		});
		
});
 
 