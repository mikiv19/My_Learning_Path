#Sorting and serching

'Insertion sort'

def insert_cabinet(cabinet,to_insert):  
    check_location = len(cabinet) - 1  
    insert_location = 0  
    while(check_location >= 0):    
        if to_insert > cabinet[check_location]:        
            insert_location = check_location + 1        
            check_location = - 1    
        check_location = check_location - 1  
    cabinet.insert(insert_location,to_insert)  
    return(cabinet)

'Measuring Algorithm Efficiency'
cabinet = [8,4,6,1,2,5,3,7]
def insertion_sort(cabinet):  
    newcabinet = []  
    while len(cabinet) > 0:    
        to_insert = cabinet.pop(0)    
        newcabinet = insert_cabinet(newcabinet, to_insert)  
    return(newcabinet)
sortedcabinet = insertion_sort(cabinet)
print(sortedcabinet)

cabinet = [1,2,3,3,4,6,8,12]
newcabinet = insert_cabinet(cabinet,5)
print(newcabinet)

from timeit import default_timer as timer
start = timer()
cabinet = [8,4,6,1,2,5,3,7]
sortedcabinet = insertion_sort(cabinet)
end = timer()
print(end - start)

'''
Counting steps
'''
def insert_cabinet(cabinet,to_insert):  
    check_location = len(cabinet) - 1  
    insert_location = 0  
    global stepcounter  
    while(check_location >= 0):    
        stepcounter += 1    
        if to_insert > cabinet[check_location]:        
            insert_location = check_location + 1        
            check_location = - 1    
            check_location = check_location - 1  
            stepcounter += 1  
            cabinet.insert(insert_location,to_insert)  
    return(cabinet)

def insertion_sort(cabinet):  
    newcabinet = []  
    global stepcounter  
    while len(cabinet) > 0:    
        stepcounter += 1    
        to_insert = cabinet.pop(0)    
        newcabinet = insert_cabinet(newcabinet,to_insert)  
    return(newcabinet)
cabinet = [8,4,6,1,2,5,3,7]
stepcounter = 0
sortedcabinet = insertion_sort(cabinet)
print("steps",stepcounter)
