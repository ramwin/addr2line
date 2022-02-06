from pathlib import Path
from addr2line.base import Addr2lineContext
import unittest


class Test(unittest.TestCase):

    def test(self):
        """
        0000000000001139 g     F .text	0000000000000025              function1
        000000000000115e g     F .text	0000000000000025              function2
        0000000000001183 g     F .text	0000000000000025              function3
        00000000000011a8 g     F .text	0000000000000029              main
        """
        with Addr2lineContext(Path("tests/source.out")) as c:
            self.assertEqual(
                c.get_function(0x1189),
                "function3",
            )
            self.assertEqual(
                c.get_function(0x11a8),
                "main",
            )
