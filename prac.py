# choice =0
# if choice:
#     print("i am 1")
# else:
#     print("I am 0")


#epsilon greedy working v2
# import random 
# best=0
# ran = 0
# for _ in range(100):
#     num = random.random()
#     if (num<0.1):
#         choice = random.choice([0,1])
#         if choice:
#             best+=1
#             ran+=1
#     else:
#         best+=1
# print(best,ran)


# Q = {
#     (15, 10, False): {
#         0: 0.65,  # Stick
#         1: 0.35   # Hit
#     },
#     (18, 6, True): {
#         0: 0.72,
#         1: 0.41
#     }
# }
# print(Q[(15, 10, False)][0])

li = [
    ((15, 10, False), 1),
    ((18, 10, False), 0)
]
for state,action in li:
    print(state,action)