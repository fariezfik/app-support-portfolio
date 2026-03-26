
f=open("/Users/fariezfikhi/repos/app-support-portfolio/access.log")

count404 =0
count500 = 0

for line in f:
    if "404" in line:
        
        ip=line.split()[0]
        count404+= 1

        thisdict404={"IP address" : "x.x.x.x",
                  "Error code ": "404",
                  "Error Count": "x"                  
                   }
        thisdict404["IP address"]=ip
        thisdict404["Error Count"]=count404
        
    if "500 " in line:
        
        ip=line.split()[0]
        count500+=1

        thisdict500={"IP address" : "x.x.x.x",
                  "Error code ": "500",
                  "Error Count": "x"                  
                   }
        thisdict500["IP address"]=ip
        thisdict500["Error Count"]=count500

print(thisdict404)
print(thisdict500)
f.close()