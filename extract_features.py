import librosa


def extract_features(y, sr):
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch = [pitches[magnitudes[:, t].argmax(), t] for t in range(magnitudes.shape[1])]

    rms = librosa.feature.rms(y=y)[0]
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)

    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

    return {
        "pitch": pitch,
        "velocity": rms.tolist(),
        "onsets": onsets.tolist(),
        "tempo": tempo,
        "mfccs": mfccs.tolist(),
        "timbre": spectral_centroid.tolist()
    }
