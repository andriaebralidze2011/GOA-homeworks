# 1) შექმენით სია სადაც მოათავსებთ მნიშვნელობებს (სადაც გექნებათ მინიმუმ 10 მონაცემი და მინიმუმ 2 მათგანი მეორდება), მაგ: names = ["Saba", "NIka", "Saba", "Giorgi", "Nia", "Mariami", "Nia", "Saba", "Lasha", "Levani"].
# for ციკლის და პირობითი ოპერატორის გამოყენებით დაითვალეთ რამდენჯერ მეორდება "Saba" ამ მასივში, საბოლოოდ გამოიტანეთ ამ ელემენტის რაოდენობა სიაში.

names = ["Saba", "NIka", "Saba", "Giorgi", "Nia", "Mariami", "Nia", "Saba", "Lasha", "Levani"]
saba_count = 0

for i in names:
    if i == "Saba":
        saba_count += 1

print(saba_count)



count = names.count("Saba")
print(count)