label spring_03:
    scene bg spring_3
    with dissolve
    "Day 3 - Spring"
    fern "The first morning, I thought I'd know I was retired when I stopped looking for trouble."
    fern "This morning I caught myself looking forward to the walk. I wonder how far I'd go if nobody was counting on me to finish it."
    "Fern finds a narrow path beyond the meadow. She cannot see where it leads from here."
    menu:
        "Follow the path.":
            $ unlock_choice_memory("spring_03:follow-the-path", "Spring - Day 3", "Follow the path.")
        "Go home before it gets late.":
            $ independencia += 1
            $ day_summary = "Fern found a path beyond the meadow and decided to head home before nightfall."
            $ unlock_choice_memory("spring_03:go-home-before-it-gets-late", "Spring - Day 3", day_summary)
            fern "I could be back before the kettle cools. A trail can still be interesting tomorrow."
            call return_home
            return
    "The flowers thin out. A break in the trees ahead looks like a fork."
    menu:
        "Continue to the fork.":
            $ unlock_choice_memory("spring_03:continue-to-the-fork", "Spring - Day 3", "Continue to the fork.")
        "Turn back while the path is familiar.":
            $ independencia += 1
            $ day_summary = "Fern followed the path as far as the thinning flowers, then turned back while she knew the way."
            $ unlock_choice_memory("spring_03:turn-back-while-the-path-is-familiar", "Spring - Day 3", day_summary)
            fern "I wanted another look at the flowers. I'll remember the point where even the yellow ones gave out."
            call return_home
            return
    menu:
        "Go left, toward the glint between the stones.":
            $ curiosidade += 1
            $ day_summary = "Fern took the left fork, found a silver amulet between the stones, and brought it home."
            $ unlock_choice_memory("spring_03:go-left-toward-the-glint-between-the-stones", "Spring - Day 3", day_summary)
            $ found_amulet = True
            "Fern lifts a small amulet from between the stones. A leaf has been etched into its silver surface."
            "She pockets it and takes the trail home."
            fern "The leaf on the silver is worn smooth at the tip. Someone used to rub it the way I'm rubbing it now."
        "Go right, where the fallen leaves are hiding the trail.":
            $ unlock_choice_memory("spring_03:go-right-where-the-fallen-leaves-are-hiding-the-trail", "Spring - Day 3", "Go right, where the fallen leaves are hiding the trail.")
            $ coragem += 1
            $ visited_dark_spring = True
            $ play_mystery_soundtrack()
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
                    $ unlock_choice_memory("spring_03:offer-to-help-tend-the-roots", "Spring - Day 3", day_summary)
                    $ mystery_response = "tend"
                    fern "If you show me where the roots begin to fail, I can help you care for them."
                    fern "My offer came out before I'd thought about what it would cost. When I picture tomorrow, I think I can give him the morning."
                "Ask why the magic stopped moving.":
                    $ curiosidade += 1
                    $ day_summary = "Fern followed the right fork into the dying forest. Rowan led her home, and she asked why the magic had stopped."
                    $ unlock_choice_memory("spring_03:ask-why-the-magic-stopped-moving", "Spring - Day 3", day_summary)
                    $ mystery_response = "investigate"
                    fern "I'd like to know what changed. The flowers could tell us where it started."
                    fern "If I can find where the roots first went dry, perhaps I'll know where to start looking for an answer."
                "Ask for time to think.":
                    $ independencia += 1
                    $ day_summary = "Fern followed the right fork into the dying forest. Rowan led her home, and she asked for time to think."
                    $ unlock_choice_memory("spring_03:ask-for-time-to-think", "Spring - Day 3", day_summary)
                    $ mystery_response = "wait"
                    fern "I need to think about what I can promise."
                    fern "Rowan waited while I thought. I'm glad he let me leave the question open."
            return
    call return_home
    return
