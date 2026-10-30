# from azpeitia.addon import _
from Acquisition import aq_inner
from Products.CMFPlone.utils import human_readable_size
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface

import time


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IPublicationView(Interface):
    """Marker Interface for IPublicationView"""


@implementer(IPublicationView)
class PublicationView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('publication_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()

    def human_readable_size(self):
        return human_readable_size(self.context.file.getSize())

    def time_for_no_caching(self):
        return str(time.time())


class EmbedPublicationView(BrowserView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.traverse_subpath = []

    def publishTraverse(self, request, name):
        self.traverse_subpath.append(name)
        return self

    def __call__(self):
        context = aq_inner(self.context)
        data = context.file.data
        self.request.response.setHeader("Content-Type", "application/pdf")
        self.request.response.setHeader("Content-Length", len(data))
        return self.request.response.write(data)
