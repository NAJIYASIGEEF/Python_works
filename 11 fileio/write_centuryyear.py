# write all century years from 1800 to 2024 into century_year.txt

# path="D:\\Desktop\\Python works\\fileio\\century_years.txt"
# f=open(path,"w")
# for year in range(1800,2025):
#     if year%100==0:
#         f.write(str(year)+"\n")

# write all years from 1800 to 2024
path="D:\\Desktop\\Python works\\fileio\\year.txt"
f=open(path,"w")
for year in range(1800,2025):
    f.write(str(year)+"\n")
