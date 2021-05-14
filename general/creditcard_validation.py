card_number = list(input("Enter a card number: ").strip())
#print(card_number)

card_number = [int(number) for number in card_number]
check_num = card_number.pop(-1)
card_number.reverse()
#print(card_number)

for number in range(0,len(card_number),2):
    card_number[number] = card_number[number]*2
    if card_number[number] > 9:
        card_number[number] = card_number[number] - 9
#print(card_number)

check_num += sum(card_number)
print(check_num)
if check_num % 10 == 0:
    print("Entered card Number is valid")
else:
    print("Entered card number is invalid")
