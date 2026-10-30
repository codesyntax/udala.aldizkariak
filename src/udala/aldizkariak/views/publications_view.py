from plone.app.contenttypes.browser.collection import CollectionView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IPublicationView(Interface):
    """Marker Interface for IPublicationkView"""


@implementer(IPublicationView)
class PublicationsView(CollectionView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('publicationk_view.pt')

    def publication_item_dict(self, news, index=0):
        obj = news.getObject()
        publi_dict = {
            "title": obj.Title(),
            "url": news.getURL(),
            "description": news.Description,
        }
        if obj.image:
            featured_scales = obj.restrictedTraverse("@@images")
            publi_dict["image"] = featured_scales.scale("image", scale="mini").url
        else:
            publi_dict["image"] = ""
        publi_dict["loading"] = (index > 8 and "lazy") or ""
        return publi_dict
