


# You are given operations, an array containing the following two types of operations:
# [0, a, b] - Create and save a rectangle of size a xb:
# [1, a, b] - Answer the question: "Could a box of size ax b fit inside of each of the earlier saved
# rectangles?". It is possible to rotate the rectangles by go degrees; ie: a rectangle of dimensions a xb
# can be rotated so that its dimensions are b x
# IE
# Your task is to return an array of booleans, representing the answers to the second type of operation, in the
# order they appear.
# GS
# Note that the operations should proceed iteratively, so when operations[i] is executed, only the results of
# the previous operations o
# 1
# - 1 are avallable.
# Example
# • For operations = [[1, 1, 1]], the output should be solution (operations) = [true]
# There are no rectangles, so return true because there were no rectangles that the box was unable to fit
# inside
# For operations = [[0, 100000, 100000]] the output should be solution(operations)
# = 0


operations = [[0, 3, 3], [0, 5, 2], [1, 3, 2], [1, 2, 4]]

def Solution(operations):
    saved_matrix = []
    res = []
    for idx,operation in enumerate(operations):
        if operation[0] == 0:
            saved_matrix.append([operation[1], operation[2]])
        if operation[0] == 1:
            if idx == 0:
                res.append(True)
                continue
            flag = False          
            a2 = min(operation[1],operation[2])
            b2 = max(operation[1],operation[2])
            for sm in saved_matrix:
                a1 = min(sm[0],sm[1])
                b1 = max(sm[0],sm[1])
                if not((a2 <= a1 or a2<= b1) and (b2 <= a1 or b2 <= b1)):
                    print(operation)
                    print(a1,a2,b1)
                    print(a1,b2,b1)
                    res.append(False)
                    flag = True
                    break
            if flag == False:
                res.append(True)

    return res

print(Solution(operations))

