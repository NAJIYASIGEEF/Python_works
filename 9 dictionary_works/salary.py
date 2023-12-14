employee={"id":100,"name":"hari","department":"developer","salary":50000}

employee["department"]="senior dev"

if "salary" not in employee:
    employee["salary"]=45000
else:
    employee["salary"]+=10000

print(employee)