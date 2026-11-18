label spring_02:
    scene bg spring_2
    with dissolve
    "Day 2 - Spring"
    fern "I saw lamplight from this direction last night. I nearly came over, then remembered I could introduce myself in daylight."
    fern "I used to know every household along my patrol. Here, I can knock on a door simply because I'd like to meet whoever lives behind it."
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
                $ unlock_choice_memory("spring_02:accept-the-tea-and-ask-how-rowan-came-to-live-here", "Spring - Day 2", day_summary)
                scene bg rowan_cottage
                show rowan at rowan_portrait
                with dissolve
                rowan "This place has been my home for many years."
                fern "It feels warm... different from my cottage."
                rowan "It took me a long time to feel that way about it, too."
                fern "Rowan set my cup down with the handle turned toward me. I like that there's a way to say welcome even after you've already said it."
            "Ask Rowan about the withered flowers by the path.":
                $ curiosidade += 1
                $ day_summary = "Rowan answered the door. Fern asked him about the withered flowers at the edge of the meadow."
                $ unlock_choice_memory("spring_02:ask-rowan-about-the-withered-flowers-by-the-path", "Spring - Day 2", day_summary)
                rowan "The flowers in this meadow never truly disappear. That's what worries me about the ones that have."
                fern "I had half a dozen more questions ready. Rowan lives with those flowers in sight of his window. I wonder which one he'd ask first."
            "Thank Rowan and keep exploring on her own.":
                $ independencia += 1
                $ day_summary = "Fern met Rowan at his cottage, then chose to find her way home on her own."
                $ unlock_choice_memory("spring_02:thank-rowan-and-keep-exploring-on-her-own", "Spring - Day 2", day_summary)
                fern "Another time, perhaps. I'd like to learn the way home by myself while there's still daylight."
                fern "I hope he asks me again. I'd like my first walk home from here to belong to me."
    else:
        "Nobody answers. Fern hears only the wind moving through the orchard."
        menu:
            "Leave a friendly note by the door.":
                $ empatia += 1
                $ day_summary = "Nobody answered at the cottage, so Fern left a note with her name and where to find her."
                $ unlock_choice_memory("spring_02:leave-a-friendly-note-by-the-door", "Spring - Day 2", day_summary)
                "Fern writes her name and where to find her, then tucks the note under a dry stone."
                fern "I nearly signed it with my old title. It looks strange to see my name on a piece of paper with nothing after it."
            "Look for signs that someone still lives here.":
                $ curiosidade += 1
                $ day_summary = "Nobody answered at the cottage. Fern looked around and found withered flowers by the meadow."
                $ unlock_choice_memory("spring_02:look-for-signs-that-someone-still-lives-here", "Spring - Day 2", day_summary)
                "The doorstep has been swept. Beyond it, Fern notices a few withered flowers at the edge of the meadow."
                fern "The swept step reassured me. It makes the flowers beyond it feel peculiar. Someone is paying attention here."
            "Head back and map the path to her cottage.":
                $ independencia += 1
                $ day_summary = "Nobody answered at the cottage. Fern sketched the trail so she could find it again."
                $ unlock_choice_memory("spring_02:head-back-and-map-the-path-to-her-cottage", "Spring - Day 2", day_summary)
                "Fern makes a sketch of the orchard and the bend in the path so she can find her way here again."
                fern "On the sketch, I drew the orchard twice the size it needed to be. I suppose that's the part I wanted to remember."
    call return_home
    return
