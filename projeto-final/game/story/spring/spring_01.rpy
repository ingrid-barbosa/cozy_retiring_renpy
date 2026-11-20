label spring_01:
    scene bg spring_1
    with dissolve
    "Day 1 - Spring"
    fern "Three hundred years, and I still wake up listening for the southern woods."
    fern "The meadow has its own sounds. If I sit here long enough, perhaps I'll learn which ones mean I can go back to sleep."
    "Fern walks through the grass fields until she reaches a hill overlooking the sea."
    "Butterflies follow her, as if sensing the magic she once used to protect the forest."
    "At a bend in the path, the butterflies drift back toward the meadow. Fern holds out a hand. The air is still."
    "Something stirs between the bushes. A small bird is on the ground, holding one wing close."
    show bird at discovery
    with dissolve
    menu (prompt="What should Fern do?"):
        "Sit beside it and tend to its wing.":
            $ empatia += 1
            $ day_summary = "On the hill above the sea, Fern found an injured bird and wrapped its wing."
            $ unlock_choice_memory("spring_01:sit-beside-it-and-tend-to-its-wing", "Spring - Day 1", day_summary)
            "Fern waits for the bird to stop trembling before wrapping its wing in a strip of soft cloth."
            fern "The bird stopped trembling before I did. I hadn't noticed how hard I was holding my own hands together."
        "Look for what knocked it from its nest.":
            $ curiosidade += 1
            $ day_summary = "Fern traced the bird's fall to a broken branch and moved it somewhere safer."
            $ unlock_choice_memory("spring_01:look-for-what-knocked-it-from-its-nest", "Spring - Day 1", day_summary)
            "Fern finds a broken branch and carries the bird away from the branches still swaying overhead."
            fern "I can spend all morning finding out why a branch broke. The bird needed somewhere dry before it needed my answer."
        "Climb the slope to reach its sheltered nest.":
            $ coragem += 1
            $ day_summary = "Fern climbed the steep slope to return the injured bird to its nest."
            $ unlock_choice_memory("spring_01:climb-the-slope-to-reach-its-sheltered-nest", "Spring - Day 1", day_summary)
            "Fern takes the steep path one careful step at a time and settles the bird into its nest."
            fern "Halfway up, I thought about calling for help. I wonder why I still find that more frightening than the climb."
        "Make a shelter with the materials at hand.":
            $ independencia += 1
            $ day_summary = "Fern built a shelter out of leaves and twigs for the injured bird."
            $ unlock_choice_memory("spring_01:make-a-shelter-with-the-materials-at-hand", "Spring - Day 1", day_summary)
            "Fern folds broad leaves beneath the bush and props them up with twigs. The bird shuffles into the shade."
            fern "There. It can get out whenever it wants. I wish I'd thought to make my own shelters with such an obvious way out."
    call return_home from _call_return_home_4
    return
