import argparse
from socket import *


def connScan(targetHost,targetPort):
	try:
		connectSocket=socket(AF_INET,SOCK_STREAM)
		connectSocket.connect((targetHost, targetPort))
		connectSocket.send('Hello how are you\r\n')
		result = connectSocket.recv(100)
		print '[+] %d/tcp open'% targetPort
		print '[+]' + str(result)
		connectSocket.close()
	except:
		print '[-] %d/tcp closed' % targetPort

def portScan(targetHost,targetPorts):
	try:
		targetIP=gethostbyname(targetHost)
	except:
		print "\n[-] Cannot resolve %s" % targetHost
		return

	try:
		targetName=gethostbyaddr(targetIP)
		print '\n[+] Scan result for: ' + targetName[0]
	except:
		print '\n[+] Scan result for: ' + targetIP
	setdefaulttimeout(1)

	for targetPort in targetPorts:
		print 'Scanning port: ' + targetPort
		connScan(targetHost,int(targetPort))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Port Scanning usage -host <target host> -port <target port>")
	parser.add_argument('--host',type=str, help='specify target host', required=True)
	parser.add_argument('--port',type=str, help='specify target port[s] separated by comma', required=True)
	args = parser.parse_args()
	targetHost = args.host
	targetPorts = str(args.port).split(',')
	
	portScan(targetHost,targetPorts)
	

