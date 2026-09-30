# Program to find minimum number of notes

amount = int(input("Enter amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
count = 0

for note in notes:
    num = amount // note
    if num > 0:
        print(note, ":", num)
        count = count + num
        amount = amount % note

print("Minimum number of notes =", count)