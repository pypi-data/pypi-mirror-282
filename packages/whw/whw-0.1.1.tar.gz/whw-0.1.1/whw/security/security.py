from whw.security.config import LoadKeySecurity, OptionsSecurity, WriteSecurity
from web3 import Account
from typing import Literal, Any

class Security:
    """
    Class to manage security-related operations for Ethereum accounts
    """
    def __init__(
            self,
            options=OptionsSecurity,
            name_: str = None
    ) -> None:
        self.option = options
        self.__private_key = options['private_key']
        self.__account = None
        self.__name = name_ or "unknown"

        self.__connect_profile()        

    def __connect_profile(self) -> None:
        """
        Connects to the Ethereum account using the provided private key
        """
        account = Account.from_key(self.__private_key)
        self.__account = account

    def set_name(self, name: str) -> None:
        """
        Sets the name associated with this Security instance
        params: name (str)
        """
        self.__name = name

    @property
    def account(self) -> Any:
        """
        Returns the Ethereum account object
        return: Ethereum account object
        """
        return self.__account
    
    @property
    def addr_ethereum(self) -> str:
        """
        Returns the Ethereum address of the account
        return: Ethereum address (str)
        """
        return self.__account.address
    
    @property
    def private_key(self) -> Any:
        """
        Returns the private key associated with this account
        return: Private key (Any)
        """
        return self.__private_key
    
    @property
    def sign_transaction(self) -> Any:
        """
        Returns the function to sign transactions with this account
        return: Function to sign transactions (Any)
        """
        return self.__account.sign_transaction
    
    @property
    def format_frame(self) -> dict:
        """
        Returns a dictionary with the name and Ethereum address of the account
        return: Dictionary with account details (dict)
        """
        return {
            "NAME": self.__name,
            "ADDR": self.addr_ethereum
        }
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the Security instance
        return: String representation (str)
        """
        return f"Security(addr={self.addr_ethereum}, name={self.__name})"
