# 3️⃣ Розрахувати вартість товару з урахуванням знижки.
# Якщо вартість товару більше 100 грн. - знижка 3%.
# Якщо вартість товару більше 500 грн. - знижка 5%
# Якщо вартість товару більше 1000 грн. - знижка 10%

price = int(input("Вкажіть ціну"))
discount = 0

# 0.03, 0.05, 0.1

if price > 1000:
    discount = 0.1
elif price > 500:
    discount = 0.05
elif price > 100:
    discount = 0.03

priceWithDiscount = price - (price * discount)


if discount == 0:
    print('Знижки немає. Ціна ', price)
else:
    print("Ціна вашого товару зі знижкою ", priceWithDiscount)  
