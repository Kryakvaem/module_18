#При подсчете скидки на полную стоимость заказа 
# НЕ учитываются посетители конференции, которым менее 18 лет.

count_tickets = int(input("Введите количество билетов, которые хотите приобрести на мероприятие:"))
coupon = 10
price_sum = 0
count_less_18 = 0

for i in range(count_tickets):
    age = int(input("возраст посетителя %d:"% (i+1)))
        
    if age>=18 and age<25:
        price_sum += 990
    elif age>=25:
        price_sum += 1390
    else:
        price_sum += 0
        count_less_18 +=1
       


if (count_tickets - count_less_18)>3:
    price_sum = price_sum - coupon/100*price_sum

print("сумма к оплате",price_sum)
