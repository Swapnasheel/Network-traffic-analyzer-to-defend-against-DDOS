import subprocess
import os

proc = subprocess.Popen(["./detection.sh"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
s = out.split()
#print out
x = s[0::2]
#print x
y = s[1::1]
#print y
n=0
for n in x:
	if int(n) > 100:
		print " Your server is under attack by attacker - {}".format(y[0])
		print " No. of sockets opened by attacker - {}".format(x[0])
		ans=True
		while ans:
	    		print ("""
	    		1.Mitigate the attack on your server
	  		2.Resume current server state
			3.Exit from the menu
	    		""")
	    		ans=raw_input("Enter the option: ") 
	    		if ans=="1": 
				os.system('sudo gnome-terminal -x sh -c "./mitigation.sh; bash"')
				break;
	    		elif ans=="2":
	    	 			 print("\n Resuming the current server state")
					 break;	 
	    		elif ans=="3":
	      				print("\n Goodbye")
					break; 
	   		elif ans !="":
	     				 print("\n Not Valid Choice Try again") 
else:	
	print " Your server is safe!"
