from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from functools import partial
from github import GitHub
import keyring

from . import __version__

class Dripstone:
    def __init__ (self):
        self.github = GitHub(self.token)        

    @property
    def token (self): return keyring.get_password('dripstone', 'token')
    
    @token.setter
    def token (self, value): keyring.set_password('dripstone', 'token', value)

    @token.deleter
    def token (self): keyring.delete_password('dripstone', 'token')

def main ():
    parser = ArgumentParser(
        description='Make GitHub labels from definitions in JSON, YAML, or TOML',
        prog='dripstone',
        fromfile_prefix_chars='@',
        formatter_class=ArgumentDefaultsHelpFormatter)
    argument = parser.add_argument
    argument('-t', '--token', help='GitHub access token')
    argument('-V', '--version', action='version', version=f'%(prog)s {__version__}')
    argument('--no-store', action='store_true', help='Do not store GitHub API Token')
    argument('--wipe', action='store_true', help='Delete stored GitHub API Token on exit')
    argument('--hostname', help='GitHub API v3 host', default='github.com')
    args = parser.parse_args()

#    stone = Dripstone()

    if not args.token:
        args.token = os.environ.get('GITHUB_API_TOKEN', keyring.get_password('dripstone', 'token'))
    hub = GitHub(base_url=f'https://{args.hostname}/api/v3')

__name__ == '__main__' and main()
