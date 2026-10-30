from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from udala.aldizkariak.content.publication import IPublication
from udala.aldizkariak.testing import INTEGRATION_TESTING
from zope.component import createObject
from zope.component import queryUtility

import unittest


class PublicationIntegrationTest(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_publication_schema(self):
        fti = queryUtility(IDexterityFTI, name="Publication")
        schema = fti.lookupSchema()
        self.assertEqual(IPublication, schema)

    def test_ct_publication_fti(self):
        fti = queryUtility(IDexterityFTI, name="Publication")
        self.assertTrue(fti)

    def test_ct_publication_factory(self):
        fti = queryUtility(IDexterityFTI, name="Publication")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPublication.providedBy(obj),
            f"IPublication not provided by {obj}!",
        )

    def test_ct_publication_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="Publication",
            id="publication",
        )

        self.assertTrue(
            IPublication.providedBy(obj),
            f"IPublication not provided by {obj.id}!",
        )

        parent = obj.__parent__
        self.assertIn("publication", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("publication", parent.objectIds())

    def test_ct_publication_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Publication")
        self.assertTrue(fti.global_allow, f"{fti.id} is not globally addable!")

    def test_ct_publication_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Publication")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "publication_id",
            title="Publication container",
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type="Document",
            title="My Content",
        )
        self.assertTrue(obj, f"Cannot add {obj.id} to {fti.id} container!")
