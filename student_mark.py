
student=[]
print("Enter the number of student::")
n=int(input("number of the student"))
print(n)
while n>0:
    name=input("enter the student name:")
    #print("student name:",name)
    mark1=int(input("mark1"))
    mark2=int(input("mark2"))
    mark3=int(input("mark3"))
    #print("marks::",mark1,mark2,mark3)
    total=int(mark1+mark2+mark3)
    Average=round((total)/3,2)
    #print(f"Total:{total} \nAverage:{Average}")
    if mark1<35 or mark2<35 or mark3<35:
        Result='Fail'
    else:
        Result='Pass'
    if Average>=85:
        Grade='A'
    elif Average>=75:
        Grade='B'
    elif Average>=65:
        Grade='C'
    elif Average>=35:
        Grade='D'
    elif Average<=34:
       Grade='F'
    
    students={'Name':name,
              'Mark1':mark1,
              'Mark2':mark2,
              'Mark3':mark3,
             'Total':total,
             'Average':Average,
             'Result':Result,
             'Grade':Grade
            }
    student.append(students)
    

    n=n-1
highest_scorer=max(student,key=lambda x:x['Total'])
lowest_score=min(student,key=lambda x:x['Total'])
class_average=round(sum(s['Average'] for s in student)/len(student),2)
fail_count=sum(1 for s in student if s["Result"]=='Fail')
pass_count=sum(1 for s in student if s["Result"]=='Pass')
sorted_student=sorted(student,key=lambda x:x['Total'],reverse=True)
for s in student:
    print(s)
print(f"highest_scorer::: \n {highest_scorer}")
print(f"lowest_score::: \n {lowest_score}")
print(f"class average::: \n {class_average}")
print(f"Failed_student:: \n {fail_count}")
print(f"pass_count::: \n {pass_count}")
print("top 3 student \n")
for s in sorted_student[:3]:
    print(f"{s['Name']} --{s['Total']}")

    
