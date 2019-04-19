#Now, Jimothy, we come to the first problem you'll have problems with. Possibly.
#In case you can't tell, this is to multipy matrices.
#Go ahead and yeet your fleek into cash money.
#Sufficiently disgusted and/or confused? Good, now you're getting the spirit.
def matmult(a,b):
    zip_b = zip(*b)
    # uncomment next line if python 2.7 : 
    #zip_b = list(zip_b)
    return [[sum(ele_a**ele_b for ele_a, ele_b in zip(a, b)) 
             for col_b in zip_b] for row_a in a]
x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
y = [[1,2],[1,2],[3,4]]
print(matmult(x,y))
