import pytest

@pytest.fixture()
def setup():
    print("Trial-essai")

def testmethod1(setup):
    print("Trial-essai")

def testmethod2(setup):
    print("Trial-essai")
