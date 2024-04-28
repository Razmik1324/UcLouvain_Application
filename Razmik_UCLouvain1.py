import unittest

adj_mat1 =   [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]

adj_mat2 =   [[0, 1, 0, 1, 0, 0],
             [1, 0, 1, 0, 1, 0],
             [1, 0, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0]]

adj_mat3 =   [[0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 1, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 1, 0, 0, 0]]

def getAdjList(adj_mat):
    #final adj_list to return at the end of the function
    adj_list = []
    #for loop to traverse horizontally through each index of the matrix
    for i in range(len(adj_mat)):
        #temporary list which is refreshed with each outer for loop
        tempList = []
        #Nested for loop to traverse the nested lists in the matrix
        for j in range(len(adj_mat[i])):
                #Check for connection towards a specific node               
                if adj_mat[i][j] == 1:
                    #Update temp list with j value each time a match occurs                    
                    tempList.append(j)

        #append the temporary list to the final one to return
        adj_list.append(tempList)

    return adj_list    
    

class TestListResult(unittest.TestCase):
     
     def testResultSuccess1(self):
       self.assertEqual([[1, 3], [2], [0], [4], [3], []],getAdjList(adj_mat1))   

     def testResultSuccess2(self):
       self.assertEqual([[1, 3], [0,2,4], [0,3], [1,4], [3], [2]],getAdjList(adj_mat2))  
     def testResultSuccess3(self):
       self.assertEqual([[3], [2,4], [5], [1,4], [2,3], [2]],getAdjList(adj_mat3))

print("first adjacency list: ")
print(getAdjList(adj_mat1))

unittest.main()