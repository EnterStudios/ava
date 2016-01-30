import logging
import re

from django.core.exceptions import ValidationError

log = logging.getLogger(__name__)


class IdentifierValidation(object):
    # Skype names <https://support.skype.com/en/faq/FA10858/what-is-a-skype-name-and-how-do-i-find-mine>
    # - are 6-32 characters in length
    # - start with a letter
    # - may contain: alphanumeric, full stop, comma, underscore and hyphen
    VALIDATE_SKYPE = re.compile(r'^[A-Za-z][a-z0-9.,_-]{5,31}$')

    # Twitter usernames <https://support.twitter.com/articles/101299-why-can-t-i-register-certain-usernames>
    # - up to 15 characters in length
    # - may contain: alphanumeric, underscore
    VALIDATE_TWITTER = re.compile(r'^[A-Za-z0-9_]{1,15}$')


def validate_skype(skype_username):
    """
    Validates that the user name meets Skype's rules for valid user names.
    :param skype_name: The Skype user name to validate.
    """
    if IdentifierValidation.VALIDATE_SKYPE.match(skype_username) is None:
        raise ValidationError('Skype user name is not valid.')


def validate_twitter(twitter_username):
    """
    Validates that the supplied user name meets Twitter's rules for valid
    user names.
    :param twitter_username: The Twitter user name to validate.
    """
    if IdentifierValidation.VALIDATE_TWITTER.match(twitter_username) is None:
        raise ValidationError('Twitter user name is not valid.')
