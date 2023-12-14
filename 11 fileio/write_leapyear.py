# read all years from year.txt and print leap years
# path="D:\\Desktop\\Python works\\fileio\year.txt"
# f=open(path,"r")

# for line in f:
#     year=int(line.rstrip("\n"))
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         print(year)


# ?write all leapyears into leap_years.txt
read_path="D:\\Desktop\\Python works\\fileio\year.txt"
fr=open(read_path,"r")

write_path="D:\\Desktop\\Python works\\fileio\leap_year.txt"
fw=open(write_path,"w")
for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        fw.write(str(year)+"\n")
