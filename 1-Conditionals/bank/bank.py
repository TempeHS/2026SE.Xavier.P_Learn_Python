text = input("Greeting: ").lower()

first = text[0]

if "hello" in text:
    print("$0")
elif first == "h":
    print("$20")
else:
    print("$100")