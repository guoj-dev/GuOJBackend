from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from django_rest_passwordreset.signals import reset_password_token_created
from django.contrib.sites.shortcuts import get_current_site


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'username': reset_password_token.user.username,
        'site_name': reset_password_token.user.email,
        'password_reset_key': reset_password_token.key,
    }

    # render email text
    email_html_message = render_to_string(
        'account/email/password_reset_key_message.txt', context)
    email_plaintext_message = render_to_string(
        'account/email/password_reset_key_message.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title='GuOJ'),
        # message:
        email_plaintext_message,
        # from:
        settings.DEFAULT_FROM_EMAIL,
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()