default story_music_mode = None
default story_music_channel = "music"
default story_music_file = None
default story_neutral_tracks_played = ()
default last_dark_track = None
default jamendo_ambience_active = True

# Measured MP3 durations in seconds, used if the audio backend cannot report them.
define story_track_durations = {
    "musics/seasonal/spring.mp3": 145.03,
    "musics/seasonal/summer.mp3": 137.69,
    "musics/seasonal/autumn.mp3": 134.06,
    "musics/neutral/neutral.mp3": 103.08,
    "musics/neutral/neutral2.mp3": 170.97,
    "musics/neutral/neutral3.mp3": 135.05,
    "musics/neutral/neutral4.mp3": 146.23,
}

init python:
    renpy.music.register_channel("story_music_alt", mixer="music", loop=False)
    renpy.music.register_channel("ambience", mixer="sfx", loop=True)
    renpy.music.register_channel("jamendo_ambience", mixer="sfx", loop=True)
    renpy.music.register_channel("radio_preview", mixer="music", loop=True)
    config.overlay_screens.append("cozy_soundtrack_timer")

    def local_story_tracks(group, prefix):
        folder = "musics/{}/".format(group)
        return sorted(
            filename for filename in renpy.list_files()
            if filename.startswith(folder + prefix)
            and "/" not in filename[len(folder):]
            and filename.rsplit(".", 1)[-1].lower() in ("mp3", "ogg", "wav", "opus")
        )

    def select_story_track(tracks, previous=None):
        alternatives = [track for track in tracks if track != previous]
        return renpy.random.choice(alternatives or tracks) if tracks else None

    def switch_story_track(filename, mode, fadeout=0.8, fadein=0.8, volume=0.15, loop=False):
        global story_music_channel, story_music_file, story_music_mode
        global story_neutral_tracks_played
        next_channel = "story_music_alt" if story_music_channel == "music" else "music"
        renpy.music.stop(channel=story_music_channel, fadeout=fadeout)
        if filename:
            renpy.music.play(filename, channel=next_channel, loop=loop,
                             fadein=fadein, fadeout=0, relative_volume=volume)
        story_music_channel, story_music_file, story_music_mode = next_channel, filename, mode
        if mode == "seasonal":
            story_neutral_tracks_played = ()
        elif mode == "neutral":
            story_neutral_tracks_played = (story_neutral_tracks_played + (filename,))[-4:]

    def play_season_soundtrack(selected_season):
        filename = "musics/seasonal/{}.mp3".format(selected_season)
        if story_music_file != filename and renpy.loadable(filename):
            switch_story_track(filename, "seasonal")

    def play_day_soundtrack(with_ambience=True):
        if story_music_mode not in ("seasonal", "neutral"):
            play_season_soundtrack(season)

        if with_ambience:
            environment = "beach" if season == "summer" else "nature"
            for extension in ("ogg", "mp3", "wav", "opus"):
                filename = "musics/{}.{}".format(environment, extension)
                if renpy.loadable(filename):
                    renpy.music.play(filename, channel="ambience", loop=True, fadein=0.5,
                                     fadeout=0.5, if_changed=True, relative_volume=0.35)
                    return

    def advance_story_soundtrack():
        if story_music_mode not in ("seasonal", "neutral") or not story_music_file:
            return
        if preferences.get_mute("music"):
            return
        playing = renpy.music.get_playing(channel=story_music_channel)
        position = renpy.music.get_pos(channel=story_music_channel)
        duration = (renpy.music.get_duration(channel=story_music_channel)
                    or story_track_durations.get(story_music_file))
        if playing and (playing != story_music_file or position is None
                        or not duration or duration - position > 6.0):
            return
        fade = 6.0 if playing else 0.8
        seasonal_track = "musics/seasonal/{}.mp3".format(season)
        if len(story_neutral_tracks_played) == 4 and renpy.loadable(seasonal_track):
            switch_story_track(seasonal_track, "seasonal", fadeout=fade, fadein=fade)
        else:
            neutral_tracks = local_story_tracks("neutral", "neutral")
            unplayed_tracks = [track for track in neutral_tracks if track not in story_neutral_tracks_played]
            next_track = select_story_track(unplayed_tracks or neutral_tracks, story_music_file)
            if not next_track:
                return
            switch_story_track(next_track, "neutral", fadeout=fade, fadein=fade, volume=0.10)
        renpy.restart_interaction()

    def play_mystery_soundtrack():
        global last_dark_track
        renpy.music.stop(channel="ambience", fadeout=0.5)
        if story_music_mode != "dark":
            track = select_story_track(local_story_tracks("dark", "dark"), last_dark_track)
            switch_story_track(track, "dark", loop=True)
            last_dark_track = track

    def stop_story_soundtrack():
        global story_music_mode, story_music_file
        story_music_mode = story_music_file = None
        for channel in ("music", "story_music_alt", "ambience"):
            renpy.music.stop(channel=channel, fadeout=0.5)

screen cozy_soundtrack_timer():
    zorder 90

    if jamendo_ambience_active and not main_menu:
        timer 1.0 repeat True action Function(cozy_jamendo_ambience.update, _update_screens=False)

    if story_music_file and not preferences.get_mute("music"):
        $ track_name = story_music_file.rsplit("/", 1)[-1].rsplit(".", 1)[0].title()
        frame:
            xpos 24
            ypos 18
            padding (18, 10)
            background Solid("#32233adc")
            text _("Now playing: [track_name]") size 24 color "#fff4df"

    if story_music_mode in ("seasonal", "neutral"):
        timer 0.25 repeat True action Function(advance_story_soundtrack, _update_screens=False)
