# coding:utf8
from datetime import date

from django.conf import settings


def SiteInfo(request):
    return {
        'site_title': settings.SITE_TITLE,
        'site_motto': settings.SITE_MOTTO,
        'site_since': "Desde " + settings.SITE_SINCE,
        'more_than_five': date.today().year - int(settings.IS_OLD) > int(settings.SITE_SINCE)
    }
