
#
# def getArrayScore(array):
#     score = 0
#     for box in array:
#         score = score + box - 1.5
#     return score
#
# arrayList = [[]]
# for _ in range(31):
#     newArrayList = []
#     for array in arrayList:
#         for i in range(3):
#             newArray = array.copy()
#             newArray.append(i)
#             if(getArrayScore(newArray) > 0):
#                 newArrayList.append(newArray)
#     arrayList = newArrayList
#
# for array in arrayList:
#     print(getArrayScore(array))

# score = 0
# for repo in range(31):
#     score = score + repo
#     print(repo, ': score: ', score)



import random

for _ in range(50):
    print(random.randint(1, 6))