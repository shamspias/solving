size_number = int(input())

main_sum = 0
avalable_shoes = list(map(int, input().split()))
sell_number = int(input())
for i in range(sell_number):
    a,b = map(int, input().split())
    if a in avalable_shoes:
        main_sum += b
        avalable_shoes.remove(a)
print(main_sum)
    
