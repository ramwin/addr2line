# addr2line
interact with addr2line command

# Installation

    pip install addr2line


# Test

    python -m unittest discover tests


# usage


        with Addr2lineContext(Path("tests/source.out")) as c:
            self.assertEqual(
                c.get_function(0x1189),
                "function3",
            )
            self.assertEqual(
                c.get_function(0x11a8),
                "main",
            )
