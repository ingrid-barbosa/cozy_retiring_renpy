label spring_03:
    scene bg spring_3
    with dissolve
    "Day 3 - Spring"
    "Fern finds a narrow path beyond the meadow. She cannot see where it leads from here."
    menu:
        "Follow the path.":
            pass
        "Go home before it gets late.":
            $ independencia += 1
            $ day_summary = "Fern found a path beyond the meadow and decided to head home before nightfall."
            call return_home
            return
    "The flowers thin out. A break in the trees ahead looks like a fork."
    menu:
        "Continue to the fork.":
            pass
        "Turn back while the path is familiar.":
            $ independencia += 1
            $ day_summary = "Fern followed the path as far as the thinning flowers, then turned back while she knew the way."
            call return_home
            return
    menu:
        "Go left, toward the glint between the stones.":
            $ curiosidade += 1
            $ day_summary = "Fern took the left fork, found a silver amulet between the stones, and brought it home."
            $ found_amulet = True
            "Fern lifts a small amulet from between the stones. A leaf has been etched into its silver surface."
            "She pockets it and takes the trail home."
        "Go right, where the fallen leaves are hiding the trail.":
            $ coragem += 1
            $ visited_dark_spring = True
            scene bg dark_spring
            with dissolve
            "Dry leaves cover the ground. The trees are still standing, but Fern can feel their roots losing their magic."
            mysterious "Hey! What are you doing out here?"
            show rowan at rowan_portrait
            if met_rowan:
                fern "Rowan! I thought I was the only one out here."
            else:
                fern "I followed the trail. Who are you?"
                call rowan_introduction
            rowan "Easy. You're safe now. Step where I step and I'll take you back."
            call return_home
            show rowan at rowan_portrait
            rowan "That was the dead flower field. The roots used to carry spring from the meadow into the forest."
            rowan "Now the magic stops there. The trees beyond the field are dying faster than I can reach them."
            menu:
                "Offer to help tend the roots.":
                    $ empatia += 1
                    $ day_summary = "Fern followed the right fork into the dying forest. Rowan led her home, and she offered to help tend the roots."
                    fern "If you show me where the roots begin to fail, I can help you care for them."
                "Ask why the magic stopped moving.":
                    $ curiosidade += 1
                    $ day_summary = "Fern followed the right fork into the dying forest. Rowan led her home, and she asked why the magic had stopped."
                    fern "I'd like to know what changed. The flowers could tell us where it started."
                "Ask for time to think.":
                    $ independencia += 1
                    $ day_summary = "Fern followed the right fork into the dying forest. Rowan led her home, and she asked for time to think."
                    fern "I need to think about what I can promise."
            return
    call return_home
    return
