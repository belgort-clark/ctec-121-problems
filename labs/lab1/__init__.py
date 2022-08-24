import check50
from re import escape


@check50.check()
def exists():
    """lab1.py exists"""
    check50.exists("lab1.py")


@check50.check(exists)
def testviktor():
    """input of Viktor, hourly wage 15.25, hours worked 38, yields Net Pay of $452.01'"""
    output = "\nName: Viktor\nHourly wage: $15.25\nLocal taxes: $57.95\nMedical insurance: $69.54\nOvertime pay: $0.00\nTotal gross earnings: $579.50\nNet pay: $452.01\n"
    check50.run("python3 lab1.py").stdin("Viktor", prompt=True).stdin(
        "15.25", prompt=True
    ).stdin("38", prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testjerome():
    """input of Jerome, hourly wage 15.25, hours worked 42, yields Net Pay of $511.48'"""
    output = "\nName: Jerome\nHourly wage: $15.25\nLocal taxes: $65.58\nMedical insurance: $78.69\nOvertime pay: $45.75\nTotal gross earnings: $655.75\nNet pay: $511.48\n"
    check50.run("python3 lab1.py").stdin("Jerome", prompt=True).stdin(
        "15.25", prompt=True
    ).stdin("42", prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testbella():
    """input of Bella, hourly wage 15.75, hours worked 40, yields Net Pay of $491.40'"""
    output = "\nName: Bella\nHourly wage: $15.75\nLocal taxes: $63.00\nMedical insurance: $75.60\nOvertime pay: $0.00\nTotal gross earnings: $630.00\nNet pay: $491.40\n"
    check50.run("python3 lab1.py").stdin("Bella", prompt=True).stdin(
        "15.75", prompt=True
    ).stdin("40", prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    """match case-sensitively, allowing for characters (not numbers) on either side. Ensure not negative with no dashes"""
    return rf"^[^\d-]*{escape(text)}[^\d]*$"
