from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

from typing import Tuple, Literal, Optional, Union
from pathlib import Path
import os


class GeneratePrivateKey:
    """
    Class GeneratePrivateKey
        -> static method generate_private: Generates an EllipticCurvePrivateKey
    """
    @staticmethod
    def generate_private() -> ec.EllipticCurvePrivateKey:
        """
        Generates a new private key conforming to the Ethereum blockchain
        params: void
        return: EllipticCurvePrivateKey
        """
        try:
            private_key = ec.generate_private_key(ec.SECP256K1())
            return private_key
        except Exception as e:
            raise Exception("Error generating private key") from e


class LoadKeySecurity:
    """
    Class to load a private key and provide its hex representation
    """
    def __init__(self, private_key: ec.EllipticCurvePrivateKey = None) -> None:
        self.__private_key = private_key if private_key else self.__connect()
        self.__private_hex, self.__public_hex = self.__keys_to_hex()

    def __connect(self) -> ec.EllipticCurvePrivateKey:
        """
        Connects to the private key generator to create a new key if not provided
        return: EllipticCurvePrivateKey
        """
        try:
            private_key = GeneratePrivateKey.generate_private()
            return private_key
        except Exception as e:
            raise Exception("Error connecting to private key generator") from e

    def __keys_to_hex(self) -> Tuple[str, str]:
        """
        Converts the private and public keys to their hex representations
        return: Tuple containing hex representations of the private and public keys
        """
        private_key = self.__private_key.private_numbers().private_value.to_bytes(32, "big").hex()
        public_key = self.__private_key.public_key().public_bytes(
            encoding=serialization.Encoding.X962,
            format=serialization.PublicFormat.UncompressedPoint
        ).hex()
        return private_key, public_key

    @property
    def private_key(self) -> ec.EllipticCurvePrivateKey:
        return self.__private_key

    @property
    def private_key_hex(self) -> str:
        return self.__private_hex

    @property
    def public_key_hex(self) -> str:
        return self.__public_hex


class OptionsSecurity(dict):
    """
    Class to handle security options for creating or importing keys
    """
    def __init__(
            self, 
            service: Literal['create', 'import'], 
            key: Optional[str] = None, 
            path_key: Optional[Union[Path, str]] = None,
            *args, 
            **kwargs
            ) -> None:
        self.private_key = None
        self['private_key'] = None
        super().__init__(*args, **kwargs)
        if service == "create":
            self._option_create()
        else:
            self._option_import(key, path_key)

    def _option_import(self, key: Optional[str], path_key: Optional[Union[Path, str]]) -> None:
        """
        Handles importing a key from a given key string or path to a key file
        """
        if not key and not path_key:
            raise Exception("Import without key or file key")
        
        if key and not path_key:
            private_key = key
        elif path_key and not key:
            if isinstance(path_key, str):
                path_ = Path(path_key)
            else:
                path_ = path_key
            private_key = self.read_file(path_)
        self.private_key = private_key
        self['private_key'] = private_key

    def read_file(self, path_file: Path) -> str:
        """
        Reads a key from a file and returns its hex representation
        params: Path to the key file
        return: Hex representation of the key
        """
        try:
            if not path_file.exists():
                raise FileNotFoundError("File Not Found: " + str(path_file))
            filename = path_file.name.split('.')
            extension = filename[1]
            if extension == 'pem':
                with open(path_file, 'rb') as f:
                    brut_key = f.read()
                    private_key = serialization.load_pem_private_key(
                        brut_key,
                        password=None
                    )
                    format_private_key = LoadKeySecurity(private_key)
                    return format_private_key.private_key_hex
            elif extension in ["txt", "whw"]:
                with open(path_file, "r") as f:
                    format_private_key = f.read().strip()
                    return format_private_key
            else:
                raise Exception("Extension not supported")
        except Exception as e:
            raise e

    def _option_create(self) -> None:
        """
        Creates a new private key and stores its hex representation
        """
        try:
            private_key = GeneratePrivateKey.generate_private()
            load_s = LoadKeySecurity(private_key=private_key)
            self.private_key = load_s.private_key_hex
            self['private_key'] = load_s.private_key_hex
        except Exception as e:
            raise e


class WriteSecurity:
    extension_type = ['txt', 'whw']
    
    def __init__(self, options_security: OptionsSecurity = None, private_key: str = None) -> None:
        """
        Initializes the WriteSecurity class with either an OptionsSecurity object or a private key string
        """
        self.private_key = None
        if options_security and options_security['private_key']:
            self.private_key = options_security['private_key']
        if private_key:
            self.private_key = private_key
        if self.private_key is None:
            raise Exception("No options found to write")
        if options_security and private_key:
            if options_security['private_key']:
                pr_opt = options_security['private_key']
                if pr_opt == private_key:
                    self.private_key = private_key
                else:
                    self.private_key = pr_opt

    def write(self, filename: str) -> None:
        """
        Writes the private key to a file with the given filename
        params: filename
        """
        try:
            path_ = Path(os.getcwd()).joinpath(filename)
            if path_.exists():
                raise FileExistsError("Filename already exists: " + filename)
            self.verify_extension(filename)
        except Exception as e:
            raise e

    def verify_extension(self, filename: str) -> None:
        """
        Verifies that the file extension is supported
        params: filename
        """
        extension = filename.split(".")
        if len(extension) < 2:
            raise Exception("Extension not found: " + filename)
        extension = extension[1]
        if extension not in WriteSecurity.extension_type:
            raise Exception("Extension not supported: " + extension)
        self.wr_extension_valid(filename)

    def wr_extension_valid(self, filename: str) -> None:
        """
        Writes the private key to a file after verifying the extension
        params: filename
        """
        try:
            with open(filename, 'w') as f:
                f.write(self.private_key)
        except Exception as e:
            raise Exception("Error writing file: " + filename) from e
