"""
Tests for library tools service.
"""
from mock import patch
from xmodule.library_tools import LibraryToolsService
from xmodule.modulestore.tests.factories import LibraryFactory
from xmodule.modulestore.tests.utils import MixedSplitTestCase


class LibraryToolsServiceTest(MixedSplitTestCase):
    """
    Tests library service
    """

    def setUp(self):
        super(LibraryToolsServiceTest, self).setUp()

        self.tools = LibraryToolsService(self.store)

    def test_list_available_libraries(self):
        """
        Test listing of libraries.
        """
        _ = LibraryFactory.create(modulestore=self.store)
        all_libraries = self.tools.list_available_libraries()
        self.assertTrue(all_libraries)
        self.assertEqual(len(all_libraries), 1)
        # make sure light weight library summary objects are used to generate library list
        with patch(
                'xmodule.modulestore.split_mongo.split.SplitMongoModuleStore.get_library_summaries'
        ) as mock_get_library_summaries:
            _ = self.tools.list_available_libraries()
            self.assertTrue(mock_get_library_summaries.called)
