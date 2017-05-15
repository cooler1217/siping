#! /bin/bash   


ps -ef|grep mongo | grep -v 'grep' |wc -l |awk '{if($1>1){print "mdb is ok";}else{ system("rm -fr /home/mongoRepSet/mongod.lock && /usr/bin/mongod -f /etc/mongodb.conf ")}}'
