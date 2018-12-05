import timeit
def Max_List(my_list):
    if len(my_list) == 1:
        return int(my_list[0])
    elif len(my_list) == 0:
        print('Emptylist!')
        quit()
    else:
        maxnum = Max_List(my_list[1:])
        if maxnum > int(my_list[0]):
            return maxnum 
        else:
            return int(my_list[0])
        


  

