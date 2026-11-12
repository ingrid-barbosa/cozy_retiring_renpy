label endings:
    call home_view
    show caelum at speaker_right
    caelum "Fern... before your new life truly begins, I want to ask you something."
    fern "What do you mean?"
    caelum "After everything you discovered, what path do you want to follow?"

    $ can_guard = empatia > 0 and (visited_dark_spring or visited_dark_autumn)
    $ can_explore = season != "autumn" and (coragem > 0 or curiosidade > 0 or found_amulet)
    $ can_collect = curiosidade > 0 and (visited_dark_summer or read_tree or visited_dark_autumn)
    $ directions = [("rest", independencia)]
    if can_guard:
        $ directions.append(("guard", empatia))
    if can_explore:
        $ directions.append(("explore", coragem))
    if can_collect:
        $ directions.append(("collect", curiosidade))
    $ suggested_ending = max(directions, key=lambda direction: direction[1])[0]

    if suggested_ending == "guard":
        fern "I keep thinking about what will happen to the forest if nobody goes back."
    elif suggested_ending == "explore":
        fern "I want to see where the trails lead when I have more than an afternoon."
    elif suggested_ending == "collect":
        fern "I'm already afraid I'll forget the stories I heard here."
    else:
        fern "I keep thinking about what it would feel like to wake up with the day to myself."

    menu:
        "Protect the forest on this side." if can_guard:
            "Ending — The Forest Guardian"
            if visited_dark_spring:
                "Fern meets Rowan at the edge of the meadow. They start with one tree whose roots still answer to spring."
            else:
                "Fern walks back to the white tree and begins learning how to care for the roots that hold the old seal."
            "At dusk, she goes home. She has decided what she can give the forest, and when to rest."
        "Keep exploring the world." if can_explore:
            "Ending — The Endless Journey"
            if found_amulet:
                "Fern tucks the silver amulet beside her map. Somewhere beyond the meadow, someone might recognize the leaf carved into it."
            elif season == "summer":
                "Fern studies the coast at low tide and marks the first headland she has yet to walk around."
            else:
                "Fern marks the farthest path she walked in the meadow, then leaves the rest of the map blank."
            "She packs for the morning, leaving her cottage key where she can find it when she comes home."
        "Collect the stories of this place." if can_collect:
            "Ending — The Keeper of Stories"
            if visited_dark_summer:
                "On the first page of a new book, Fern writes about a voice the sea borrowed for a night."
            elif read_tree:
                "On the first page, Fern copies the promise carved into the white tree."
            else:
                "On the first page, Fern records what she learned about the guardian who sealed the forest."
            "She leaves room beneath each story for the people who remember it differently."
        "Make a quiet life here.":
            "Ending — A Quiet Life"
            "Fern puts the kettle on and opens the cottage window. Outside, the last light settles over the path."
            "Tomorrow she can wake when she likes. For tonight, it is enough to know she is home."
    return
