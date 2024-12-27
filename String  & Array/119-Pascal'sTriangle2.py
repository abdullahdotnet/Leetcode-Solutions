def getRow(rowIndex):
    triangle = []
    if rowIndex ==0:
        return [[1]]
    for row_num in range(rowIndex+1):
        row = [ None ] * ( row_num + 1) 
        row[0], row[-1] = 1, 1

        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
        

        triangle.append(row)

    return triangle[-1]


# def getRow(rowIndex):
#     row = [1] * (rowIndex + 1)

#     for i in range(1, rowIndex + 1):
#         for j in range(i - 1, 0, -1):
#             row[j] += row[j - 1]

#     return row
print(getRow(3))