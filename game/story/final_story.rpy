define final_story_narrator = Character(None, screen="prologue_text", cb_fixed_text_speed=True)

init python:
    def final_story_paragraphs():
        paragraphs = [
            "With Caelum's help, Fern made the {} cottage in {} her new home.".format(
                house_color, home_memory_locations[season]),
        ]
        for day in range(1, 4):
            chapter = "{} - Day {}".format(season.capitalize(), day)
            decisions = [
                description for memory_chapter, description in playthrough_memories
                if memory_chapter == chapter
            ]
            if decisions:
                if season == "autumn" and day == 3 and not visited_dark_autumn:
                    paragraphs.append("Fern followed the forest trail to a clearing and found her way home before dark.")
                else:
                    paragraphs.append(decisions[-1])
        final_choices = [
            description for chapter, description in playthrough_memories
            if chapter == "Fern's next chapter"
        ]
        choice = final_choices[-1] if final_choices else ""
        conclusions = {
            "Protect the forest on this side.": "Fern chose to become a guardian on this side. She would begin with the roots that needed her care, ask others to share the work, and return to her cottage at dusk.",
            "Keep exploring the world.": "Fern chose to keep exploring. She packed for another day away and kept her cottage key close, knowing there was a place she could return to.",
            "Collect the stories of this place.": "Fern chose to collect the stories of this place. She began with what she had witnessed herself and left room for the voices of those who remembered more.",
            "Make a quiet life here.": "Fern chose a quiet life. She put the kettle on and opened the window. In the morning, she could wake when she pleased and decide how to spend her day.",
        }
        paragraphs.append(conclusions.get(choice, "Fern returned home with the memories of the paths she had chosen."))
        return paragraphs

screen cozy_final_story():
    modal True
    zorder 200

    add Solid("#000")
    key "game_menu" action Return("menu")

    text _("The End"):
        align (0.5, 0.5)
        font gui.text_font
        size 42
        color "#ffffff"

    hbox:
        xalign 0.5
        yalign 0.8
        spacing 100
        textbutton _("Main Menu") action Return("menu")
        textbutton _("Play Again") action Return("replay")
