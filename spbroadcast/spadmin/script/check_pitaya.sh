#! /bin/bash
#  author cooler
#  time  2012-10-10 
#  program : 判断进行是否存在，并重新启动


function check(){
    count=`ps -ef |grep $1 |grep -v "grep" |wc -l`
    #echo $count
    if [ 0 == $count ];then
        cd /Application/pitaya/
        nohup python  $1 > /Application/pitaya/logs/check.log 2>&1 &
        echo "$1 start is ok!"
    else
	echo "$1 is running"
    fi
}
check pitayad.py 