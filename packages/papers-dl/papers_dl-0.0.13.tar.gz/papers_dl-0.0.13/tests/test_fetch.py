import unittest

import aiohttp
import asyncio

from src.providers.scihub import SciHub


class TestSciHub(unittest.IsolatedAsyncioTestCase):
    def test_scihub_up(self):
        """
        Test to verify that `scihub.now.sh` is available
        """
        urls = SciHub.get_available_scihub_urls()
        self.assertIsNotNone(urls, "Failed to find Sci-Hub domains")
