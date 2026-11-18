default playthrough_memories = []
default playthrough_memory_keys = {}
default memory_book_day = 1

init python:
    config.overlay_screens.append("cozy_memory_icon")

    def memory_book_entries_by_day():
        entries = {1: [], 2: [], 3: []}
        for chapter, description in playthrough_memories:
            _, separator, day_number = chapter.rpartition(" - Day ")
            if separator and day_number in ("1", "2", "3"):
                entries[int(day_number)].append((None, description))
            else:
                day = 3 if chapter == "Fern's next chapter" else 1
                entries[day].append((chapter, description))
        if read_tree:
            directions = (
                "1. At the first fork, turn LEFT beneath the white root.\n\n"
                "2. At the next fork, turn RIGHT toward the hollow sound.\n\n"
                "3. At the last fork, turn LEFT beneath the branches that touch."
            )
            entries[2].append(("Directions from the white tree", directions))
            entries[3].insert(0, ("Follow the white tree's directions", directions))
        return entries

    def unlock_choice_memory(key, chapter, description):
        global playthrough_memories
        playthrough_memory_keys[len(playthrough_memories)] = key
        playthrough_memories = playthrough_memories + [(chapter, description)]
        notification_id = "{}:{}".format(key, len(playthrough_memories))
        renpy.show_screen("cozy_memory_notification", memory_key=notification_id)
        renpy.music.play("musics/effects/scribble.mp3", channel="sound", loop=False)

screen cozy_memory_icon():
    zorder 90

    imagebutton:
        idle Transform("images/ui/Memorybook_ICON.png", xysize=(96, 72), fit="contain")
        hover Transform("images/ui/Memorybook_ICON.png", xysize=(96, 72), fit="contain", matrixcolor=BrightnessMatrix(0.12))
        xalign 1.0
        xoffset -24
        ypos 18
        alt _("Open Memory Book")
        action Show("cozy_livro")

screen cozy_memory_notification(memory_key):
    zorder 99

    frame at notify_appear:
        xalign 1.0
        xoffset -24
        ypos 106
        padding (20, 12)
        background Solid("#32233aed")
        text _("New memory unlocked!") size 27 color "#fff4df"

    timer 3.25 id memory_key action Hide("cozy_memory_notification")

transform memory_book_open:
    align (0.5, 0.5)
    zoom 0.78
    alpha 0.0
    easeout 0.28 zoom 1.0 alpha 1.0

style memory_book_ink is default:
    font gui.interface_text_font
    color "#49262c"
    size 32

style memory_book_button_text is memory_book_ink:
    size 28
    hover_color "#a23d51"
    insensitive_color "#927e79"

screen cozy_livro():
    modal True
    zorder 100
    default selected_day = None

    $ entries = memory_book_entries_by_day()
    $ latest_day = max(day for day in entries if day <= memory_book_day or entries[day])
    $ current_day = latest_day if selected_day is None else selected_day
    $ memories = entries[current_day]
    $ middle = (len(memories) + 1) // 2
    $ pages = (memories[:middle], memories[middle:])

    key "game_menu" action Hide("cozy_livro")
    add Solid("#150e1ac0")

    fixed at memory_book_open:
        xysize (1500, 960)
        add Transform("images/ui/Memory_BOOK.png", xysize=(1500, 960), fit="contain")

        text _("Day [current_day]") style "memory_book_ink" size 46 bold True pos (102, 61)
        textbutton _("Close"):
            xpos 1398
            xanchor 1.0
            ypos 63
            text_style "memory_book_button_text"
            action Hide("cozy_livro")

        if not memories:
            text _("No memories yet for this day.") style "memory_book_ink" pos (102, 158) xmaximum 560

        for page_index, page_memories in enumerate(pages):
            viewport:
                id ("memory_book_page_{}_{}".format(current_day, page_index))
                pos (102 + page_index * 736, 158)
                xysize (560, 655)
                mousewheel True
                draggable True

                vbox:
                    xsize 560
                    spacing 25
                    for title, description in page_memories:
                        vbox:
                            spacing 8
                            if title:
                                text title style "memory_book_ink" size 36 bold True substitute False
                            text description style "memory_book_ink" substitute False

        textbutton "<":
            pos (80, 837)
            text_style "memory_book_button_text"
            text_size 42
            alt _("Previous day")
            action SetScreenVariable("selected_day", current_day - 1)
            sensitive (current_day > 1)

        textbutton ">":
            xpos 1420
            xanchor 1.0
            ypos 837
            text_style "memory_book_button_text"
            text_size 42
            alt _("Next day")
            action SetScreenVariable("selected_day", current_day + 1)
            sensitive (current_day < latest_day)
