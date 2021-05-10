"""This module translat text on multiple langage."""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def english_to_french(recognized_text):
	"""
	translate english in french
	"""
	url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/cb11d724-6e45-4d10-832f-74750736e091'
	apikey_lt='xkiVlHqOONexj6oAsCv6fMZvwYA4x8Yxy0CLwpcHtK5B'
	version_lt='2018-05-01'
	authenticator = IAMAuthenticator(apikey_lt)
	language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
	language_translator.set_service_url(url_lt)

	if recognized_text != "":
		translation_response = language_translator.translate(\
		    text=recognized_text, model_id='en-fr')
		_get_only_result= translation_response.get_result()
		english_french_result =_get_only_result['translations'][0]['translation']
		return english_french_result
	else:
		return ""


def english_to_german(recognized_text):
	"""
	translate english in german
	"""
	url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/cb11d724-6e45-4d10-832f-74750736e091'
	apikey_lt='xkiVlHqOONexj6oAsCv6fMZvwYA4x8Yxy0CLwpcHtK5B'
	version_lt='2018-05-01'
	authenticator = IAMAuthenticator(apikey_lt)
	language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
	language_translator.set_service_url(url_lt)

	if recognized_text != "":
		translation_response = language_translator.translate(\
		    text=recognized_text, model_id='en-de')
		_get_only_result= translation_response.get_result()
		english_german_result =_get_only_result['translations'][0]['translation']
		return english_german_result
	else:
		return ""
