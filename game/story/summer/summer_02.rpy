label summer_02:
    scene bg summer_2
    with dissolve
    "Day 2 - Summer"
    fern "Yesterday I went out to learn the shape of the coast. Today I'm here because I wanted to see what the tide left behind."
    fern "I used to need a better reason than that. This morning it was enough to put on my boots."
    "A strange shell glows near the sea in the shallow water."
    "As the water slips off the rock, the shell flashes twice. Fern remembers what Caelum said about the reef."
    show shell at discovery
    menu:
        "Reach into the crevice to pick up the shell.":
            $ coragem += 1
            $ day_summary = "Fern reached for the glowing shell and cut her hand on the rock. She wrapped the cut and went home."
            $ unlock_choice_memory("summer_02:reach-into-the-crevice-to-pick-up-the-shell", "Summer - Day 2", day_summary)
            $ shell_cut = True
            "A wave pushes Fern's hand against the sharp rock. She pulls it free and wraps the cut in a cloth."
            fern "I was so busy watching the light that I forgot where I put my other hand. That'll be the part I remember tomorrow."
        "Watch when the shell lights up.":
            $ curiosidade += 1
            $ day_summary = "Fern watched the shell flash twice as the water receded. Something farther down the coast answered in the same rhythm."
            $ unlock_choice_memory("summer_02:watch-when-the-shell-lights-up", "Summer - Day 2", day_summary)
            "Every time the water retreats, the shell pulses twice. The same two beats come back from farther down the coast."
            fern "Two flashes from the shell. Two more, farther off. I wish I could tell where the second pair came from."
        "Check whether anything is living inside.":
            $ empatia += 1
            $ day_summary = "Fern saw a creature sheltering inside the glowing shell and left it where it was."
            $ unlock_choice_memory("summer_02:check-whether-anything-is-living-inside", "Summer - Day 2", day_summary)
            "Tiny legs curl out of the opening. Fern steps back and lets the creature keep its shelter."
            fern "The little legs looked for purchase even with my shadow over them. I'm glad I saw them before I reached in."
        "Mark the spot and leave before the tide turns.":
            $ independencia += 1
            $ day_summary = "Fern marked the rocks near the glowing shell so she could return at low tide."
            $ unlock_choice_memory("summer_02:mark-the-spot-and-leave-before-the-tide-turns", "Summer - Day 2", day_summary)
            "Fern stacks three stones above the waterline. She can find the spot again when the tide is lower."
            fern "The bottom stone is heavier than it looks. Next time I'll know where to stand before I look down."
    call return_home
    return
