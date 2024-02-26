#                               LAB 9

# TASK 1 

def Add(lst):
    result = 0
    for num in lst:
        result = result + num
    return result

def Substract(lst):
    result = lst[0]
    for num in lst[1:]:
        result = result - num
    return result

def Multiply(lst):
    result = lst[0]
    for num in lst[1:]:
        result = result * num
    return result

def Divide(lst):
    result = lst[0]
    if result==0:
        print("Error:Cannot divide by 0")
    else:
        for num in lst[1:]:
            result = result / num
        return result
    
given_List=[1,2,-3,4]
print(Add(given_List))
print(Substract(given_List))
print(Multiply(given_List))
print(Divide(given_List))

# TASK 2

def separate_indexes(lst):
    lst1 = []
    lst2 = []

    for num in range(len(lst)):
        if num % 2 != 0:
            lst1.append(lst[num])
        else:
            lst2.append(lst[num])

    return lst1, lst2

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1, lst2 = separate_indexes(lst)
print("Even index list:", lst1)
print("Odd index list:", lst2)

# TASK 3

def separator(lst):
    sum_even = 0
    sum_odd = 0
    for num in lst:
        if num % 2 == 0:  
            sum_even += num
        else:
            sum_odd += num
    return sum_even, sum_odd
list00 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_sum, odd_sum = separator(list00)

print("Sum of even numbers =", even_sum)
print("Sum of odd numbers =", odd_sum)

#TASK 4
def reverse_list(lst):
    reversed_lst = []

    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])

    return reversed_lst

random_numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(random_numbers)

print("Original List:", random_numbers)
print("Reversed List:", reversed_numbers)

# TASK 5
def first_last(lst1, lst2):
    combined_names = []
    for first, last in zip(lst1, reversed(lst2)):
        combined_names.append([first, last])
    return combined_names

first_names = ["Ali", "Ahad", "Wasi", "Waqas", "Shaaz"]
last_names = ["Qumail", "Wali", "Shah", "Asif", "Bari"]
result = first_last(first_names, last_names)

print("The answer is:",first_last(first_names,last_names))





    
    

        