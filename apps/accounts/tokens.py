from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    """
    Use PasswordResetTokenGenerator to make hash the value.
    """
    def _make_hash_value(self, user, timestamp):
        """
        Get user pk and user is_active boolean field and time to generate a valid token by Six lib.
        """
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()
