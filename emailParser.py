import email
from email import policy
from email.parser import BytesParser
import glob

with open("spamemail.eml", 'rb') as fp:
    msg = BytesParser(policy = policy.default).parse(fp)


print("MTA of USER",end = "\n")
print("-----------",end = "\n")

mydict = {}

for item in msg._headers:
	if(item[0] == "Received"):
		print(item[1])

for item in msg._headers:
	mydict[item[0]] = item[1]

ipaddress = mydict["Received-SPF"]

ipaddress = ipaddress[ipaddress.index('=')+1 : ipaddress.index(';')]

print("\nSender IP-Address = {}\n\n".format(ipaddress))

sd = mydict["From"]

print("Details of Sender : \n==================\nName {}\n\nEmail : {}\n".format(sd[sd.index('"')+1 : sd[1:].index('"')], sd[sd.index("<")+1 : sd.index(">")]))
"""
print(msg)


text = msg.get_body(preferencelist = ('plain')).get_content()
print(text)
"""
