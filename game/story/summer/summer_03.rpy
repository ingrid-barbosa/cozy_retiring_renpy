label summer_03:
    scene bg summer_3 at moonlight
    with dissolve
    "Day 3 - Summer"
    "Fern follows the moonlight along the coast. The water shines softly, almost like it is breathing."
    $ companion = renpy.random.choice(("rowan", "caelum"))
    if companion == "rowan":
        show rowan at rowan_portrait
        call rowan_introduction
        rowan "The sea has been loud tonight. I came down to see what had stirred it."
        if shell_cut:
            rowan "How did you hurt your hand?"
    else:
        show caelum at speaker_right
        caelum "The ocean looks different tonight."
        caelum "Some places remember the magic of the past."
        if shell_cut:
            caelum "Did the rocks catch your hand?"
    if shell_cut:
        fern "Yesterday, by the shell. I wrapped it when I got home."
    fern "Wait. Did you hear that?"
    "Two hollow notes sound from a cave behind the reef."
    menu:
        "Follow the sound through the cave together.":
            $ coragem += 1
            $ visited_dark_summer = True
        "Listen from the beach, then go home.":
            $ independencia += 1
            $ day_summary = f"Fern heard two notes by the reef with {companion.capitalize()}. She listened from the beach until they faded, then went home."
            "Fern listens until the notes fade into the tide."
            call return_home
            return
    scene bg dark_summer
    with dissolve
    "The cave opens onto a pocket of pale sand. Blue light runs under the water, and the palms stand perfectly still."
    "The sound comes again. This time the water answers in the voice of someone Fern almost remembers."
    if companion == "rowan":
        show rowan at rowan_portrait
        rowan "The tide carries scraps of voices here. My first night on this coast, I thought one of them was calling me home."
        fern "What did you do?"
        rowan "I stayed until it finished. Then I went home the way I came."
    else:
        show caelum at speaker_right
        caelum "The spirits borrow voices the way they borrow trinkets. Once the tide turns, they let them go."
        fern "I wonder whose voice that was before the sea found it."
    menu:
        "Remember the voice and write down what it said.":
            $ curiosidade += 1
            $ day_summary = f"Fern followed the sound through the cave with {companion.capitalize()}. She brought home the words she heard on the hidden beach."
            "Fern repeats the words softly so she can put them on paper at home."
        "Ask how to return when the tide is low.":
            $ independencia += 1
            $ day_summary = f"Fern reached the hidden beach with {companion.capitalize()} and noted how to return at low tide."
            "Fern makes note of the reef and the height of the water at the cave mouth."
        "Wait with the voice until the tide carries it away.":
            $ empatia += 1
            $ day_summary = f"Fern reached the hidden beach with {companion.capitalize()} and stayed until the tide carried the voice away."
            "Fern stays at the edge of the water until the voice falls quiet."
    call return_home
    return
