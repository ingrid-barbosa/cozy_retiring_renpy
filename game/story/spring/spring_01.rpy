label spring_01:
    scene bg spring_1
    with dissolve
    "Day 1 - Spring"
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
            "Fern waits for the bird to stop trembling before wrapping its wing in a strip of soft cloth."
        "Look for what knocked it from its nest.":
            $ curiosidade += 1
            $ day_summary = "Fern traced the bird's fall to a broken branch and moved it somewhere safer."
            "Fern finds a broken branch and carries the bird away from the branches still swaying overhead."
        "Climb the slope to reach its sheltered nest.":
            $ coragem += 1
            $ day_summary = "Fern climbed the steep slope to return the injured bird to its nest."
            "Fern takes the steep path one careful step at a time and settles the bird into its nest."
        "Make a shelter with the materials at hand.":
            $ independencia += 1
            $ day_summary = "Fern built a shelter out of leaves and twigs for the injured bird."
            "Fern folds broad leaves beneath the bush and props them up with twigs. The bird shuffles into the shade."
    call return_home
    return
