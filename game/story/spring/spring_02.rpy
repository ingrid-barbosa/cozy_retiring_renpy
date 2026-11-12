label spring_02:
    scene bg spring_2
    with dissolve
    "Day 2 - Spring"
    "Fern follows the path beyond the meadow and finds a cottage behind the flower fields."
    fern "Hello? Is anyone home?"
    if house_color == "yellow":
        show rowan at rowan_portrait
        rowan "Oh... I didn't expect a visitor."
        fern "Sorry, I was just exploring."
        call rowan_introduction
        fern "Caelum helped me settle in. I didn't realize I had a neighbor."
        rowan "You know Caelum the cat? Then we're good. Do you care to share some tea in my cottage?"
        menu:
            "Accept the tea and ask how Rowan came to live here.":
                $ empatia += 1
                $ day_summary = "Rowan answered the door. Fern accepted his tea and heard how his cottage came to feel like home."
                scene bg rowan_cottage
                show rowan at rowan_portrait
                with dissolve
                rowan "This place has been my home for many years."
                fern "It feels warm... different from my cottage."
                rowan "It took me a long time to feel that way about it, too."
            "Ask Rowan about the withered flowers by the path.":
                $ curiosidade += 1
                $ day_summary = "Rowan answered the door. Fern asked him about the withered flowers at the edge of the meadow."
                rowan "The flowers in this meadow never truly disappear. That's what worries me about the ones that have."
            "Thank Rowan and keep exploring on her own.":
                $ independencia += 1
                $ day_summary = "Fern met Rowan at his cottage, then chose to find her way home on her own."
                fern "Another time, perhaps. I'd like to learn the way home by myself while there's still daylight."
    else:
        "Nobody answers. Fern hears only the wind moving through the orchard."
        menu:
            "Leave a friendly note by the door.":
                $ empatia += 1
                $ day_summary = "Nobody answered at the cottage, so Fern left a note with her name and where to find her."
                "Fern writes her name and where to find her, then tucks the note under a dry stone."
            "Look for signs that someone still lives here.":
                $ curiosidade += 1
                $ day_summary = "Nobody answered at the cottage. Fern looked around and found withered flowers by the meadow."
                "The doorstep has been swept. Beyond it, Fern notices a few withered flowers at the edge of the meadow."
            "Head back and map the path to her cottage.":
                $ independencia += 1
                $ day_summary = "Nobody answered at the cottage. Fern sketched the trail so she could find it again."
                "Fern makes a sketch of the orchard and the bend in the path so she can find her way here again."
    call return_home
    return
