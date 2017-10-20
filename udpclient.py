import socket
import time







target_host = "127.0.0.1"
target_port = 12000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hi = "hello"

time_out = time.clock()

print(time_out)



client.sendto(hi.encode('utf-8'), (target_host, target_port))

data, addr = client.recvfrom(4096)

triptime = time.clock() - time_out


print (data)
print ("Your trip time was: " + str(triptime))




