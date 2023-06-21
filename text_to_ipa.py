import ndjson
import pandas as pd
from functools import partial
from phonemizer.backend import EspeakBackend
from phonemizer.punctuation import Punctuation
from phonemizer.separator import Separator

_phonemizer_language_map = {
    'hi_HI': 'hi',
    'hi': 'hi',
    'mar_MAR': 'mr',
    'te_TE': 'te',
    'pt_BR': 'pt-br',
    'en_US': 'en-us',
    'en': 'en-us',
    'de_DE': 'de',
    'fr_FR': 'fr-fr',
    'es_ES': 'es',
    'es_CO': 'es-419',
    'es_AR': 'es-419',
    'es_CL': 'es-419',
    'es_PE': 'es-419',
    'es_PR': 'es-419',
    'es_VE': 'es-419',
    'es_MX': 'es-419',
    'en_ES': 'en-us',
    'en_MN': 'en-us',
    'en_UK': 'en-gb'
}


def get_phonemizer_output(text, phonemizer_backend, separator, punctuation):
    text_ipa = phonemizer_backend.phonemize(
        [text],
        separator=separator,
        strip=True)[0]
    text_ipa = text_ipa.replace('|\p|', ' ')
    text_ipa = '{' + text_ipa + '}'
    return text_ipa


def main(metadata_path, language, save_path, field):
    with open(metadata_path, "r") as fp:
        metadata = ndjson.load(fp)
    df = pd.DataFrame(metadata)
    print(f"Loaded metadata from {metadata_path}")

    separator = Separator(phone='|\p|', word='} {')
    punctuation = Punctuation.default_marks()
    phonemizer_backend = EspeakBackend(language,
                                       preserve_punctuation=True,
                                       with_stress=True,
                                       words_mismatch='ignore')

    fn = partial(get_phonemizer_output,
                 phonemizer_backend=phonemizer_backend,
                 separator=separator,
                 punctuation=punctuation)
    df['text_ipa'] = df[args.field].apply(fn)
    df_new = df.to_dict('records')
    with open(save_path, "w", encoding="utf-8") as fp:
        ndjson.dump(df_new, fp, ensure_ascii=False)
    print(f"Added ipa transcriptions and saved to {save_path}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata_path", required=True)
    parser.add_argument("--save_path", required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument("--field", default='text')

    args = parser.parse_args()
    main(args.metadata_path, args.language, args.save_path, args.field)
