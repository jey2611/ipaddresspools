import ipaddress

iprange = '10.22.240.0'

output = open('terminaloutput8.txt', 'a')



with open('CWLocalPoolCountandVPNName.txt','r') as VPNpoolName:

        for c in VPNpoolName:
            fields = c.split(',')
            increment = int(fields[1])
            vpnname = fields[0]
        #check for Integer when null
            if increment is not None:
                firstip = ipaddress.ip_address(iprange)
                lastip = ipaddress.ip_address(iprange) + increment
                iprange = lastip + 1
            else:
                firstip = ipaddress.ip_address(iprange)
                lastip = ipaddress.ip_address(iprange) + 1
                iprange = lastip + 1

            output.write("ip local pool ")
            output.write(vpnname)
            output.write(' ')
            output.write(str(firstip))
            output.write('-')
            output.write(str(lastip))
            output.write("\n")

        #output.write (therange)


VPNpoolName.close()
output.close()


