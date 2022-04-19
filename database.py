import requests
import warnings
from hg0428db.errors import *


class DataBase:
    def __init__(self,
                 token,
                 undefined: str = 'warn',
                 undefined_return=None,
                 undefined_deletion='error'):
        self.undefined_deletion = undefined_deletion
        self.undefined = undefined
        self.undefined_return = undefined_return
        self.token = token
        self.accessCode = None
        self.temp = None
        self.authorized = False

    def request(self, endpoint, json={}, headers={}):
        json.update({'auth': self.accessCode})
        headers.update({
            'TOKEN': self.token,
            'Content-Type': 'application/json',
            'TEMPORARY-ACCESS-KEY': str(self.temp)
        })
        try:
            data = requests.post('https://DB-API.hg0428.repl.co/' + endpoint,
                                 headers=headers,
                                 json=json)
            if data.status_code == 502 or data.status_code == 404:
                if data.status_code == 502: msg = '502: The API is offline'
                else: msg = "error in the program 404"
                warnings.warn(
                    f'There was an error in the program. Report this to the developers: {msg}'
                )
                return
            return data.json()
        except:
            raise HTTPError(f'{data.status_code}: {data.reason}')

    def authorize(self, code):
        self.accessCode = code
        data = self.request('auth')
        if data['error'] == 'null':
            self.temp = data['temp']
        else:
            raise AuthenticationError(data['error'])

    def __getitem__(self, key):
        result = self.request('get', {
            'key': key,
            'default': self.undefined_return
        })
        if result['error'] != 'null':
            if result['message'].lower().startswith('access denied'):
                raise AuthenticationError(
                    f"{result['message']}: {result['error']}")
            elif result['message'].lower().startswith('error'):
                raise DataError(f"{result['message']}: {result['error']}")
        if result['message'].lower().startswith('undefined'):
            if self.undefined == 'warn':
                warnings.warn(
                    f"{key} is not defined. Returned None. \nAdd undefined='error' argument to instead raise an error. \nAdd undefined='ignore' to stop these warnings.\nTo set a custom return on undefined, set the undefined_return argument.",
                    UndefinedWarning)
            elif self.undefined == 'error':
                try:
                    raise UndefinedError(
                        f"{key} is not defined. \nAdd undefined='warn' argument to instead raise an warning. \nAdd undefined='ignore' to stop these errors.\nTo set a custom return on undefined, set the undefined_return argument."
                    )
                finally:
                    self.end()
        return result['return']
        #db[key]

    def __setitem__(self, key, value):
        result = self.request('set', {'key': key, 'value': value})
        if result['error'] != 'null':
            if result['message'].lower().startswith('access denied'):
                raise AuthenticationError(
                    f"{result['message']}: {result['error']}")
            elif result['message'].lower().startswith('error'):
                raise DataError(f"{result['message']}: {result['error']}")
        #db[key] = value

    def __delitem__(self, key):
        result = self.request('delete', {'key': key})
        if result['error'] != 'null':
            if result['message'].lower().startswith('access denied'):
                raise AuthenticationError(
                    f"{result['message']}: {result['error']}")
            elif result['message'].lower().startswith('error'):
                raise DataError(f"{result['message']}: {result['error']}")
        if result['message'].lower().startswith('undefined'):
            if self.undefined_deletion == 'error':
                try:
                    raise UndefinedError(
                        f"{key} is not defined. \nAdd undefined_deletion='ignore' argument to ignore these errors."
                    )
                finally:
                    self.end()
        #del db[key]

    def __missing__(self, key):
        pass  #db[key] in the case db doesn't have key

    def keys(self):
        result = self.request('list', {})
        if result['error'] != 'null':
            if result['message'].lower().startswith('access denied'):
                raise AuthenticationError(
                    f"{result['message']}: {result['error']}")
            elif result['message'].lower().startswith('error'):
                raise DataError(f"{result['message']}: {result['error']}")
        self.allKeys = result['keys']
        return self.allKeys

    def __contains__(self, key):
        result = self.request('list', {})
        if result['error'] != 'null':
            if result['message'].lower().startswith('access denied'):
                raise AuthenticationError(
                    f"{result['message']}: {result['error']}")
            elif result['message'].lower().startswith('error'):
                raise DataError(f"{result['message']}: {result['error']}")
        self.allKeys = result['keys']
        return key in self.allKeys
        #item in db

    def __len__(self):
        result = self.request('list', {})
        if result['error'] != 'null':
            if result['message'].lower().startswith('access denied'):
                raise AuthenticationError(
                    f"{result['message']}: {result['error']}")
            elif result['message'].lower().startswith('error'):
                raise DataError(f"{result['message']}: {result['error']}")
        self.allKeys = result['keys']
        return len(self.allKeys)
        #len(db)
    def toDict(self):
        result = self.request('json', {})
        if result['error'] != 'null':
            if result['message'].lower().startswith('access denied'):
                raise AuthenticationError(
                    f"{result['message']}: {result['error']}")
            elif result['message'].lower().startswith('error'):
                raise DataError(f"{result['message']}: {result['error']}")
        self.dict = result['json']
        return self.dict
        #db.toDict
    def __iter__(self):
        for k in self.keys():
            yield k, self[k]

    def __next__(self):
        pass  #db.next()

    def __reversed__(self):
        pass  #return a reverse iter

    def __call__(self):
        pass  #db()

    def __add__(self, other):
        pass  #db + other

    def __sub__(self, other):
        pass  #db - other

    def __eq__(self, other):
        pass  #db == otherdb

    def __ne__(self, other):
        pass  #db != otherdb

    def __bool__(self):
        pass  #if db:

    def __str__(self):
        pass  #print(db)

    def __enter__(self):
        pass  #begining of a with block

    def __exit__(self, *args):
        self.request('end', headers={'TERMPORARY-ACCESS-KEY': str(self.temp)})
        #args gives a ton of unneeded info.
        #add the end connection request here

    def end(self):
        self.request('end', headers={'TERMPORARY-ACCESS-KEY': str(self.temp)})
        # was __del__ but there is a bug with requests and __del__ so had to be removed.