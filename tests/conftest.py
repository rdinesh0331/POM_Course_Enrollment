import pytest
from base_package.webdriverfactory import WebDriverFactory


@pytest.fixture()
def setup():
    pass

@pytest.fixture(scope="class")
def oneTimeSetup(request,Browseroption, OSoption):
    wdf = WebDriverFactory(Browseroption)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()



def pytest_addoption(parser):
    parser.addoption("--Browseroption")
    parser.addoption("--OSoption")



@pytest.fixture(scope="session")
def Browseroption(request):
    return request.config.getoption("--Browseroption")



@pytest.fixture(scope="session")
def OSoption(request):
    return request.config.getoption("--OSoption")






