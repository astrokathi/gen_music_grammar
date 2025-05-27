def build_grammar(features, instrument="violin"):
    grammar = []
    prev_onset = 0
    for i, onset in enumerate(features["onsets"]):
        pitch = features["pitch"][onset] if onset < len(features["pitch"]) else 0
        vel = features["velocity"][onset] if onset < len(features["velocity"]) else 0
        pause = (onset - prev_onset) / 100.0
        duration = 0.5  # placeholder, could be refined by looking at onset difference

        grammar.append({
            "note": {
                "pitch": int(pitch),
                "velocity": float(vel),
                "duration": duration,
                "instrument": instrument
            },
            "pause": pause
        })
        prev_onset = onset
    return grammar
