import datetime

from investfly.api.MarketDataApiClient import MarketDataApiClient
from investfly.api.PortfolioApiClient import PortfolioApiClient
from investfly.api.RestApiClient import RestApiClient
from investfly.api.StrategyApiClient import StrategyApiClient
from investfly.models import Session


class InvestflyApiClient:
    """
    Investfly API Client. This class should be used as the entry point to make all API calls.
    After authentication, access marketApi or portfolioApi to make calls to /market or /portfolio endpoints
    """

    def __init__(self, baseUrl: str = "https://api.investfly.com"):
        self.restApiClient = RestApiClient(baseUrl)
        self.marketApi = MarketDataApiClient(self.restApiClient)
        """Class used to make calls to /market endpoint """
        self.portfolioApi = PortfolioApiClient(self.restApiClient)
        self.strategyApi = StrategyApiClient(self.restApiClient)

    def login(self, username, password) -> Session:
        """
        Login to investfly backend.
        :param username: Username
        :param password: Password
        :return: Session object representing authenticated session
        """
        return self.restApiClient.login(username, password)

    def logout(self):
        self.restApiClient.logout()

    def isLoggedIn(self) -> bool:
        return "investfly-client-id" in self.restApiClient.headers

    def getSession(self) -> Session:
        sessionJson = self.restApiClient.doGet('/user/session')
        session: Session = Session.fromJsonDict(sessionJson)
        return session

    @staticmethod
    def parseDatetime(date_str: str) -> datetime.datetime:
        return datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f%z')
