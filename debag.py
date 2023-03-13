# get_url = 'https://piter-online.net/leningradskaya-oblast/business?house_id=4270758'
#
# dacha = "https://piter-online.net/leningradskaya-oblast/orders/sat"
# apartments = 'https://piter-online.net/leningradskaya-oblast/rates?house_id=4270758'
# office = 'https://piter-online.net/leningradskaya-oblast/business?house_id=4270758'
#
# list_type = ['sat', 'rates', 'business']
# print(len(list_type))
#
# list_get_url = get_url.replace('/', ' ').replace('?', ' ').split(' ')
#
# i = 0
# while i < 3:
#     if list_type[i] in list_get_url:
#         rez = i
#         break
#     i += 1
#
#
# if rez == 0:
#     print("дача")
# elif rez == 1:
#     print("квартира")
# elif rez == 2:
#     print("офис")
