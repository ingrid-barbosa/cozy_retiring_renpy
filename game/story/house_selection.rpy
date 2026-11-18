define home_memory_titles = {
    ("spring", "yellow"): "A sunny place beneath the flowers.",
    ("spring", "blue"): "A patch of sky among the blossoms.",
    ("spring", "red"): "A red door at the edge of the meadow.",
    ("summer", "yellow"): "A little sunlight by the sea.",
    ("summer", "blue"): "A blue door above the tide.",
    ("summer", "red"): "An ember on the shore.",
    ("autumn", "yellow"): "A golden roof beneath the leaves.",
    ("autumn", "blue"): "A quiet blue among the copper trees.",
    ("autumn", "red"): "A red cottage in the falling leaves.",
}

define home_memory_locations = {
    "spring": "the Eternal Meadow",
    "summer": "the Northern Coast",
    "autumn": "the Old Forest",
}

label house_selection:
    call location_tour
    menu (prompt="Where would I like to settle?"):
        "The Eternal Meadow — Spring":
            $ season = "spring"
        "The Northern Coast — Summer":
            $ season = "summer"
        "The Old Forest — Autumn":
            $ season = "autumn"
    $ play_season_soundtrack(season)
    call home_view
    show caelum at speaker_right
    menu (prompt="Which cottage feels like mine?"):
        "The yellow cottage":
            $ house_color = "yellow"
        "The blue cottage":
            $ house_color = "blue"
        "The red cottage":
            $ house_color = "red"
    call home_view
    show caelum at speaker_right
    menu (prompt="Am I ready to call this place home?"):
        "Make this my new home":
            $ unlock_choice_memory("home:{}:{}".format(season, house_color), home_memory_titles[(season, house_color)], "Fern made the {} cottage in {} her new home.".format(house_color, home_memory_locations[season]))
        "Look at the locations and cottages again":
            $ house_color = None
            $ stop_story_soundtrack()
            jump house_selection
    caelum "The key is yours, Fern. Come find me if you need anything."
    fern "Thank you, Caelum. I think I'll stay and watch the light change."
    return

label location_tour:
    scene bg home_spring
    show caelum at speaker_right
    with dissolve
    caelum "I've found three places where you could settle. This is the first: the Eternal Meadow."
    caelum "It's always spring here. The flowers never truly disappear, and every one carries a little magic from the forest spirits."
    fern "That explains why the entire field feels alive."
    caelum "I used to follow the butterflies all the way to the woods. Lately, they turn back at the same bend."
    fern "Do you know why?"
    caelum "I thought it was the wind. They turn back on still days, too."

    scene bg home_summer
    show caelum at speaker_right
    with dissolve
    caelum "This is the Northern Coast. Here, summer lingers, and you can hear the sea from your doorstep."
    caelum "After dark, the waves glow with the light of the ancient spirits that live beneath them."
    fern "Then I suppose I would have some interesting neighbors."
    caelum "Sometimes, just as the tide goes out, you'll hear two notes from beyond the reef. I hear them best on nights when there isn't a boat in sight."

    scene bg home_autumn
    show caelum at speaker_right
    with dissolve
    caelum "And this is the Old Forest. The leaves turn gold here, but the woods never fall completely bare."
    caelum "These trees remember everything that happens here. Every traveler, every spirit, every promise."
    caelum "There's a white tree up the trail. I saw an old carving on it once. When I passed it again years later, the rest of the bark had grown around it."
    fern "What did it say?"
    caelum "I couldn't read the hand. You might recognize it."
    return

label home_view:
    scene expression ("bg home_" + season)
    if house_color:
        show expression ("house " + house_color) as cottage at cottage_position
    with dissolve
    return

label return_home:
    $ play_day_soundtrack()
    call home_view
    "Fern returns to her cottage."
    return
