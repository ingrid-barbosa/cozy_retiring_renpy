label autumn_02:
    scene bg autumn_2
    with dissolve
    "Day 2 - Autumn"
    "The trees along the trail are crowded together, except for one. Its white trunk rises alone and towers above the others."
    "Fern remembers Caelum's carving. The bark has folded around the letters, leaving each line untouched."
    "Someone carved a line of symbols into the bark. Fern recognizes the old script the guardians used to leave messages for one another."
    menu:
        "Read the whole inscription and copy the directions.":
            $ curiosidade += 1
            $ day_summary = "Fern read the promise on the white tree and copied the directions carved beneath it."
            call autumn_inscription
            "Fern copies the three turns onto a scrap of paper."
        "Read it aloud to remember whoever carved it.":
            $ empatia += 1
            $ day_summary = "Fern read the old guardian's promise aloud. Leaves fell from the white tree even though there was no wind."
            call autumn_inscription
            "When Fern reads the last line aloud, leaves fall from the white branches, though there is no wind."
        "Leave the writing alone and mark the path home.":
            $ independencia += 1
            $ day_summary = "Fern left the inscription unread and learned the bends in the trail on the way home."
            "Fern leaves the tree as she found it and learns the bends of the trail on the way back."
    call return_home
    return

label autumn_inscription:
    $ read_tree = True
    "I sealed the old magic where the sun cannot reach it. I promised to come back and tend the roots that hold it."
    "From the first fork, take the left beneath the white root. Turn right where the ground sounds hollow, then left beneath the branches that touch."
    fern "Whoever wrote this meant to come back. I wonder what kept them."
    return
