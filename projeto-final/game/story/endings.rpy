label endings:
    call home_view from _call_home_view
    fern "I've started leaving the key on the windowsill. The first night I kept it in my pocket, even after I'd locked the door."
    fern "I used to fall asleep going over the places I hadn't reached. Tonight I can give myself a little time to think about the ones I did."
    call ending_day_recap from _call_ending_day_recap
    call ending_reflection from _call_ending_reflection
    show caelum at speaker_right
    with dissolve
    caelum "You left the lamp on. I thought you might still be awake."
    fern "I was trying to decide what I'd do tomorrow. Somehow I ended up planning the next hundred years."
    caelum "Start with tomorrow, then. What would you like to wake up and do?"
    hide caelum
    fern "I know what I would have said before I came here. I would have named whatever needed doing first."
    fern "Let me think about what I'd put my boots on for, if the whole morning were mine."

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
        fern "I keep picturing the first tree I'd check. I could start there and tell someone when I mean to be home."
    elif suggested_ending == "explore":
        fern "I'd like to take a path far enough that I have to stop and eat the lunch I packed."
    elif suggested_ending == "collect":
        fern "The details are starting to change in my head. I could sit down with a blank page while I still remember the order of things."
    else:
        fern "I'd like to open the shutters and decide after I've had my tea. I've spent years promising myself that morning."

    menu:
        "Protect the forest on this side." if can_guard:
            $ unlock_choice_memory("endings:protect-the-forest-on-this-side", "Fern's next chapter", "Protect the forest on this side.")
            fern "I want to go back. The first thing I'll do is ask who can share the work."
            "Ending — The Forest Guardian"
            if visited_dark_spring:
                "Fern meets Rowan at the edge of the meadow. They start with one tree whose roots still answer to spring."
            else:
                "Fern walks back to the white tree and begins learning how to care for the roots that hold the old seal."
            "At dusk, she goes home. She has decided what she can give the forest, and when to rest."
        "Keep exploring the world." if can_explore:
            $ unlock_choice_memory("endings:keep-exploring-the-world", "Fern's next chapter", "Keep exploring the world.")
            fern "I'll pack enough for a day away. If I want another day, I'll decide when I get there."
            "Ending — The Endless Journey"
            if found_amulet:
                "Fern tucks the silver amulet beside her map. Somewhere beyond the meadow, someone might recognize the leaf carved into it."
            elif season == "summer":
                "Fern studies the coast at low tide and marks the first headland she has yet to walk around."
            else:
                "Fern marks the farthest path she walked in the meadow, then leaves the rest of the map blank."
            "She packs for the morning, leaving her cottage key where she can find it when she comes home."
        "Collect the stories of this place." if can_collect:
            $ unlock_choice_memory("endings:collect-the-stories-of-this-place", "Fern's next chapter", "Collect the stories of this place.")
            fern "I'll start with the parts I heard myself. The rest can wait until I've spoken to the people who know them."
            "Ending — The Keeper of Stories"
            if visited_dark_summer:
                "On the first page of a new book, Fern writes about a voice the sea borrowed for a night."
            elif read_tree:
                "On the first page, Fern copies the promise carved into the white tree."
            else:
                "On the first page, Fern records what she learned about the guardian who sealed the forest."
            "She leaves room beneath each story for the people who remember it differently."
        "Make a quiet life here.":
            $ unlock_choice_memory("endings:make-a-quiet-life-here", "Fern's next chapter", "Make a quiet life here.")
            fern "I think I'll stay in tomorrow. There's a chair by the window I haven't once sat in."
            "Ending — A Quiet Life"
            "Fern puts the kettle on and opens the cottage window. Outside, the last light settles over the path."
            "Tomorrow she can wake when she likes. For tonight, it is enough to know she is home."
    return

label ending_reflection:
    # As lembranças de mistério usam só o cenário, sem sprites.
    if visited_dark_spring:
        $ play_mystery_soundtrack()
        scene bg dark_spring
        with dissolve
        fern "I remember the leaves giving way under my boots. I could still see green overhead, so it took me a moment to understand what I was standing on."
        fern "Rowan knew exactly where to put his feet on the way out. I wonder how many times he's had to make that walk."
        if mystery_response == "tend":
            fern "I offered to help with the roots. Tomorrow I'll ask where he wants me to start, and tell him how long I can stay."
        elif mystery_response == "investigate":
            fern "I asked him how it started. I keep thinking about the butterflies turning back while the rest of us kept walking."
        elif mystery_response == "wait":
            fern "I asked for time to think. For once, I want to be able to keep whatever promise I make."
    elif visited_dark_summer:
        $ play_mystery_soundtrack()
        scene bg dark_summer
        with dissolve
        fern "In my head, the water still lights up all the way to the rocks. I remember the voice much less clearly. Every time I try to hear it again, it sounds a little more like someone I used to know."
        if shell_cut:
            fern "The salt stung my hand when we went through the cave. I remember that part plainly enough."
        if mystery_response == "record":
            fern "I tried to bring the words home exactly as I heard them. I'll write down what I'm sure of and leave a space where the water drowned the rest."
        elif mystery_response == "return":
            fern "I asked how to come back at low tide. I think I'd like to see the beach in daylight before I decide how much of it I understood."
        elif mystery_response == "listen":
            fern "I stayed until the voice went quiet. I'm glad I gave it that time, even if the sea never brings it back."
    elif visited_dark_autumn:
        $ play_mystery_soundtrack()
        scene bg dark_autumn
        with dissolve
        if read_tree:
            fern "I'd already read the directions on the white tree. Down among the roots, I kept thinking about the person who took the trouble to leave them."
        else:
            fern "I walked past the inscription without reading it. I only learned what the white roots were holding after we found our way out."
        fern "I remember how ordinary the air felt when we reached the clearing. I wanted to keep breathing it for a while."
        if mystery_response == "tend":
            fern "I asked what keeps the roots alive. I want to know whether there are ways to tend them that someone else could learn, too."
        elif mystery_response == "record":
            fern "I wanted to write down the guardian's promise. I'd put the way out on the same page as the way in."
        elif mystery_response == "wait":
            fern "I gave myself the evening to think. The guardian's promise has waited a long time. I can afford to read it twice before adding my own."
    else:
        call home_view from _call_home_view_1
        if found_amulet:
            fern "I put the amulet by the window. The leaf catches the light there. I'd like to find out who wore it before me."
        elif season == "spring" and met_rowan:
            fern "I know who lives beyond the meadow now. Next time I take that path, I could knock simply to say hello."
        elif season == "summer":
            fern "I heard enough from the beach. On the way home I kept listening for those notes. The farther I got from the water, the more I noticed my own footsteps."
        elif read_tree:
            fern "I read what the guardian left on the white tree. I can still picture the first few words. I'd like to go back in the morning and take my time over them."
        else:
            fern "I can find my way home from a little farther out than I could yesterday. I think that's enough ground to have covered for now."
        fern "It might take a few more evenings before I stop expecting someone to knock and ask where I've been."
        return

    $ play_day_soundtrack(with_ambience=False)
    call home_view from _call_home_view_2
    fern "The cottage is warm. I can sit here a little longer before I have to put any of that into words."
    return
