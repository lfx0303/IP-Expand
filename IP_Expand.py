print('IP Expand Script')
f = open("ip-ranges.txt", "rt")
f1=open("ip-ranges-expanded.csv", "w")
numlines=0
counter=0
for x in f: 
	IsRange=""
	numlines+=1
	if numlines >1: 
#	and numlines < 4:
		linelength=len(x)
#		print(x)
		firsttab=x.find("\t")
		dot1=x.find(".",firsttab,linelength)
		dot2=x.find(".",dot1+1,linelength)
		dot3=x.find(".",dot2+1,linelength)
		secondtab=x.find("\t",dot3+1,linelength)
		dot4=x.find(".",secondtab+1,linelength)
		dot5=x.find(".",dot4+1,linelength)
		dot6=x.find(".",dot5+1,linelength)
		thirdtab=x.find("\t",dot6+1,linelength)
		fourthtab=x.find("\t",thirdtab+1,linelength)
#		READ FIRST IP ADDRESS
		ip1_1=int(x[firsttab:dot1].strip())
		ip1_2=int(x[dot1+1:dot2].strip())
		ip1_3=int(x[dot2+1:dot3].strip())
		ip1_4=int(x[dot3+1:secondtab].strip())
#		READ SECOND IP ADDRESS
		ip2_1=int(x[secondtab:dot4].strip())
		ip2_2=int(x[dot4+1:dot5].strip())
		ip2_3=int(x[dot5+1:dot6].strip())
		ip2_4=int(x[dot6+1:thirdtab].strip())
#		READ RANGE DESCRIPTION
		desc=x[thirdtab:fourthtab].strip()
		if ip1_3 == ip2_3 and ip1_4 == ip2_4:
			IsRange="N"
		else:
			IsRange="Y"
		for a in range (ip1_3,ip2_3+1):
			for b in range (ip1_4,ip2_4+1):
				ip1_string=str(ip1_1)+"."+str(ip1_2)+"."+str(a)+"."+str(b)+","+x[firsttab:secondtab]+"-"+x[secondtab:thirdtab]+","+IsRange+","+desc
				counter+=1
				print(counter,end="\r")
				f1.write(ip1_string)
				f1.write("\n")
#print(numlines)
f.close()
f1.close()