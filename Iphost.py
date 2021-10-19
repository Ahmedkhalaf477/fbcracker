import socket 
####################
print( " >>>>>>>>>>>>>>>> ELmagic Ahmed_Khalaf <<<<<<<<<<<<<< ")
print( " >>>>>>>>>> Wolcome To Script Ex_Ip Host <<<<<<<<<<<<< ")
host = input (" Enter Your Hostname   : " )
serv=socket.gethostbyname(host)

print(serv)