cityTemp = open("citytemp.csv")
rec1 = cityTemp.readline()
city, temparature, unit=rec1.split(',')
prev_city = city
cityTemp.seek(0)

tempSum =0.0
count =0
averageTemp=0.0

for records in cityTemp:
    records=records.rstrip('\n')
    city, temparature, unit = records.split(',')
    if unit =='C':
        temparature=(float(temparature) * 9/5) + 32
    if city !=prev_city:
        averageTemp=tempSum/count
        print(prev_city+" "+str(round(averageTemp, 2)))    
        prev_city=city
        tempSum=0.0
        count=0
        averageTemp=0.0
    tempSum=tempSum+float(temparature)
    count=count+1    
else:
    averageTemp=tempSum/count
    print(prev_city+" "+str(round(averageTemp, 2)))    