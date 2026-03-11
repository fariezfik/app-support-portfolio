f=open("/Users/fariezfikhi/repos/app-support-portfolio/access.log")

count404 =0
count500 = 0
for line in f:
    if "404" in line:
        count404+= 1
    if "500 " in line:
        count500+=1

print("Total Error 404 :",count404)
print("Total Error 500 :",count500)



f.close()