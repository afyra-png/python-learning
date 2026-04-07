#ai therapy detecting emotions : sad, angry, happy

sad_responses = [
    "Oh that sucks, hope you feeling better soon",
    "Every typhoon goes would have sunshine and rainbow afterwards. Don't give up man",
    "Since you're feeling like this, take a small sip of this tea i made ☕ ",
    "I'm here seeing you, you're not alone"
]

happy_responses = [
    "omg that's so cool glad to see you happy",
    "that made my day too man not gonna lie",
    "bru you deserve that moment dang that's tuff",
    "yoo i wanna know more what you're so happy about!"
]

angry_responses = [
    "heck yea you should leave that shi",
    "ikr that's so frustrating, but keep calm and save your energy queen",
    "omg i'd be so mad if i were you",
    "i can see you really that upset. we need to do smth for this problem"
]

import random 

while True: 
    user_input = input("\nWhat are you feeling right now? ")

    user_input = user_input.lower()

    if "exit" in user_input:
        print("Take care of yourself, see ya <3")
        break

    if "sad" in user_input or "rough" in user_input or "tired" in user_input or "numb" in user_input:
        response = random.choice(sad_responses)
        print(response)

    elif "happy" in user_input or "excited" in user_input or "delightful" in user_input or "wonderful" in user_input:
        response = random.choice(happy_responses)
        print(response)

    elif "angry" in user_input or "mad" in user_input or "furious" in user_input or "fuck" in user_input or "shit" in user_input:
        response = random.choice(angry_responses)
        print(response)

    else :
        print("Hmm im not sure i understand, but im here for youu !!")

    


