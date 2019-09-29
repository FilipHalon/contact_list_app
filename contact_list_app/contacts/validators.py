from django.core.exceptions import ValidationError
import re


def email_validator(email):

    if not re.match(r'.+@.+', email):
        raise ValidationError
