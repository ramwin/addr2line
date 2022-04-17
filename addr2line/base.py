"""
this module will create a background process (addr2line -g -e filename)
"""


from pathlib import Path
import subprocess


class ExecutableFileParser(object):
    """
    this class will keep the subprocess information
    executable_file: the executable file, like a.out
    TODO: make the command addr2line changable
    """

    def __init__(self, executable_file: Path):
        self.executable_file = executable_file
        self.process = None

    def prepare(self):
        if self.process is not None:
            raise Exception("I have been prepared")
        cmds = ["addr2line", "-f", "-e", self.executable_file]
        self.process = subprocess.Popen(cmds,
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        # stderr=subprocess.PIPE,
                                        text=True,
                                        encoding="utf-8",
                                        )

    def get_function(self, addr: int):
        # cmds = ["addr2line", "-f", "-e", self.executable_file, hex(addr)[2:]]
        # res = subprocess.run(cmds, encoding="utf-8", capture_output=True)
        # return res.stdout.split("\n")[0]
        assert self.process, "I'm not prepared"
        self.process.stdin.write(hex(addr)[2:] + "\n")
        self.process.stdin.flush()
        function_name = self.process.stdout.readline().strip()
        self.process.stdout.readline()
        return function_name

    def stop(self):
        self.process.stdin.close()
        self.process.stdout.close()
        # self.process.stderr.close()
        self.process.wait(1)


class Addr2lineContext:

    def __init__(self, file: Path):
        self.file = file
        self.parser = ExecutableFileParser(self.file)

    def __enter__(self):
        self.parser.prepare()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.parser.stop()

    def get_function(self, addr: int):
        return self.parser.get_function(addr)
