# %%
# def get_min(arr):
#     print(f"{arr}*********{min(arr)}")
#     return min(arr)

# def generate_subarrays(arr, k):
#     sub_arrs = []
#     min_arrs = []
#     for i in range(len(arr)-k+1):
#         tmp = arr[i:k+i]
#         print(f"{i} --> {tmp}")
#         sub_arrs.append(tmp)
#     #     tmp2 = get_min(arr[i:k+i])
#     #     min_arrs.append(tmp2)
#     # print(min_arrs)
#     return sub_arrs

# # def maxMin(arr, k):
# #     sub_arrs = []
# #     for i in range(len(arr)):
# #         tmp = min(arr[i:k+i])
# #         sub_arrs.append(tmp)
# #     print(max(sub_arrs))

# def maxMin(arr, k):
#     min_arrs = []
#     arrs = generate_subarrays(arr,k)
#     print(f"sub arrays {arrs}")
#     for i in range(len(arrs)):
#         min_arrs.append(min(arrs[i]))
#     print(f"min arras {min_arrs}")
#     print(max(min_arrs))

#     # for i in range(len(arr)):
#     #     tmp = min(arr[i:k+i])
#     #     sub_arrs.append(tmp)
#     # print(max(sub_arrs))
def maxMin(arr, k):
    sub_arrs = []
    min_arrs = []
    max_num = 0
    for i in range(len(arr)-k+1):
        tmp = min(arr[i:k+i])
        if(tmp > max_num):
            max_num = tmp
    return max_num

# arr = [1,2,3,1,2,1]
arr = [2,5,4,6,8]
k = 3
maxMin(arr,k)
# %%
