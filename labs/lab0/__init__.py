import check50


@check50.check()
def exists():
    """lab0.py exists"""
    check50.exists("lab0.py")


@check50.check(exists)
def testbruce():
    """input of HELLO yields output of hello"""
    check50.run("python3 lab0.py").stdin("Bruce", prompt=True).stdin(
        "42", prompt=True
    ).stdin(
        "11", prompt=True
    ).
    stdout("Hey Bruce! The sum of 42 and 11 is 53.\n").exit()

