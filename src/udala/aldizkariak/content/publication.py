# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container

# from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.namedfile import field as namedfile
from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
from zope.interface import alsoProvides

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
# from zope import schema
from zope.interface import implementer
from plone.app.dexterity.textindexer import searchable

from udala.aldizkariak import _


class IPublication(model.Schema):
    """Marker interface and Dexterity Python Schema for Publication"""

    file = namedfile.NamedBlobFile(
        title=_("Publication pdf"),
        required=True,
    )


alsoProvides(IPublication["file"], ILanguageIndependentField)


@implementer(IPublication)
class Publication(Container):
    """Content-type class for IPublication"""
