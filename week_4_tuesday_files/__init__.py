import check50


@check50.check()
def exists():
    """problem1.py - problem4.py exist"""
    check50.exists("problem1.py")
    check50.exists("problem2.py")
    check50.exists("problem3.py")
    check50.exists("problem4.py")

