# def maximumReliability(cost_arr, reliability, max_amount):
#     tot_dev = len(cost_arr)
#     devices = [1] * tot_dev
#     sum_cost_arr = sum(cost_arr)
#
#     if max_amount < 0:
#         return -1
#     elif max_amount == 0:
#         return devices
#     upp_bound = [1+(max_amount//i) for i in cost_arr]
#     ans_matrix = [[(reliability[0]**(i+1), cost_arr[0]*(i+1)) for i in range(upp_bound[0])]]
#     ans_matrix = []
#     for i in range(tot_dev):
#         arr = []
#         for j in range(upp_bound[i]):
#             arr.append([])
#     for dev_no in range(1, tot_dev):
#         for dev_amount in range(1, upp_bound[dev_no]+1):
#             for k in ans_matrix[dev_no-1]:
#                 ini_rel, alr_costed = k[0], k[1]
#                 rem_amount = max_amount-alr_costed
#                 if alr_costed+ dev_amount*cost_arr[dev_no] > rem_amount:
#                     break
#                 else:
#                     ini_rel *= reliability[dev_no]
#                     alr_costed -= dev_amount*cost_arr[dev_no]
#                     ans_matrix[dev_no][dev_amount].append(ini_rel, alr_costed)
#
#     max = 0
#     for i in range(len(ans_matrix[tot_dev-1])):
#         for j in ans_matrix[tot_dev-1][i]:
#             if j[0] > max:
#                 max = j[0]
#
#     return max
#
# print(maximumReliability([30,15,20], [.9,.8,.5], 105))