import check50


@check50.check()
def exists():
    """problem1.py - problem10.py exist"""
    check50.exists("problem1.py").exists("problem2.py").exit()
    
    


