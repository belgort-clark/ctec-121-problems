import check50

@check50.check()
def exists():
    """problem1.py, problem2.py, problem3.py and problem4.py exist"""
    check50.exists("demo1.py")
    check50.exists("demo2.py")
    check50.exists("demo3.py")
    check50.exists("demo4.py")

