import pyfiglet
import sys
import socket

#Algumas partes extraídas do https://www.geeksforgeeks.org/port-scanner-using-python/

def main():

	ascii_banner = pyfiglet.figlet_format("TECHACK - PORT SCANNER")
	print(ascii_banner)

	if len(sys.argv) == 2:
		ip = sys.argv[1]
	else:
		print("IPinválido")

	starting_port = int(input("Digite a primeira porta: "))
	ending_port = int(input("Digite a última porta: "))

	try:
		
		
		for port in range(starting_port,ending_port):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			
			# returns an error indicator
			result = s.connect_ex((ip,port))
			if result ==0:
				service = socket.getservbyport(port, "tcp")
				print(f"Porta {port} aberta rodando {service}")
			s.close()
			
	except KeyboardInterrupt:
			print("\n Exiting Program !!!!")
			sys.exit()
	except socket.gaierror:
			print("\n Hostname Could Not Be Resolved !!!!")
			sys.exit()
	except socket.error:
			print("\ Server not responding !!!!")
			sys.exit()

if __name__ == "__main__":
	main()