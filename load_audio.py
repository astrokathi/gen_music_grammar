import librosa


def load_audio(filepath, sr=16000):
    y, _sr = librosa.load(filepath, sr=sr)
    return y, _sr
