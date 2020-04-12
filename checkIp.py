import re

regex = '''^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'''

def checkIp(Ip):
   if (re.search(regex, Ip)):
      print "valid IP: "+ str(Ip)
   else:
      print "invalid IP: "+ str(Ip)

if __name__ == '__main__':
   ipList = ["255.256.355.422", "10.0.0.2", "4.245.954.1", "100.90.14.0"]
   for ip in ipList:
      checkIp(ip)
