label autumn_01:
    scene bg autumn_1
    with dissolve
    "Day 1 - Autumn"
    "A squirrel darts past Fern's cottage. She follows it into the orange forest, where leaves stir around her boots."
    "It pauses on a branch to watch her. The branch snaps, and the squirrel falls into the undergrowth."
    show squirrel at discovery
    with dissolve
    menu:
        "Check for injuries and wait until it recovers.":
            $ empatia += 1
            $ day_summary = "Fern followed a squirrel into the forest and waited nearby until it recovered from its fall."
            "Fern sits at a distance until the squirrel gets to its feet and slips between the roots."
        "Inspect the branch that broke.":
            $ curiosidade += 1
            $ day_summary = "After the squirrel fell, Fern examined the broken branch and found it dry inside."
            "The wood is dry inside, even though the tree is still full of leaves. Fern remembers the strange break."
        "Go down the steep bank to check where it landed.":
            $ coragem += 1
            $ day_summary = "Fern climbed down the steep bank to check where the squirrel had landed."
            "Fern catches hold of an exposed root and lowers herself down. The squirrel darts into a hollow."
        "Make a way back up the bank with a fallen branch.":
            $ independencia += 1
            $ day_summary = "Fern laid a branch across the loose soil so the squirrel could climb back up the bank."
            "Fern lays a branch across the loose soil. The squirrel uses it to scramble back to higher ground."
    call return_home
    return
