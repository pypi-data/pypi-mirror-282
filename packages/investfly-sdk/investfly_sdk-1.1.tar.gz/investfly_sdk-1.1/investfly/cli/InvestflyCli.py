import argparse
import pickle
import os.path
from typing import List

from investfly.api.InvestflyApiClient import InvestflyApiClient
from investfly.models import Session
from investfly.models.StrategyModels import TradingStrategyModel

from investfly import samples
import inspect
from pathlib import Path
import shutil


class InvestflyCli:

    def __init__(self):
        self.running: bool = True
        self.investflyApi = InvestflyApiClient()


    def __loginAction(self, args: argparse.Namespace) -> Session:
        username = args.username
        password = args.password
        session = self.investflyApi.login(username, password)
        return session

    def __logoutAction(self, args: argparse.Namespace) -> None:
        self.investflyApi.logout()

    def __listStrategies(self, args: argparse.Namespace) -> str:
        strategies: List[TradingStrategyModel] = self.investflyApi.strategyApi.getStrategies()
        strategiesDictList = list(map(lambda model: str({'strategyId': model.strategyId,  'strategyName': model.strategyName}), strategies))
        return "\n".join(strategiesDictList)

    def __copySamples(self, args: argparse.Namespace) -> str:
        samplesPath = inspect.getfile(samples)
        path = Path(samplesPath)
        parentPath = path.parent
        shutil.copytree(parentPath, './samples', dirs_exist_ok=True)
        return "Samples copied to ./samples directory"

    def __createStrategy(self, args: argparse.Namespace) -> str:
        name = args.name
        path = args.file
        with open(path, 'r') as source_file:
            code = source_file.read()
        tradingStrategyModel = TradingStrategyModel(strategyName=name, strategyDesc=name, pythonCode=code)
        tradingStrategyModel = self.investflyApi.strategyApi.createStrategy(tradingStrategyModel)
        return f'Created strategy {tradingStrategyModel.strategyId}'

    def __updateCode(self, args: argparse.Namespace) -> str:
        strategyId = int(args.id)
        path = args.file
        with open(path, 'r') as source_file:
            code = source_file.read()
        self.investflyApi.strategyApi.updateStrategyCode(strategyId, code)
        return 'Code Updated'

    def __exitAction(self, args: argparse.Namespace|None) -> None:
        if self.investflyApi.isLoggedIn():
            self.investflyApi.logout()
        self.running = False

    def runCli(self) -> None:
        parser = argparse.ArgumentParser(prog="investfly-cli")
        subparser = parser.add_subparsers(help='Available Commands', dest="command")

        parser_login = subparser.add_parser('login', help='Login to Investfly')
        parser_login.add_argument('-u', '--username', required=True, help='Input username')
        parser_login.add_argument('-p', '--password', required=True, help='Input user password')
        parser_login.set_defaults(func=self.__loginAction)

        parser_logout = subparser.add_parser('logout', help="Logout from Investfly")
        parser_logout.set_defaults(func=self.__logoutAction)

        parser_listStrategies = subparser.add_parser('listStrategies', help='List Python Strategies')
        parser_listStrategies.set_defaults(func=self.__listStrategies)

        parser_copySamples = subparser.add_parser('copySamples', help='Copy Samples from SDK')
        parser_copySamples.set_defaults(func=self.__copySamples)

        parser_createStrategy = subparser.add_parser('createStrategy', help='Create a new trading strategy')
        parser_createStrategy.add_argument('-n', '--name', required=True, help='Strategy Name')
        parser_createStrategy.add_argument('-f', '--file', required=True, help='Python File Path relative to the project root that contains strategy code')
        parser_createStrategy.set_defaults(func=self.__createStrategy)

        parser_updateCode = subparser.add_parser('updateStrategyCode', help='Update strategy Python Code')
        parser_updateCode.add_argument('-i', '--id', required=True, help='Strategy ID')
        parser_updateCode.add_argument('-f', '--file', required=True, help='Python File Path relative to the project root that contains strategy code')
        parser_updateCode.set_defaults(func=self.__updateCode)


        parser_exit = subparser.add_parser('exit', help='Stop and Exit CLI')
        parser_exit.set_defaults(func = self.__exitAction)

        while self.running:
            try:
                data = input("\ninvestfly-cli$ ")
                args = parser.parse_args(data.split())
                if args.command is None:
                    # When user hits Enter without any command
                    parser.print_help()
                else:
                    result = args.func(args)
                    if result is not None:
                        print(result)
            except SystemExit:
                # System exit is caught because when -h is used, argparser displays help and exists the apputils with SystemExit
                pass
            except KeyboardInterrupt:
                self.__exitAction(None)
            except Exception as e:
                print("Received exception " + str(e))



def main():
    investflyCli = InvestflyCli()
    investflyCli.runCli()

    # # Check to see if user already has a session active
    # if os.path.exists('/tmp/loginSession'):
    #     tmpfile = open('/tmp/loginSession', 'rb')
    #     restApi = pickle.load(tmpfile)
    #     tmpfile.close()
    # else:
    #     restApi = StrategyApiClient("https://api.investfly.com")
    #
    # # CLI Commands
    # parser = argparse.ArgumentParser()
    # subparser = parser.add_subparsers(dest='command')
    #
    # parser_login = subparser.add_parser('login', help='Login to Investfly')
    # parser_login.add_argument('-u', '--username', required='true', help='Input username')
    # parser_login.add_argument('-p', '--password', required='true', help='Input user password')
    #
    # subparser.add_parser('whoami', help='View your user information')
    #
    # subparser.add_parser('logout', help='Logout')
    #
    # parser_strategy = subparser.add_parser('strategy', help='View all your current strategies')
    # parser_strategy.add_argument('-id', help='Provide the Strategy ID')
    # parser_strategy.add_argument('-o', '--output-file', help='Provide a location to save the output file of a custom strategy (Requires Strategy ID)')
    # parser_strategy.add_argument('-u', '--update-file', help='Provide the file location to update the script of a custom strategy (Requires Strategy ID)')
    #
    # args = parser.parse_args()
    #
    # # If user is logging in, create a new login session and save it locally
    # if args.command == 'login':
    #     restApi.login(args.username, args.password)
    #     tmpFile = open('/tmp/loginSession', 'ab')
    #     pickle.dump(restApi, tmpFile)
    #     tmpFile.close()
    #
    # elif args.command == 'logout':
    #     restApi.logout()
    #     os.remove('/tmp/loginSession')
    #
    # elif args.command == 'whoami':
    #     restApi.getStatus()
    #
    # elif args.command == 'strategy':
    #     if all(e is None for e in [args.id, args.output_file, args.update_file]):
    #         restApi.getStrategies()
    #     elif (args.output_file is not None) and (args.id is not None):
    #         try:
    #             code = restApi.saveStrategy(args.id)
    #             file = open(args.output_file, "w")
    #             file.write(code)
    #             file.close()
    #             print('File successfully saved to '+args.output_file)
    #         except Exception as e:
    #             print(e)
    #     elif (args.update_file is not None) and (args.id is not None):
    #         try:
    #             file = open(args.update_file, "r")
    #             code = file.read()
    #             restApi.updateStrategy(args.id, code)
    #             file.close()
    #         except Exception as e:
    #             print(e)
    #     else:
    #         parser_strategy.print_help()
    #
    #
    # else:
    #     parser.print_help()


if __name__ == '__main__':
    #main()
    print(inspect.getfile(samples))