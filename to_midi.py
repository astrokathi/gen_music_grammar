from mido import Message, MidiFile, MidiTrack, bpm2tempo


def clamp(value, min_val=0, max_val=127):
    return max(min(int(value), max_val), min_val)


def grammar_to_midi(grammar, filename="output.mid", bpm=120):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=40, time=0))  # violin

    for item in grammar:
        note = item["note"]
        pause_ticks = int(item["pause"] * 480)
        dur_ticks = int(note["duration"] * 480)
        pitch = clamp(note["pitch"], 0, 127) if note["pitch"] > 0 else 60
        velocity = clamp(note["velocity"] * 127, 0, 127)

        track.append(Message('note_on', note=pitch, velocity=velocity, time=pause_ticks))
        track.append(Message('note_off', note=pitch, velocity=0, time=dur_ticks))

    mid.save(filename)
