from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

import urllib.parse


EMAIL_RECIPIENTS = (
    ('all_participants', _('all participants')),
    ('due_participants', _('due participants')),
    ('responsible', _('responsible person')),
    ('editors', _('all editors')),
    ('contributors', _('all contributors'))
)

def custom_redirect(url_name, *args, **kwargs):
    url = reverse(url_name, args=args)
    params = urllib.parse.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)
