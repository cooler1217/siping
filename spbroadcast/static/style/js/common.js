function filterSqlStr(value){  
    var sqlStr=sql_str().split(',');  
    var flag=false;  
    for(var i=0;i<sqlStr.length;i++){  
        if(value.toLowerCase().indexOf(sqlStr[i])!=-1){  
            flag=true;  
            break;  
        }  
    }  
    return flag;  
}  
  
function sql_str(){  
    var str="and,delete,or,exec,insert,select,union,update,count,*,',join,>,<";  
    return str;  
}

/**重置查询form*/
function resetSearchForm() {
	var searchForm = searchDlgObj.find('form')[0];
	if (typeof searchForm != 'undefined') {
		searchForm.reset();	
	}
}

$(function(){
	$('.clearSearchCondition').click(function(){
		var form = $(this).parent().parent('form')[0];
		if (typeof form != 'undefined') {
			form.reset();
		}
	});
});

function gbqSelectInit(moveDlgObj) {
	//根据属性获取被选中的下拉项
	function getSelectedItem($uldom, value) {
			var itemList = $uldom.find("li");
			for (var i = 0; i < itemList.length; i++) {
				if (itemList[i].getAttribute("catalogid") == value){
					return itemList[i];
				}
			}
			return undefined;
	}

	//定义点击和mouseover 
	moveDlgObj.find(".GCCPSelect").on("click",function(){
		if ($(this).find("ul").css("display") == "none"){
			$(this).find("ul").css("display","block");
			$(this).removeClass("GCCPSelect_norm").addClass("GCCPSelect_click");

			// 初始化上次选中的ltem
			/*var selectedItem = getSelectedItem($(this).find("ul"), $(this).find("span").attr("catalogid"));
			if (selectedItem != undefined){
				$(selectedItem).addClass("itemSelected");
				$(selectedItem).removeClass("itemNotSelected");
			}*/
		} else {
			$(this).find("ul").css("display","none");
			$(this).removeClass("GCCPSelect_click").addClass("GCCPSelect_norm");
		}
	}).mouseleave(function () {
	 $(this).find("ul").css("display","none");
	});

	//移动时兄弟节点不能为选中状态（主要目的是去掉初始选中的item样式）
	moveDlgObj.find(".GCCPSelect ul").on("mouseover","li",function () {
		$(this).siblings().addClass("itemNotSelected");
		$(this).siblings().removeClass("itemSelected");
	}).on("click","li",function(){
		$(this).parents(".GCCPSelect").find("span").attr("catalogid",$(this).attr("catalogid"));
		$(this).parents(".GCCPSelect").find("span").attr("catalogid_guid",$(this).attr("catalogid_guid"));
		$(this).parents(".GCCPSelect").find("span").text(this.innerText);
	});
}


/*获取目标CatalogId*/
function setMoveTargetCatalogID(moveDlgObj, param){
	var rootCatalog = moveDlgObj.find('#rootCatalog');
	var leafCatalog = moveDlgObj.find('#leafCatalog');
	var leafSelect = moveDlgObj.find('#leafSelect');
	if (leafCatalog.css("display") == 'none' || leafSelect.css("display") == 'none'){  
		param.targetCatalogId= rootCatalog.attr("catalogid"); 
		param.targetCatalogIdGuid= rootCatalog.attr("catalogid_guid");     
	} else {
		param.targetCatalogId = leafCatalog.attr("catalogid");
		param.targetCatalogIdGuid = leafCatalog.attr("catalogid_guid");
	}
}


function addMaskDiv(body){
	var $dialog_background = $("<div class='dialog_background'></div>");
	if (typeof body == 'undefined') {
		$("body").append($dialog_background);	
	} else {
		body.append($dialog_background);
	}
}

function removeMaskDiv(body){
	if (typeof body == 'undefined') {
		$(".dialog_background").remove();	
	} else {
		body.find(".dialog_background").remove();
	}
}
