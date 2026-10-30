# from udala.aldizkariak import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IPublicationView(Interface):
    """ Marker Interface for IPublicationView"""


@implementer(IPublicationView)
class PublicationView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('publication_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
