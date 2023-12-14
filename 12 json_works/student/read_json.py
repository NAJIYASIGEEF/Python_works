from json import load
f=open("D:\Desktop\Python works\jason_works\students.json","r")
data=load(f)
print(data)

all_names=[emp.get("name") for emp in data]
print(all_names)

all_dept={emp.get("department") for emp in data}
print(all_dept)

max_sal=max(data,key=lambda d:d.get("salary"))
print(max_sal)



