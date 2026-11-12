label autumn_03:
    scene bg autumn_3
    with dissolve
    "Day 3 - Autumn"
    "Fern takes a different trail. The branches are so close together that she can only see a narrow strip of sky."
    if read_tree:
        "Fern remembers the turns carved into the white tree: left, right, left."
    "At the first fork, a pale root crosses the path to the left."
    menu:
        "Turn left beneath the white root.":
            pass
        "Turn right toward the open sky.":
            jump autumn_clear_trail
    "At the next fork, a pebble rolls down the path on the right. It strikes the ground with a hollow knock."
    menu:
        "Turn left where the earth is solid.":
            jump autumn_clear_trail
        "Turn right toward the hollow sound.":
            pass
    "At the last fork, two branches touch above the path to the left."
    menu:
        "Turn left under the branches.":
            pass
        "Turn right toward a clearing.":
            jump autumn_clear_trail
    $ coragem += 1
    $ visited_dark_autumn = True
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
        call rowan_introduction
    else:
        show caelum at speaker_right
        caelum "Fern! Step back. This magic is older than this forest. Follow my voice."
    call return_home
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
            fern "Someone should find out what it takes to keep that promise."
        "Record the story of the guardian and the white tree.":
            $ curiosidade += 1
            $ day_summary = f"Fern found the old seal and returned with {companion.capitalize()}. She recorded the story of the white tree and its guardian."
            fern "I'll write down how to recognize the path and why the roots matter."
        "Take the evening to think before making a promise.":
            $ independencia += 1
            $ day_summary = f"Fern found the old seal. {companion.capitalize()} brought her home, and she took the evening to think before making a promise."
            fern "I'd like to sit a while. I have enough to think about tonight."
    return

label autumn_clear_trail:
    $ independencia += 1
    $ day_summary = "Fern chose a turn that led to a clearing and found her way home before dark."
    "The trail opens into a patch of afternoon light. Fern finds her bearings and follows the clearing back toward home."
    call return_home
    return
