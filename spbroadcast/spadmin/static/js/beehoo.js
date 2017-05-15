function checkBrowser(){
    if($.browser.safari || $.browser.mozilla || $.browser.opera){
        return true;
    }
    if($.browser.msie && parseInt($.browser['version'])>=9){
        return true;
    }
}

function checkNagivate(){
    var menu = (location.href.split("/")[4]);
    $("#"+menu).addClass("active");
}

checkNagivate();