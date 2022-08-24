import check50


@check50.check()
def exists():
    """lab1.py exists"""
    check50.exists("lab1.py")


@check50.check(exists)
def testviktor():
    """input of Viktor, hourly wage 15.25, hours worked 38, yields Net Pay of $452.01'"""
    check50.run("python3 lab1.py").stdin("Viktor", prompt=True).stdin(
        "15.25", prompt=True
    ).stdin("38", prompt=True).stdout("\n").stdout(
        "Name: Viktor\nHourly wage: $15.25\nLocal taxes: $57.95\nMedical insurance: $69.54\nOvertime pay: $0\nTotal gross earnings: $579.5\nNet pay: $452.01"
    ).exit()


@check50.check(exists)
def testviktor():
    """input of Viktor, hourly wage 15.25, hours worked 38, yields Net Pay of $452.01'"""
    check50.run("python3 lab1.py").stdin("Viktor", prompt=True).stdin(
        "15.25", prompt=True
    ).stdin("38", prompt=True).stdout("\n").stdout(
        "Name: Viktor\nHourly wage: $15.25"
    ).exit()
