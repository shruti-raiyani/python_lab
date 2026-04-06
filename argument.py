# 
def student_info(name, age=18, course="BSC IT"):
    print("name:", name)
    print("age:", age)
    print("course:", course)
    print("-" * 20)
student_info("ravi")
student_info("sema", 20)
student_info("amit", 19, "BSC IT") 

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add_numbers(10, 20))
print(add_numbers(5, 10, 15))
print(add_numbers(1, 2, 3, 4, 5))        

