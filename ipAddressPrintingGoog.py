"""
print 1000 or 2000 ip addresses and you are given a starting IP address
"""

def getNextIpAddresses(ip, count):
    # ip = start ip
    # count = howmany next ip addresses to print
    print ip
    ipl = ip.split('.')
    o1, o2, o3, o4 = int(ipl[0]), int(ipl[1]), int(ipl[2]), int(ipl[3])
    for i in range(count):
        if o4 < 255:
            o4 += 1
        elif o3 < 255:
            o3 += 1
            o4 = 0
        elif o2 < 255:
            o2 += 1
            o3 = o4 = 0
        elif o1 < 255:
            o1 += 1
            o2 = o3 = o4 = 0
        else:
            print "None !"
        res = str(o1) + '.' + str(o2) + '.' + str(o3) + '.' + str(o4)
        line1 = 'neighbor ' + res + ' peer group EB-EB-V4'
        line2 = 'neighbor ' + res + ' description ebb.ibgp.scale.ixia'
        print(line1)
        print(line2)
getNextIpAddresses('1.1.1.1', 10)
