print("CatGPT 🐈: say something (or type 'quit' to exit)")
while True:
    user=input("You: ").strip()
    if user.lower() == 'quit':
        print("CatGPT 🐈: Fine. Nap Time.")
        break
    print(f"CatGPT 🐈: {user}")
          