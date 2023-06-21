# text to ipa
Adds IPA transcriptions given text metadata in ndjson format.
Requires espeak-ng and python libraries described in `requirements.txt`
Please refer to [phonemizer's repo](https://github.com/bootphon/phonemizer) on how to install the espeak-ng backend.

`python text_to_phonemizer.py --metadata_path "metadata.ndjson" --language "en-us" --save_path metadata_with_ipa.ndjson`
