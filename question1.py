def find_duplicates(array, number):
    array.append(number)
    array.sort()
    
    duplicates = set()
    
    for i in range(len(array) - 1):
        if array[i] == array[i+1]:
            duplicates.add(array[i])
       
    if len(duplicates) == 0 : 
        print("no duplicate found")   
    else:
        print ("duplicates found", list(duplicates)) 
        
    return list(duplicates)
          
input1 = [1, 2, 4, 3, 6] 
input2 = 7  
find_duplicates(input1,input2)    

input1 = [1, 2, 4, 3, 6, 2, 5] 
input2 = 3 
find_duplicates(input1,input2)                          
            
    


    

