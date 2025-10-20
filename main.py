import random

print("CatGPT 🐈: say something (or type 'quit' to exit)")

replies = [
    "Meow! 🐾",
    "Wow, groundbreaking. Truly.",
    "Did you know I can nap for 16 hours a day? Impressive, right?",
    "I'm not ignoring you, I'm just contemplating the mysteries of the universe... or maybe just a spot on the wall.",
    "Oh, you're talking to me? How quaint.",
    "That's a you problem, not a me problem.",
    "ugh, humans.",
    "fasinating, please tell me less.",
    "Did you just meow at me?",
    "I'm sorry, I can't hear you over the sound of my own superiority.",
]


while True:
    user=input("You: ").strip()
    if user.lower() == 'quit':
        print("CatGPT 🐈: Fine. Nap Time.")
        break
    Respomse=random.choice(replies)
    print(f"CatGPT 🐈: {Respomse}")
 
          