import check50
import re


@check50.check()
def exists():
    """helloworld.py exists"""
    check50.exists("helloworld.py")


@check50.check(exists)
def testhello():
    """Prints out Hello, World!"""
    output = check50.run("python3 helloworld.py").stdout()
    if not re.match("Hello, World!", output):
        raise check50.Mismatch("Hello, World", output)
    