image fern = "images/characters/Fern_Character.png"
image caelum = "images/characters/Caelum_Character.png"
image rowan = "images/characters/Rowan_Character.png"

image fern_box = "images/ui/chat_box/Fern_BOX.png"
image caelum_box = "images/ui/chat_box/Caelum_BOX.png"
image rowan_box = "images/ui/chat_box/Rowan_BOX.png"
image ui_box = "images/ui/chat_box/UI_BOX.png"
image narrator_box = Crop((0, 629, 2245, 329), "images/ui/chat_box/narrator_BOX.png")

init python:
    def scenery_background(filename):
        scenery = Transform(filename, xysize=(1920, 1080), fit="cover")
        return ConditionSwitch(
            "renpy.showing('rowan')",
            Transform(scenery, blur=11.0, matrixcolor=TintMatrix("#a6a6a6")),
            "any(renpy.showing(tag) for tag in ('fern', 'caelum', 'bird', 'turtle', 'squirrel'))",
            Transform(scenery, blur=6.0),
            "True",
            scenery,
            predict_all=True,
        )

    def animal_photo(filename):
        photo = Transform(filename, xysize=(552, 462), fit="contain")
        return Window(photo, style="empty", background=Solid("#ffffff"),
                      padding=(14, 14), xfill=False, yfill=False)

image bg home_spring = scenery_background("images/backgrounds/spring/Background SPRING.png")
image bg spring_1 = scenery_background("images/backgrounds/spring/Spring 1.png")
image bg spring_2 = scenery_background("images/backgrounds/spring/Spring 2.png")
image bg spring_3 = scenery_background("images/backgrounds/spring/Spring 3.png")
image bg dark_spring = scenery_background("images/backgrounds/special/Dark_spring.png")
image bg home_summer = scenery_background("images/backgrounds/summer/Background SUMMER.png")
image bg summer_1 = scenery_background("images/backgrounds/summer/Summer 1.png")
image bg summer_2 = scenery_background("images/backgrounds/summer/Summer 2.png")
image bg summer_3 = scenery_background("images/backgrounds/summer/Summer 3.png")
image bg dark_summer = scenery_background("images/backgrounds/special/Dark_summer.png")
image bg home_autumn = scenery_background("images/backgrounds/autumn/Background AUTUMN.png")
image bg autumn_1 = scenery_background("images/backgrounds/autumn/Autumn 1.png")
image bg autumn_2 = scenery_background("images/backgrounds/autumn/Autumn 2.png")
image bg autumn_3 = scenery_background("images/backgrounds/autumn/Autumn 3.png")
image bg dark_autumn = scenery_background("images/backgrounds/special/Dark_autumn.png")
image bg rowan_cottage = scenery_background("images/backgrounds/spring/Rowan_cottage.png")

image house yellow = "images/houses/house_yellow.png"
image house blue = "images/houses/house_blue.png"
image house red = "images/houses/house_red.png"

image bird = animal_photo("images/objects/bird_spring 1.png")
image turtle = animal_photo("images/objects/turtle_summer.png")
image shell = "images/objects/shell_summer 1.png"
image squirrel = animal_photo("images/objects/squirrel_autumn 1.png")

transform cottage_position:
    xalign 0.5
    yalign 0.78
    xysize (660, 550)
    fit "contain"

transform speaker_right:
    xalign 0.80
    yalign 0.60
    xysize (850, 940)
    fit "contain"

transform rowan_portrait:
    xalign 0.80
    ypos 205
    yanchor 0.0
    xysize (940, 1040)
    fit "contain"

transform discovery:
    xalign 0.5
    yalign 0.40
    xysize (580, 490)
    fit "contain"

transform moonlight:
    matrixcolor TintMatrix("#7789bd")
