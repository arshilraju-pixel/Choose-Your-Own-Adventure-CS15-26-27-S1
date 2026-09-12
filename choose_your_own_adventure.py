from selectors import SelectSelector

user_choice = None

story = """Your Own Princess Adventure 

You are princess Theodosia, the princess of the magical kingdom of Evermere. One morning, you wake up to find a 

mysterious letter sitting on your pillow. 

the letter says: 

"Dear Princess Theodosia,

Your kingdom is in danger. Only you can save it."

You quickly get dressed and prepare for your adventure.

you reach the crossroads outside of the catsle. 

A : Follow the glowing path into the enchanted forest 
OR
B :Follow the golden path toward the mysterious castle tower"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """Princess Theodosia follows the glowing path into the enchanted forest.
    
    The trees sparkle with tiny magical lights.
    
    After walking for a while, she finds a beautiful fairy sitting beside a fountain.
    
    The fairy smiles and says:
    
    "Princess, I have been waiting for you." The fairy offers the princess two choices
     
     A : Ask the fairy for a magical spell.
     OR
     B : Ask the fairy for a magical sword."""

    print(story)

    user_choice = input().lower()

if user_choice == "a":
    story = """The fairy gives the Princess Theodosia a glowing purple spell. "You may use this spell only once," the fairy warns. 
    
    suddenly, a giant dragon appears in the sky! The dragon lands in front of Theodosia and blocks her path. 
    
    A: Use the magical spell
    OR:
    B: Try to befriend the dragon"""

    print(story)

    user_choice = input().lower()

if user_choice == "a":
    story = """Princess Theodosia raises her hand and uses the magical spell.
    
    A huge burst of sparkling light surrounds the dragon.
    
    Instead of attacking, the dragon becomes peaceful.
    
    the dragon agrees to protect Evermere forever.
    
    Princess Theodosia returns home as a hero
    
    THE END"""

    print(story)

else:
    story = """Princess Theodosia slowly approaches the dragon and offers it a flower.
    
    The dragon is surprised by her kindness. 
    
    It bows its head and becomes her loyal companion. 
    
    Together, they fly across the kingdom and protect Evermere. 
    
    Princess Theodosia becomes known as the Dragon princess.
    
    THE END"""

    print(story)
story = """The fairy gives Princess Theodosia a sparkling silver sword.
    
"This sword can defeat any creature," the fairy says.

Theodosia continues through the forest until she reaches an ancient stone bridge. 

A giant troll is blowing the way. 

A: Fight the troll with the magical sword
OR
B: Try to convince the troll to let you pass"""

print(story)
user_choice = input().lower()

if user_choice == "a":

    story = """Princess Theodosia bravely raises her magical sword.
    
    After a difficult battle, she defeats the troll. 
    
    The bridge is finally safe to cross.
    
    Aria continues her journey and saves the kingdom from danger.
    
    THE END"""

else:
    story = """Princes Theodosia speaks calmly to the troll. she explains her goal of saving her kingdom. 
    
    The troll is impressed by her bravery and lets her cross. 
    
    It even gives her a magical jewel to help her through her journey.
    
    The princess returns to Evermere and becomes the wisest princess in the kingdom. 
    
    THE END"""

    print(story)


story = """The princess follows the golden path toward th castle tower. The tower is dark and mysterious.

Inside, she discovers a secret room filled with magical treasures. 

suddenly, a mysterious wizard appears. 

The wizard says:

"I know why you're here"

He points toward two magical objects.

A: Take the glowing golden crown.
OR
B: Take the mysterious crystal necklace."""

print(story)
user_choice = input().lower()
if user_choice == "a":
    story = """The princess picks up the golden crown. 
    
    The crown floats above her head and gives her magical powers.
    Suddenly, the castle begins shaking.
    The wizard tells her that her kingdom is under attack.
A: Use the crown's magic to protect the kingdom.
OR
B: Give the crown to the wizard
"""
    print(story)
    user_choice = input().lower()
    if user_choice == "a":
        story = """The princess uses the crown's magic to create a giant magical shield.
        
        The kingdom is protected.
        
        Everyone celebrates princess Theodosia's achievements as the greatest ruler. 
        
        THE END"""

    print(story)
else:
    story = """Princess Theodosia gives the crown to the wizard. 
    
        The wizard suddenly reveals that he was testing her.
    
        he rewards her honesty by making her an honorary sorceress. 
    
        THE END"""

    print(story)

    story = """Princess Theodosia picks up the crystal necklace.
    
    The necklace shows her a vision of the future.
    
    She sees the kingdom being attacked by a storm.
    
    A: Follow the vision and save your kingdom
    OR
    B: Return to the kingdom and warn everyone"""

    print(story)
user_choice = input().lower()
if user_choice == "a":
    story = """Princess Theodosia follows the vision deep into the mountains. 
    
    She discovers a magical crystal causing the storm.
    
    Theodosia destroys the crystal and the storm disappears.
    
    The kingdom is saved. 
    
    Princess Theodosia becomes The Gaurdian of Evermere.
    
    THE END"""

    print(story)
else:
    story = """Princess Theodosia rushes back to the kingdom and warns everyone.
    
    The citizens evacuate and seek shelter to wait till the storm passes.
    
    everyone survives safely.
    
    The kingdom celebrates princess theodosia for her quick thinking. 
    
    THE END"""

    print(story)






