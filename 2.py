import heapq

def merge_sorted_list(list1,list2):
    return list(heapq.merge(list1,list2))

list1=[1,3,5,7]
list2=[2,4,6,8]
result = merge_sorted_list(list1,list2)
print("Merged List:",result)