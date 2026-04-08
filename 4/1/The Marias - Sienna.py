import time 

def type_word(word):
    for char in word:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print("", end="")


lyrics = [
    ("\n\nO",1.0),
    ("o", 1.0),
    ("h", 0.7),
    (" Sienna", 4.5),

    ("\nWould've", 0.1),
    (" been", 0.1),
    (" cute", 3.5),

    ("\nO", 1.0),
    ("o", 1.0),
    ("h", 0.7),
    (" Sienna", 4.8),

    ("\nWould", 0.06),
    (" look", 0.06),
    (" just", 0.1),
    (" like", 0.05),
    (" you\n", 2.6),

    ("\nWith", 0.4),
    (" a", 0.01),
    (" temper", 0.2),
    (" like", 0.2),
    (" you,", 2.0),
    (" run", 0.1),
    (" around", 0.08),
    (" like", 0.03),
    (" you", 2.0),

    ("\nJumping", 0.3),
    (" in", 0.1),
    (" the", 0.1),
    (" pool,", 0.9),
    (" like", 0.2),
    (" you", 2.8),
    
    ("\nSing", 0.4),
    (" to", 0.01),
    (" all", 0.2),
    (" her", 0.2),
    (" pets", 2.0),
    (" in", 0.1),
    (" the", 0.08),
    (" way", 0.01),
    (" I", 0.2),
    (" did", 2.1),

    ("\nBe", 0.3),
    (" sensitive", 1.6),
    (" like", 0.3),
    (" you\n\n\n", 2.7)
]

for word, delay in lyrics :
    type_word(word)
    time.sleep(delay)