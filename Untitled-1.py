#1

# while True:
#     user_input = input("Skriv ett tal: ")
#     if user_input.isdigit():
#         print("Tack, du skrev ett tal!")
#         break
#     else:
#         print("Fel! Du måste skriva bara siffror.")

#2

# print("Skriv ett tal mellan 1–13 eller 'q' för att avsluta.")

# highest = None
# lowest = None

# while True:
#     user_input = input("Tal: ")

#     if user_input == "q":
#         print("Spelet avslutat!")
#         break

#     if not user_input.isdigit():
#         print("Endast siffror eller 'q' för att sluta.")
#         continue

#     num = int(user_input)

#     if 1 <=num <=13:
#         if highest is None or num > highest:
#             highest = num
#         if lowest is None or num < lowest:
#             lowest = num
    
# print(f"ditt högsta var:{highest} och din lägsta var {lowest}")

#3

# word=input("Skriv ORD NUUUU:")

# print(word[:10])

#4

# Word = input("Säg vad fan:")

# max=10

# if len(Word) > max:
#     print(Word[:max]+ "...")
# else:
#     print(Word)


#5

# Word=input("Skriv ett ord:")
# print (Word.upper())

# Word=input("Skriv ett ord:")
# print (Word.lower())