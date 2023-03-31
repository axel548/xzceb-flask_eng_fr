"""Translate with Watson and python."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
language_translator.set_service_url(url)


def englishToFrench(englishText):
    """Translate from English to French."""
    if len(englishText) == 0:
        frenchText = ''
    else:
        model_id = 'en-fr'
        translation = language_translator.translate(
            text=englishText,
            model_id=model_id).get_result()
        frenchText = translation["translations"][0]["translation"]
    return frenchText


def frenchToEnglish(frenchText):
    """Translate from French to English."""
    if len(frenchText) == 0:
        englishText = ''
    else:
        model_id = 'fr-en'
        translation = language_translator.translate(
            text=frenchText,
            model_id=model_id).get_result()
        englishText = translation["translations"][0]["translation"]
    return englishText


def list_languages():
    """A dummy docstring."""
    languages = language_translator.list_languages().get_result()
    print(json.dumps(languages, indent=2))


# print(englishToFrench('Hello'))
# print(frenchToEnglish('Bonjour'))
# list_languages()
