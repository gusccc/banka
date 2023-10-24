import pandas
get_info=input()  #input information from terminal

fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()

# write your program code here
region_code = None

for l in range(len(info_list)):
    region_name=info_list[l][1]
    if region_name==get_info:
        region_code=info_list[l][0]
        break

region=[]
if region_code !=None:
    with open("data.csv","r") as data:
        next(data)
        for line in data:
            row=line.rstrip().split(",")
            if row[1]==region_code:
                region.append(int(row[3]))

print(sum(region))
