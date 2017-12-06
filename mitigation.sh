#!/bin/bash

echo "Started Mitigation.. "
echo
echo "Limiting number of Http connections.."
sudo iptables -I INPUT -p tcp --dport 80 -m connlimit --connlimit-above 50 --connlimit-mask 20 -j DROP
echo
#echo "Flushing IPtables.."
#sudo iptables -F
#echo
echo "Killing attacker's sockets"
sudo pgrep apache2 >> pids.txt
filename="pids.txt"
while read -r line
do
	pid=$line
	sudo kill -9 $pid
done < "$filename"
sudo service apache2 restart
echo
echo "Enabled defense against Slow Lorris attack!"
