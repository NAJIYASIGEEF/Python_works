students=[
    {"id":1,"name":"John","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"Jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"Vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"Tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"Roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"Vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"Ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"Tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"Ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
   
    
]

# Q1 Total no.of students
# print("Total number of students:",len(students))

# Q2 Print all student names
# for stud in students:
#     print(stud.get("name"))

# # OR

all_studnts=[stud.get("name") for stud in students ]
# print(all_studnts)

# Q3 Print whose experience above 1

# for stud in students:
#     if stud["exp"]>1:
#         print(stud.get("name"))

# # OR
experience_1=[stud.get("name") for stud in students if stud.get("exp")>1]
# print(experience_1)

# Q4 Students who have skills in both python and java
# for stud in students:
#     if "java" in stud.get("skills") and "python" in stud.get("skills"):
#         print(stud.get("name"))

# Q5 print mca students name

# for stud in students:
#     if stud["qualification"]=="mca":
#         print(stud.get("name"))

# mca_students=[stud.get("name") for stud in students if stud.get("qualification")=="mca"]

# Q6 Most experienced student 
# most_exp=max(students,key=lambda m:m.get("exp") )
# # print(most_exp)
# high_exp=most_exp.get("exp")

# exp_students=[stud.get("name") for stud in students if stud.get("exp")==high_exp]
# print(exp_students)

# Q7 Student name having more than 2 skills

# for stud in students:
#     if len(stud.get("skills"))>2:
#         print(stud.get("name"))

# Q8 Students name starts with J
for stud in students:
       
    if stud.get("name").startswith("J"):
        print(stud.get("name"))

# Q9 maximum skill count

skill_count={}

for stud in students:
    skills=stud.get("skills")
    for sk in skills:
        if sk in skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)

max_skill=[(v,k) for k,v in skill_count.items()]
print(max(max_skill))

    




