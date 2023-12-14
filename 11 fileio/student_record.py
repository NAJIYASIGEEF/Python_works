# students who passed 
all_stud=open("D:\\Desktop\\Python works\\fileio\\students.txt","r")
failed_stud=open("D:\\Desktop\\Python works\\fileio\\failed.txt","r")


all_stud_set={st.rstrip("\n") for st in all_stud}

fail_stud_set={st.rstrip("\n") for st in failed_stud}

passed_stud=all_stud_set.difference(fail_stud_set)
print(passed_stud)

