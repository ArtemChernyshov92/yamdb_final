from django.core.exceptions import ValidationError
from django.utils import timezone


def not_future(value):
    if value > timezone.now().year:
        raise ValidationError(
            'Значение %(value)s больше текущего года!',
            params={'value': value},
        )


def not_me(value):
    if value.lower() == 'me':
        raise ValidationError(
            'Значение %(value)s не может быть использовано!',
            params={'value': value},
        )
