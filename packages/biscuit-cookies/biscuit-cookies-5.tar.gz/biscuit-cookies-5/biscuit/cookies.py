from sqlite3 import IntegrityError
from PyQL3.shell import PyConnection
from base64 import b64decode
from pathlib import Path
from json import load
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData

CONV = \
    {'host_key': 'domain', 'name': 'name', 'value': 'value', 'path': 'path',
     'expires_utc': 'expires', 'is_secure': 'secure', 'is_httponly': 'httpOnly'}
DFLT = \
    {'creation_utc': '1577826000',
     'is_persistent': '1', }
REQS = \
    ('name', 'value', 'domain', 'path', 'expires')


def decrypt(key, encrypted_value):
    """
    RU: Расшифровывает зашифрованное значение с помощью предоставленного ключа.
    EN: Decrypts the encrypted value using the provided key.

    Args:
        key (bytes): The decryption key.
        encrypted_value (bytes): The value to be decrypted.

    Returns:
        str: The decrypted value as a string.
    """
    if not isinstance(encrypted_value, bytes):
        return None
    if not encrypted_value.startswith(b'v10'):
        return None
    iv = encrypted_value[3:15]
    encrypted_value = encrypted_value[15:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    return cipher.decrypt(encrypted_value)[:-16].decode()


class Biscuit:
    """
    RU: Класс для взаимодействия с куками в браузере пользователя.
    EN: A class to interact with cookies in a user's browser.

    Attributes:
        _user_data_dir (Path): The path to the user's data directory.
        _key (bytes): The decryption key.
        _conn (PyConnection): The connection to the database.
    """

    def __init__(self, user_data_dir, profile='Default'):
        """
        RU: Создает все необходимые атрибуты для объекта Biscuit.
        EN: Constructs all the necessary attributes for the Biscuit object.

        Args:
            user_data_dir (str): The path to the user's data directory.
            profile (str, optional): The user's profile. Defaults to 'Default'.
        """
        self._user_data_dir = Path(user_data_dir)

        local_state = self._user_data_dir / 'Local State'
        with open(local_state, "r", encoding='latin-1') as file:
            local_state = load(file)
        key = b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        self._key = CryptUnprotectData(key, None, None, None, 0)[1]

        cookies_path = self._user_data_dir / profile / 'Network' / 'Cookies'
        if not cookies_path.exists():
            raise FileNotFoundError(cookies_path)
        self._conn = PyConnection(cookies_path)

    def get(self, where=None, order=None, limit=None, offset=None):
        """
        RU: Извлекает файлы cookie из базы данных.
        EN: Retrieves cookies from the database.

        Args:
            where (str, optional): The WHERE clause for the SQL query. Defaults to None.
            order (str, optional): The ORDER BY clause for the SQL query. Defaults to None.
            limit (int, optional): The LIMIT clause for the SQL query. Defaults to None.
            offset (int, optional): The OFFSET clause for the SQL query. Defaults to None.

        Returns:
            list: A list of dictionaries representing the cookies.
        """
        rows = self._conn.get('cookies').rows
        columns = list(CONV.keys()) + ['encrypted_value']

        cookies = []
        for cookie in rows.deserialize(columns, where, order, limit, offset):
            decrypted_value = decrypt(self._key, cookie[-1])
            cookie = dict(zip(CONV.values(), cookie[:-1]))
            if decrypted_value:
                cookie['value'] = decrypted_value
            if not cookie.get('value', None):
                continue
            cookies.append(cookie)
        return cookies

    def add(self, cookies):
        """
        RU: Добавляет файлы cookie в базу данных.
        EN: Adds cookies to the database.

        Args:
            cookies (list): A list of dictionaries representing the cookies.
        """
        table = self._conn.get('cookies')
        columns = table.columns.ids
        for cookie in cookies:
            if not all(item in cookie for item in REQS):
                continue
            values = \
                [cookie[CONV[item]] if item in CONV.keys()
                 else DFLT.get(item, '') for item in columns]
            try:
                table.rows.insert(values=tuple(values))
            except IntegrityError:
                pass
        self._conn.commit()
