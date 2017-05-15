function wintopii66(val)
{
    if  (document.getElementByIdx_x(val).style.display!="none")
     {
  document.getElementByIdx_x(val).style.display="none";
    }
      else
     {
    document.getElementByIdx_x(val).style.display=""
    return;
    }
}
document.writeln("<DIV id=\"qq_left\" style=\"top:366px;left:10px;POSITION:absolute;Z-INDEX:100;\">");
document.writeln("<table width=\"127\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\">");
document.writeln("  <tr>");
document.writeln("    <td><a href=\"tencent://message/?uin=2522883451&Site=在线咨询&Menu=yes\"><img src=\"/static/images/qq.png\" border=\"0\"></a></td>");
document.writeln("  </tr>");
document.writeln("</table>");
document.writeln("");
document.writeln("<\/div>");
//滚动代码开始
function qqshow(){
if (document.body.offsetWidth >900)
{
document.getElementByIdx_x("qq_left").style.top=(document.documentElement.scrollTop+166)+"px";
}
else
{
document.getElementByIdx_x("qq_left").style.display="none";
}
// document.getElementByIdx_x("qq_right").style.left=(document.documentElement.scrollLeft+document.documentElement.clientWidth-  document.getElementByIdx_x("qq_right").offsetWidth-6)+"px";
}
function showqq(){
setTimeout("qqshow();",10);
}
window.onscroll=showqq;
window.onresize=qqshow;
window.onload=qqshow;
function fullScreen(){
 this.moveTo(0,0);
this.outerWidth=screen.availWidth;
this.outerHeight=screen.availHeight;
}
window.maximize=fullScreen;