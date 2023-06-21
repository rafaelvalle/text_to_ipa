# text to ipa
Adds IPA transcriptions given text metadata in ndjson format.  
Requires [espeak-ng](https://github.com/espeak-ng/espeak-ng) and python libraries listed in `requirements.txt`   
Please refer to [phonemizer's repo](https://github.com/bootphon/phonemizer) on how to install the espeak-ng backend.

#### How to use:
`python text_to_ipa.py --metadata_path "metadata.ndjson" --language "en-us" --save_path metadata_with_ipa.ndjson`
