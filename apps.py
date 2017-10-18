# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _


from django.apps import AppConfig


class AgreementsConfig(AppConfig):
    name = 'agreements'
    verbose_name = _("User agreements")
