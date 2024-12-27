# def generate(numRows):
#     res = [[1]]

#     for _ in range(numRows-1):
#         dummyrow = [0]+res[-1]+[0]
#         row = []
#         for i in range(len(res[-1])+1):
#             row.append(dummyrow[i]+dummyrow[i+1])
#         res.append(row)
#     return res
def generate(numRows):
        triangle = []

        for row_num in range(numRows):
            row = [ None ] * ( row_num + 1) 
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            

            triangle.append(row)

        return triangle
print(generate(5))