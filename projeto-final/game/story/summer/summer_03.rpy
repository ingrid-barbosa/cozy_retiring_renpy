label summer_03:
    scene bg summer_3 at moonlight
    with dissolve
    "Day 3 - Summer"
    fern "The cottage was quiet tonight. I left the kettle full and walked down to the water before I could talk myself into staying in."
    fern "By daylight, I'd have picked out a landmark to guide me home. Tonight I keep turning to look at my own window."
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
            $ unlock_choice_memory("summer_03:follow-the-sound-through-the-cave-together", "Summer - Day 3", "Follow the sound through the cave together.")
            $ coragem += 1
            $ visited_dark_summer = True
        "Listen from the beach, then go home.":
            $ independencia += 1
            $ day_summary = f"Fern heard two notes by the reef with {companion.capitalize()}. She listened from the beach until they faded, then went home."
            $ unlock_choice_memory("summer_03:listen-from-the-beach-then-go-home", "Summer - Day 3", day_summary)
            "Fern listens until the notes fade into the tide."
            call return_home
            fern "I walked all the way home with those two notes in my head. By the time I reached the door, I could hum them without stopping to think."
            return
    $ play_mystery_soundtrack()
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
            $ unlock_choice_memory("summer_03:remember-the-voice-and-write-down-what-it-said", "Summer - Day 3", day_summary)
            $ mystery_response = "record"
            "Fern repeats the words softly so she can put them on paper at home."
            fern "I hope I get the words right. I could write down where I was standing and leave a blank for the part I couldn't hear."
        "Ask how to return when the tide is low.":
            $ independencia += 1
            $ day_summary = f"Fern reached the hidden beach with {companion.capitalize()} and noted how to return at low tide."
            $ unlock_choice_memory("summer_03:ask-how-to-return-when-the-tide-is-low", "Summer - Day 3", day_summary)
            $ mystery_response = "return"
            "Fern makes note of the reef and the height of the water at the cave mouth."
            fern "The water's up to the second notch now. I'd like to see what the cave looks like when the lowest one is dry."
        "Wait with the voice until the tide carries it away.":
            $ empatia += 1
            $ day_summary = f"Fern reached the hidden beach with {companion.capitalize()} and stayed until the tide carried the voice away."
            $ unlock_choice_memory("summer_03:wait-with-the-voice-until-the-tide-carries-it-away", "Summer - Day 3", day_summary)
            $ mystery_response = "listen"
            "Fern stays at the edge of the water until the voice falls quiet."
            fern "I kept expecting the voice to ask something of us. Once I stopped waiting for that, I heard how tired it sounded."
    call return_home
    return
