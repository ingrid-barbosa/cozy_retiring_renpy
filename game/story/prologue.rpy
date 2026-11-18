define prologue_text = Character(None, screen="prologue_text", statement_name="say-centered", cb_fixed_text_speed=True)

screen prologue_text(who, what):
    text what id "what":
        align (0.5, 0.5)
        textalign 0.5
        xmaximum 1400
        font gui.text_font
        size 42
        color "#ffffff"
        slow_cps 38
        slow_abortable True

label prologue:
    scene black
    prologue_text "For nearly three hundred years, Fern protected the enchanted forests of the South."
    prologue_text "Lately, she had been dreaming of a cottage where she could rest and finally call the place home."
    mysterious "Finally... you are here, Fern."
    fern "Who is there?"
    mysterious "Forgive me. I should introduce myself."
    show caelum at speaker_right
    caelum "My name is Caelum. I protect the northern forests."
    fern "So you are the guardian of this place."
    caelum "Yes. And I heard that the southern guardian finally decided to rest."
    fern "After so many years... I thought it was time."
    caelum "I understand your feelings, I wait for the day that my rest also comes"
    caelum "Please, allow me to help you find a place to call home here, as I know all the places in the North."
    return

label day_passed(day):
    scene black
    with fade
    prologue_text "Day [day] has come to an end.\n\n[day_summary]"
    $ memory_book_day = min(day + 1, 3)
    return
