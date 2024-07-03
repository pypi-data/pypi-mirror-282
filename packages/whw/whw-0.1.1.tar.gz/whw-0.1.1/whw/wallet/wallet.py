from decimal import Decimal
from typing import Literal, Dict, Any
from whw.wallet.wallet_eth import WalletEth
from whw.tokens.contract import TokenContract
from whw.tokens.tokens import Tokens
from whw.security.security import Security
from web3 import Web3


class Wallet(WalletEth):
    def __init__(self, security: Security, http_provider: str) -> None:
        """
        Initializes the Wallet instance with a security object and an HTTP provider.
        Args:
            security (Security): An instance of the Security class containing private key information.
            http_provider (str): The HTTP provider URL to connect to the Ethereum network.
        """
        super().__init__(security, http_provider)
        self.tokens = Tokens(self.web3, security)

    def add_token(self, addr: str, abi: Dict[str, Any]) -> None:
        """
        Adds a new token contract to the wallet.
        Args:
            addr (str): The address of the token contract.
            abi (Dict[str, Any]): The ABI of the token contract.
        """
        try:
            contract = TokenContract(self.web3, addr, abi, self.infos)
            self.tokens[contract.name] = contract
            self.infos.update_infos()
        except Exception as e:
            raise Exception(f"Error adding token: {e}") from e

    def update_token_infos(self) -> None:
        """
        Updates information for all tokens in the wallet.
        """
        try:
            self.tokens.update_tokens()
            self.infos.update_infos()
        except Exception as e:
            raise Exception(f"Error updating token infos: {e}") from e
