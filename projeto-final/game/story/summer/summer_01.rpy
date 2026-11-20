label summer_01:
    scene bg summer_1
    with dissolve
    "Day 1 - Summer"
    fern "Back south, I could tell how hard it had rained by the smell of the river. At this shore, I can't even tell which rocks will be dry in an hour."
    fern "I think I'd like to be a beginner at something for a while."
    "Fern explores the coast near her new cottage. Between two rocks, a turtle is lying upside down."
    show turtle at discovery
    with dissolve
    menu:
        "Gently turn it over and stay until it starts moving.":
            $ empatia += 1
            $ day_summary = "Fern turned over the stranded turtle and waited until it swam away."
            $ unlock_choice_memory("summer_01:gently-turn-it-over-and-stay-until-it-starts-moving", "Summer - Day 1", day_summary)
            "The turtle rests a moment, then paddles out into the shallow water."
            fern "There was a moment when its feet hung uselessly in the air. I kept thinking how little effort it took, from where I was standing, to make the ground reachable again."
        "Look for the gap it fell through and clear a way out.":
            $ curiosidade += 1
            $ day_summary = "Fern cleared stones from the groove where the turtle had fallen and helped it back to the sea."
            $ unlock_choice_memory("summer_01:look-for-the-gap-it-fell-through-and-clear-a-way-out", "Summer - Day 1", day_summary)
            "Fern spots a groove in the rock. She removes the loose stones and helps the turtle back to the water."
            fern "I could see the route from above. From the waterline, every lip of rock must have looked like the end of it."
        "Cross the wet rocks to reach it before the next wave.":
            $ coragem += 1
            $ day_summary = "Fern crossed the wet rocks and turned the turtle over before the next wave."
            $ unlock_choice_memory("summer_01:cross-the-wet-rocks-to-reach-it-before-the-next-wave", "Summer - Day 1", day_summary)
            "Fern steadies herself against the rock and turns the turtle over just as the spray reaches her boots."
            fern "The wave soaked me clear through. Now that the turtle is gone, I can admit I'd been scared of slipping."
        "Use a piece of driftwood to give it a foothold.":
            $ independencia += 1
            $ day_summary = "Fern used driftwood to give the stranded turtle a foothold."
            $ unlock_choice_memory("summer_01:use-a-piece-of-driftwood-to-give-it-a-foothold", "Summer - Day 1", day_summary)
            "Fern slides the driftwood under the edge of the shell. The turtle pushes against it until it rolls upright."
            fern "I took the driftwood back out of the pool. Something else will find a use for it after the next tide."
    call return_home from _call_return_home_10
    return
