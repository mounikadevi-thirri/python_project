# Mad Libs: The Lion and the Mouse

def madlib():
    # Predefined inputs for the Mad Libs story (to avoid input errors in certain environments)
    inputs = {
        "animal_1": "lion",
        "animal_2": "mouse",
        "sound": "roar",
        "action_1": "ran",
        "verb_1": "grabbed",
        "verb_2": "laughed",
        "verb_3": "help",
        "object_1": "net",
        "verb_4": "struggling",
        "verb_5": "gnawed"
    }

    # Extract values from predefined inputs
    animal_1 = inputs["animal_1"]
    animal_2 = inputs["animal_2"]
    sound = inputs["sound"]
    action_1 = inputs["action_1"]
    verb_1 = inputs["verb_1"]
    verb_2 = inputs["verb_2"]
    verb_3 = inputs["verb_3"]
    object_1 = inputs["object_1"]
    verb_4 = inputs["verb_4"]
    verb_5 = inputs["verb_5"]

    # Mad Libs story
    story = f"""
    One day, a {animal_1} was sleeping under a tree when a tiny {animal_2} {action_1} across its nose and woke it up. 
    The {animal_1} {verb_1} the {animal_2} with its paw and roared, "How dare you disturb my sleep! I will eat you!"

    The {animal_2} trembled and squeaked, "Please, mighty {animal_1}, spare me! If you let me go, I might {verb_3} you someday."

    The {animal_1} {verb_2} at the idea of a tiny {animal_2} {verb_3}ing a powerful {animal_1}, but it decided to let the {animal_2} go.

    A few days later, the {animal_1} was caught in a hunter's {object_1}. It roared and {verb_4}, but it couldn't break free. 
    Hearing the {animal_1}'s {sound}, the little {animal_2} rushed to the spot.

    "Don't worry, {animal_1}. I will {verb_3} you!" the {animal_2} said. It quickly {verb_5} through the ropes of the {object_1}, setting the {animal_1} free.

    The {animal_1} thanked the {animal_2} and said, "I was wrong to doubt you, little one. You saved my life!"

    Moral: Even the smallest creatures can make a big difference. Never underestimate anyone.
    """

    # Print the customized story
    print("\nHere is your Mad Libs story:")
    print(story)

# Run the Mad Libs function
madlib()
