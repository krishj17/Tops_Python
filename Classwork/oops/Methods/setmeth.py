set1 = {10,20,30,40,50}

# set1.add(60);   print(set1) # adds randomly
# set1.remove(500);   print(set1) # remove based on value. throws error if element is not present.
# set1.discard(500);  print(set1) # discard based on value. does not throw error.
# set1.pop();   print(set1) # discard randomly

# for i in set1:
#     print(i)

set2 = {10,20,30,40,50}
set3 = {30,40,50,60,70}
# update and union works same, the only diff is that update is a function and thus we cannot 
# directly print it in print() function. also update copys data from set3 to set2.
# inshort ..._update does the operation and then updates set2 with the new output.
# whereas simple union, intersection, etc only does what its told and does not change the set2.


# set2.update(set3)
# print(set2)
# print(set2.union(set3))

# set2.intersection_update(set3)
# print(set2)
# print(set2.intersection(set3))

# set2.difference_update(set3)
# print(set2)
# print(set2.difference(set3))

# set2.symmetric_difference_update(set3)
# print(set2)
# print(set2.symmetric_difference(set3))