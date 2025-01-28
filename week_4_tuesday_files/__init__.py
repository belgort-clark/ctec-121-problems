import check50


@check50.check()
def exists():
    """problem1.py - problem4.py exist"""
    check50.exists("problem1.py").exists("problem2.py").exists("problem3.py").exists("problem4.py").exit()
    
    


