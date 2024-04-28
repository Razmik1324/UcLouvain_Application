import unittest

adj_list1 = [[1, 3], [2], [0], [4], [3], []]
adj_list2 = [[1, 4, 5], [3], [0,1], [0, 4], [3,5], [1]]
adj_list3 = [[3,5],[1],[0,4],[3],[5],[2]]
def getReachable(adj_list, startingPoint):
    #create an empty set to be added to later
    setToReturn = set()    
    #check if the nested list at starting point is empty, if so return an empty set
    if len(adj_list[startingPoint]) != 0:
       #for loop to traverse over each index of the nested list at the starting point
      for i in range(len(adj_list[startingPoint])):
        #add the value at the starting point to the set    
        setToReturn.add(adj_list[startingPoint][i])  
        #set the index in the outer list to be traversed based on the value at starting point
        nestedIndex = adj_list[startingPoint][i]
        #for loop over the subsequent connections
        for j in range(len(adj_list[nestedIndex])):
            #add value at the specified outer and inner index
            setToReturn.add(adj_list[nestedIndex][j])
            #update next point to be traversed and added
            nestedIndex = adj_list[nestedIndex][j]
        #add additional values from the outer for loop
        setToReturn.add(adj_list[nestedIndex][j])

    return setToReturn      

print("Array 1, starting point 0: " + str(getReachable(adj_list1, 0)))
print("Array 1, starting point 3: " + str(getReachable(adj_list1, 3)))


class TestListResult(unittest.TestCase):
     
     def testResultSuccess1(self):
       self.assertEqual({0, 1, 2, 3, 4},getReachable(adj_list1, 0))   

     def testResultSuccess2(self):
       self.assertEqual({3, 4},getReachable(adj_list1, 3))  

     def testResultSuccess3(self):
       self.assertEqual({0, 1, 3, 4, 5},getReachable(adj_list2, 0))
       
     def testResultSuccess4(self):
       self.assertEqual({0, 2, 3, 5},getReachable(adj_list3, 0))

unittest.main()