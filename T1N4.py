emp_list_v1 = []
emp_list_v2 = []
def palyndrome_check():
    string = input('Введите строку для проверки на палиндром: ')
    for i in string:
        emp_list_v1.append(i)
        emp_list_v2.append(i)
    emp_list_v1.reverse()
    if emp_list_v1 == emp_list_v2:
        return True
    elif emp_list_v1 != emp_list_v2:
        return False
palyndrome = palyndrome_check()
print(palyndrome)# T1N4
