
import nltk
import os


def nltk_find_and_download(package_name, path):
    downloaded = False
    try:
        if not (nltk.data.find(f'{path}/{package_name}')):
            nltk.download(package_name)
            downloaded = True
    except:
        nltk.download(package_name)
        downloaded = True
    if not downloaded:
        try:
            if not nltk.data.find(f'{path}/{package_name}.zip'):
                nltk.download(package_name)
        except:
            nltk.download(package_name)


def download_nltk_data():
    nltk_find_and_download('wordnet', 'corpora')
    nltk_find_and_download('punkt', 'tokenizers')
    nltk_find_and_download('averaged_perceptron_tagger', 'taggers')


if int(os.environ.get("RANK", 0)) == 0:
    download_nltk_data()
