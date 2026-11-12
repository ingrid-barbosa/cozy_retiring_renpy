label summer_02:
    scene bg summer_2
    with dissolve
    "Day 2 - Summer"
    "A strange shell glows near the sea in the shallow water."
    "As the water slips off the rock, the shell flashes twice. Fern remembers what Caelum said about the reef."
    show shell at discovery
    menu:
        "Reach into the crevice to pick up the shell.":
            $ coragem += 1
            $ day_summary = "Fern reached for the glowing shell and cut her hand on the rock. She wrapped the cut and went home."
            $ shell_cut = True
            "A wave pushes Fern's hand against the sharp rock. She pulls it free and wraps the cut in a cloth."
        "Watch when the shell lights up.":
            $ curiosidade += 1
            $ day_summary = "Fern watched the shell flash twice as the water receded. Something farther down the coast answered in the same rhythm."
            "Every time the water retreats, the shell pulses twice. The same two beats come back from farther down the coast."
        "Check whether anything is living inside.":
            $ empatia += 1
            $ day_summary = "Fern saw a creature sheltering inside the glowing shell and left it where it was."
            "Tiny legs curl out of the opening. Fern steps back and lets the creature keep its shelter."
        "Mark the spot and leave before the tide turns.":
            $ independencia += 1
            $ day_summary = "Fern marked the rocks near the glowing shell so she could return at low tide."
            "Fern stacks three stones above the waterline. She can find the spot again when the tide is lower."
    call return_home
    return
