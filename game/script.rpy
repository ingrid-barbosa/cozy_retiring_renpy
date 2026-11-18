label start:
    $ cozy_jamendo_ambience.update()
    call prologue
    call house_selection
    $ play_day_soundtrack()
    if season == "spring":
        call spring_01
        call day_passed(1)
        call spring_02
        call day_passed(2)
        call spring_03
    elif season == "summer":
        call summer_01
        call day_passed(1)
        call summer_02
        call day_passed(2)
        call summer_03
    else:
        call autumn_01
        call day_passed(1)
        call autumn_02
        call day_passed(2)
        call autumn_03
    call day_passed(3)
    stop ambience fadeout 0.5
    call endings
    scene black
    with fade
    $ final_story_texts = final_story_paragraphs()
    $ final_story_index = 0
    while final_story_index < len(final_story_texts):
        $ final_story_current = final_story_texts[final_story_index]
        final_story_narrator "[final_story_current]"
        $ final_story_index += 1
    call screen cozy_final_story
    $ jamendo_ambience_active = False
    stop jamendo_ambience fadeout 0.5
    $ stop_story_soundtrack()
    if _return == "replay":
        $ renpy.full_restart(label="start")
    return
