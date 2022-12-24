import check50
import re


@check50.check()
def exists():
    """helloworld.py exists"""
    check50.exists("helloworld.py")


@check50.check(exists)
def testhello():
    """Prints out hello world"""
    output = check50.run("python3 helloworld.py").stdout()
    if not re.match("[Hh]ello,? world!?", output):
        raise check50.Mismatch("hello, world", output)
    