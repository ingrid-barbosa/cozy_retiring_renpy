init python:
    renpy.music.register_channel("dialogue_blip", mixer="sfx", loop=True)

    def play_dialogue_blip(event, interact=True, fixed_text_speed=False, **kwargs):
        if event in ("slow_done", "interact_done", "end"):
            renpy.music.stop(channel="dialogue_blip", fadeout=0)
        elif event == "show_done" and interact and (fixed_text_speed or preferences.text_cps > 0) and not renpy.is_skipping():
            filename = "musics/effects/text_blip.mp3"
            if renpy.loadable(filename):
                renpy.music.play(filename, channel="dialogue_blip", loop=True,
                                 fadeout=0, relative_volume=2.0)

    config.all_character_callbacks.append(play_dialogue_blip)

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
