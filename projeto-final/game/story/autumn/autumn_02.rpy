label autumn_02:
    scene bg autumn_2
    with dissolve
    "Day 2 - Autumn"
    fern "Before I learned to write a report, I learned to read marks left on trees. A nick low on a trunk could tell me where someone had stopped to eat."
    fern "I wonder what the keepers here thought was worth leaving for the next person."
    "The trees along the trail are crowded together, except for one. Its white trunk rises alone and towers above the others."
    "Fern remembers Caelum's carving. The bark has folded around the letters, leaving each line untouched."
    "Someone carved a line of symbols into the bark. Fern recognizes the old script the guardians used to leave messages for one another."
    menu:
        "Read the whole inscription and copy the directions.":
            $ curiosidade += 1
            $ day_summary = "Fern read the promise on the white tree and copied the directions carved beneath it."
            $ unlock_choice_memory("autumn_02:read-the-whole-inscription-and-copy-the-directions", "Autumn - Day 2", day_summary)
            call autumn_inscription from _call_autumn_inscription
            "Fern copies the three turns onto a scrap of paper."
            fern "I left a space below the directions on the page. If I go, I'll want to write down what the guardian could see when they stood there."
        "Read it aloud to remember whoever carved it.":
            $ empatia += 1
            $ day_summary = "Fern read the old guardian's promise aloud. Leaves fell from the white tree even though there was no wind."
            $ unlock_choice_memory("autumn_02:read-it-aloud-to-remember-whoever-carved-it", "Autumn - Day 2", day_summary)
            call autumn_inscription from _call_autumn_inscription_1
            "When Fern reads the last line aloud, leaves fall from the white branches, though there is no wind."
            fern "My voice sounded too loud after the last line. I stayed for a while to hear whether the woods would settle again."
        "Leave the writing alone and mark the path home.":
            $ independencia += 1
            $ day_summary = "Fern left the inscription unread and learned the bends in the trail on the way home."
            $ unlock_choice_memory("autumn_02:leave-the-writing-alone-and-mark-the-path-home", "Autumn - Day 2", day_summary)
            "Fern leaves the tree as she found it and learns the bends of the trail on the way back."
            fern "I can come back with better light if I want to read it. For now I can picture every bend between this tree and the door."
    call return_home from _call_return_home_1
    return

label autumn_inscription:
    $ read_tree = True
    "I sealed the old magic where the sun cannot reach it. I promised to come back and tend the roots that hold it."
    "From the first fork, take the left beneath the white root. Turn right where the ground sounds hollow, then left beneath the branches that touch."
    fern "Whoever wrote this meant to come back. I wonder what kept them."
    return
