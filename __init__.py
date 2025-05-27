from load_audio import load_audio
from extract_features import extract_features
from build_grammar import build_grammar
from to_midi import grammar_to_midi

if __name__ == "__main__":
    audio_file = "flute.wav"
    y, sr = load_audio(audio_file)
    features = extract_features(y, sr)
    grammar = build_grammar(features, instrument="violin")
    grammar_to_midi(grammar, "generated_violin_flute.mid")
