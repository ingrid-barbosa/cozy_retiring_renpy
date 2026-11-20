label autumn_03:
    scene bg autumn_3
    with dissolve
    "Day 3 - Autumn"
    fern "I used to be the one who told people which paths to avoid after dark. Now I have to judge by the light and the ground under my boots."
    fern "If I lose my bearings, I can turn back. Nobody at home is waiting for me to draw the rest of the map."
    "Fern takes a different trail. The branches are so close together that she can only see a narrow strip of sky."
    if read_tree:
        "Fern remembers the turns carved into the white tree: left, right, left."
    "At the first fork, a pale root crosses the path to the left."
    menu:
        "Turn left beneath the white root.":
            $ unlock_choice_memory("autumn_03:turn-left-beneath-the-white-root", "Autumn - Day 3", "Turn left beneath the white root.")
        "Turn right toward the open sky.":
            $ unlock_choice_memory("autumn_03:turn-right-toward-the-open-sky", "Autumn - Day 3", "Turn right toward the open sky.")
            jump autumn_clear_trail
    "At the next fork, a pebble rolls down the path on the right. It strikes the ground with a hollow knock."
    menu:
        "Turn left where the earth is solid.":
            $ unlock_choice_memory("autumn_03:turn-left-where-the-earth-is-solid", "Autumn - Day 3", "Turn left where the earth is solid.")
            jump autumn_clear_trail
        "Turn right toward the hollow sound.":
            $ unlock_choice_memory("autumn_03:turn-right-toward-the-hollow-sound", "Autumn - Day 3", "Turn right toward the hollow sound.")
    "At the last fork, two branches touch above the path to the left."
    menu:
        "Turn left under the branches.":
            $ unlock_choice_memory("autumn_03:turn-left-under-the-branches", "Autumn - Day 3", "Turn left under the branches.")
        "Turn right toward a clearing.":
            $ unlock_choice_memory("autumn_03:turn-right-toward-a-clearing", "Autumn - Day 3", "Turn right toward a clearing.")
            jump autumn_clear_trail
    $ coragem += 1
    $ visited_dark_autumn = True
    $ play_mystery_soundtrack()
    scene bg dark_autumn
    with dissolve
    "No sunlight reaches the forest floor. In the dark, Fern can just make out white roots around her feet."
    if read_tree:
        fern "The old guardian sealed the magic here. These must be the roots she promised to tend."
    else:
        fern "These roots are as pale as that tree I saw yesterday. How far have they grown?"
    $ companion = renpy.random.choice(("rowan", "caelum"))
    if companion == "rowan":
        show rowan at rowan_portrait
        rowan "Stop. Put your foot where mine is and follow me out."
        call rowan_introduction from _call_rowan_introduction
    else:
        show caelum at speaker_right
        caelum "Fern! Step back. This magic is older than this forest. Follow my voice."
    call return_home from _call_return_home_2
    if companion == "rowan":
        show rowan at rowan_portrait
        rowan "The white tree holds the seal. Its roots have been doing that work alone for longer than anyone remembers."
    else:
        show caelum at speaker_right
        caelum "Long ago, another guardian sealed this energy here. It was not evil... but it became forgotten."
    if read_tree:
        fern "I read her promise in the bark. She wanted someone to remember the way back."
    else:
        fern "I saw marks on the white tree yesterday."
        "Her companion explains that the guardian carved her promise there, along with directions to the roots that hold the seal."
    menu:
        "Ask what the roots need to stay alive.":
            $ empatia += 1
            $ day_summary = f"Fern found the roots of the old seal. {companion.capitalize()} led her home, and she asked what the roots needed to stay alive."
            $ unlock_choice_memory("autumn_03:ask-what-the-roots-need-to-stay-alive", "Autumn - Day 3", day_summary)
            $ mystery_response = "tend"
            fern "Someone should find out what it takes to keep that promise."
            fern "I heard myself ask how often the roots should be checked. I hope there's someone else who can take a turn when I can't."
        "Record the story of the guardian and the white tree.":
            $ curiosidade += 1
            $ day_summary = f"Fern found the old seal and returned with {companion.capitalize()}. She recorded the story of the white tree and its guardian."
            $ unlock_choice_memory("autumn_03:record-the-story-of-the-guardian-and-the-white-tree", "Autumn - Day 3", day_summary)
            $ mystery_response = "record"
            fern "I'll write down how to recognize the path and why the roots matter."
            fern "The guardian left such exact directions. I keep wondering who they imagined would be reading them."
        "Take the evening to think before making a promise.":
            $ independencia += 1
            $ day_summary = f"Fern found the old seal. {companion.capitalize()} brought her home, and she took the evening to think before making a promise."
            $ unlock_choice_memory("autumn_03:take-the-evening-to-think-before-making-a-promise", "Autumn - Day 3", day_summary)
            $ mystery_response = "wait"
            fern "I'd like to sit a while. I have enough to think about tonight."
            fern "I'd like to know how long I've got before the seal changes again. Tonight I can give that question a place to sit."
    return

label autumn_clear_trail:
    $ independencia += 1
    $ day_summary = "Fern chose a turn that led to a clearing and found her way home before dark."
    "The trail opens into a patch of afternoon light. Fern finds her bearings and follows the clearing back toward home."
    fern "The relief came as soon as I saw the sky. I stood in the clearing until I felt ready to walk again."
    call return_home from _call_return_home_3
    return
