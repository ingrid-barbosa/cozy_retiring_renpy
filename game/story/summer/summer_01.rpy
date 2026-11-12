label summer_01:
    scene bg summer_1
    with dissolve
    "Day 1 - Summer"
    "Fern explores the coast near her new cottage. Between two rocks, a turtle is lying upside down."
    show turtle at discovery
    with dissolve
    menu:
        "Gently turn it over and stay until it starts moving.":
            $ empatia += 1
            $ day_summary = "Fern turned over the stranded turtle and waited until it swam away."
            "The turtle rests a moment, then paddles out into the shallow water."
        "Look for the gap it fell through and clear a way out.":
            $ curiosidade += 1
            $ day_summary = "Fern cleared stones from the groove where the turtle had fallen and helped it back to the sea."
            "Fern spots a groove in the rock. She removes the loose stones and helps the turtle back to the water."
        "Cross the wet rocks to reach it before the next wave.":
            $ coragem += 1
            $ day_summary = "Fern crossed the wet rocks and turned the turtle over before the next wave."
            "Fern steadies herself against the rock and turns the turtle over just as the spray reaches her boots."
        "Use a piece of driftwood to give it a foothold.":
            $ independencia += 1
            $ day_summary = "Fern used driftwood to give the stranded turtle a foothold."
            "Fern slides the driftwood under the edge of the shell. The turtle pushes against it until it rolls upright."
    call return_home
    return
