#------------------------------------------------------------------------------------------------------------------------------------
# 7.9
# Напишите 3 варианта, как в эту строку вместо подчёркиваний можно подставить числа 4 и 4 (автомобиля и омнибуса)
# и название моста «Саутуарк»: "Сегодня утром __ автомобиля и __ омнибуса проехали по мосту __."
count = 4
name = "Саутуарк"

print("7.9: ", "Сегодня утром %d автомобиля и %d омнибуса проехали по мосту %s." % (count, count, name))
print("7.9: ", "Сегодня утром {count} автомобиля и {count} омнибуса проехали по мосту {name}.".format(count=count, name=name))
print("7.9: ", f"Сегодня утром {count} автомобиля и {count} омнибуса проехали по мосту {name}.")