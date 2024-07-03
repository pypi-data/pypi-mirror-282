from web3 import Web3
from whw.tokens.contract import TokenContract
from typing import Any, Dict

class Tokens(dict):
    def __init__(self, web3: Web3, security: Any) -> None:
        """
        Initializes the Tokens container with a Web3 provider and a Security object.
        """
        self._web3 = web3
        self._security = security
        super().__init__()

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Sets a token contract in the container.
        """
        if isinstance(value, TokenContract):
            super().__setitem__(key, value)
        else:
            raise TypeError("Value must be of type TokenContract")

    def __getitem__(self, key: Any) -> TokenContract:
        """
        Gets a token contract from the container.
        """
        if key in self:
            return super().__getitem__(key)
        raise KeyError(f"Token '{key}' not found")

    def get(self, key: Any, default: Any = None) -> TokenContract:
        """
        Gets a token contract from the container with a default value.
        """
        return super().get(key, default)
    
    def update_tokens(self) -> None:
        """
        Updates the information for all tokens in the container.
        """
        try:
            for addr, token in self.items():
                token_balance = token.balance(self._security)
                token_price = token.get_token_price()
                self[addr]['balance'] = token_balance
                self[addr]['price'] = token_price
                self[addr]['value'] = token_balance * token_price
        except Exception as e:
            raise Exception(f"Error updating tokens: {e}") from e
