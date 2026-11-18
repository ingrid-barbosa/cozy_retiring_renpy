label autumn_01:
    scene bg autumn_1
    with dissolve
    "Day 1 - Autumn"
    fern "I used to cross the same stretch of forest every morning. By the end, I could do it without looking at the trees."
    fern "I came out today to look properly. So far I've spent ten minutes watching somebody bury a nut."
    "A squirrel darts past Fern's cottage. She follows it into the orange forest, where leaves stir around her boots."
    "It pauses on a branch to watch her. The branch snaps, and the squirrel falls into the undergrowth."
    show squirrel at discovery
    with dissolve
    menu:
        "Check for injuries and wait until it recovers.":
            $ empatia += 1
            $ day_summary = "Fern followed a squirrel into the forest and waited nearby until it recovered from its fall."
            $ unlock_choice_memory("autumn_01:check-for-injuries-and-wait-until-it-recovers", "Autumn - Day 1", day_summary)
            "Fern sits at a distance until the squirrel gets to its feet and slips between the roots."
            fern "The hardest part was staying still once I knew it could get up. It had every reason to want me a little farther away."
        "Inspect the branch that broke.":
            $ curiosidade += 1
            $ day_summary = "After the squirrel fell, Fern examined the broken branch and found it dry inside."
            $ unlock_choice_memory("autumn_01:inspect-the-branch-that-broke", "Autumn - Day 1", day_summary)
            "The wood is dry inside, even though the tree is still full of leaves. Fern remembers the strange break."
            fern "The branch looked healthy from the trail. I'll remember how light it felt once I picked it up."
        "Go down the steep bank to check where it landed.":
            $ coragem += 1
            $ day_summary = "Fern climbed down the steep bank to check where the squirrel had landed."
            $ unlock_choice_memory("autumn_01:go-down-the-steep-bank-to-check-where-it-landed", "Autumn - Day 1", day_summary)
            "Fern catches hold of an exposed root and lowers herself down. The squirrel darts into a hollow."
            fern "I know the easiest way down a bank and I still managed to get soil all the way up one sleeve. It's been a while since I laughed at myself on a walk."
        "Make a way back up the bank with a fallen branch.":
            $ independencia += 1
            $ day_summary = "Fern laid a branch across the loose soil so the squirrel could climb back up the bank."
            $ unlock_choice_memory("autumn_01:make-a-way-back-up-the-bank-with-a-fallen-branch", "Autumn - Day 1", day_summary)
            "Fern lays a branch across the loose soil. The squirrel uses it to scramble back to higher ground."
            fern "I watched it choose a different branch on the way up. From where I was standing, its way made more sense."
    call return_home
    return
