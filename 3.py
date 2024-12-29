def merge_sorted_lists(list1,list2):
    #Initializing pointers for both lists
    i,j=0,0
    merged_list=[]


#Compare elements from both lists and add the smaller one to the merged list

    while i < len(list1) and j < len(list2):
        if list1[i] < list2 [j]:
            merged_list.append(list1[i])
            i +=1
        else:
            merged_list.append(list2[j])
            j+=1

#If any elements are left in list1, append them
    while i < len(list1):
        merged_list.append(list1[i])
        i+=1
    
    while j < len(list2):
        merged_list.append(list2[j])
        j+=1
    
    return merged_list

list1=[1,3,5,7]
list2=[2,4,6,8]

result = merge_sorted_lists(list1,list2)
print("Merged List:", result)