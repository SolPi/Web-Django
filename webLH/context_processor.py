# coding:utf8
from django.conf import settings

def SiteInfo(request):
	return {
		'site_title':settings.SITE_TITLE,
		'site_motto':settings.SITE_MOTTO,
		'site_since':"Desde " + settings.SITE_SINCE,
	}