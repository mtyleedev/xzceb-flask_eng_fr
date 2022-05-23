"""
This module translates a given text from a language to another language
"""

from ensurepip import version
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

# print(apikey)
# print(url)

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version,authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    This function translates a given text from english to french.
    """
    #write the code here
    if(not (english_text and not english_text.isspace())):
        return None
    translation_response = \
        language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation_response['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """
    This function translates a given text from french to english.
    """
    #write the code here
    if(not (french_text and not french_text.isspace())):
        return None
    translation_response = \
        language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation_response['translations'][0]['translation']
    return english_text
