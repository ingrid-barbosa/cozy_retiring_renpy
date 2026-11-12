define fern = Character('Fern', show_dialogue_art="fern_box")
define caelum = Character('Caelum', show_dialogue_art="caelum_box")
define rowan = Character('Rowan', show_dialogue_art="rowan_box")
define mysterious = Character('???', show_dialogue_art="ui_box")

label rowan_introduction:
    if not met_rowan:
        rowan "My name is Rowan. I protect this part of the forest."
        fern "I'm Fern. Nice to meet you."
        $ met_rowan = True
    return
