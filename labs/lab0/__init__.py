import check50


@check50.check()
def exists():
    """lab0.py exists"""
    check50.exists("lab0.py")


@check50.check(exists)
def testbruce():
    """input of Bruce, the numbers 42 and 11 yields output of 'Hey Bruce! The sum of 42 and 11 is 53.'"""
    check50.run("python3 lab0.py").stdin("Bruce", prompt=True).stdin(
        "42", prompt=True
    ).stdin("11", prompt=True).stdout("Hey Bruce! The sum of 42 and 11 is 53.\n").exit()


@check50.check(exists)
def testjacqueline(exists):
    """input of Jacqueline, the numbers 22 and 0 yields output of 'Hey Jacqueline! The sum of 22 and 0 is 22.'"""
    check50.run("python3 lab0.py").stdin("Bruce", prompt=True).stdin(
        "42", prompt=True
    ).stdin("11", prompt=True).stdout(
        "Hey Jacqueline! The sum of 22 and 0 is 22.\n"
    ).exit()


@check50.check(exists)
def testrashida(exists):
    """input of Rashida, the numbers -42 and -43 yields output of 'Hey Rashida! The sum of -42 and-43 is -85.'"""
    check50.run("python3 lab0.py").stdin("Bruce", prompt=True).stdin(
        "42", prompt=True
    ).stdin("11", prompt=True).stdout(
        "Hey Rashida! The sum of -42 and -43 is -85.\n"
    ).exit()
