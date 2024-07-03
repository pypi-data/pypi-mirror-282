from web3 import Web3
from decimal import Decimal, ROUND_DOWN
import requests
from typing import Dict, Any

from whw.infos_wallet.config import ROUNDING_PRECISION, PRICE_ETH
from whw.security.security import Security
from whw.tokens.contract import TokenContract
from whw.tokens.tokens import Tokens  # Assurez-vous d'importer la classe Tokens

class Infos(dict):
    ether_price = PRICE_ETH
    
    def __init__(self, web3: Web3, security: Security, *args, **kwargs) -> None:
        self._web3 = web3
        self._security = security
        self.tokens = Tokens(web3, security)  # Initialisation des tokens
        super().__init__(*args, **kwargs)
        self._initialisation_eth()
        self.update_infos()

    def _initialisation_eth(self) -> None:
        """
        Initializes the Ethereum balance and sold information.
        """
        self['eth'] = {}
        self['eth']['sold'] = {}
        self['eth']['balance'] = Decimal('0')

    def _initialisation_tokens(self) -> None:
        """
        Initializes the token balances and sold information.
        """
        self['tokens'] = {}
        self['tokens']['balances'] = {}
        self['tokens']['sold'] = {}

    def __balance_eth(self) -> None:
        """
        Retrieves and sets the balance of Ethereum for the given security address.
        """
        try:
            balance_wei_eth = self._web3.eth.get_balance(self._security.addr_ethereum)
            balance_eth = Decimal(self._web3.from_wei(balance_wei_eth, "ether")).quantize(ROUNDING_PRECISION, rounding=ROUND_DOWN)
            self['eth']['balance'] = balance_eth
        except Exception as e:
            raise Exception("Error retrieving Ethereum balance") from e
    
    def __sold_eth(self) -> None:
        """
        Calculates and updates the sold value of Ethereum based on current prices.
        """
        try:
            ether_balance = self['eth']['balance']
            ether_price = Infos.ether_price

            for k, v in ether_price.items():
                decimal_value = Decimal(v)
                self['eth']['sold'][k] = (ether_balance * decimal_value).quantize(ROUNDING_PRECISION, rounding=ROUND_DOWN)
        except Exception as e:
            raise Exception("Error calculating Ethereum sold value") from e

    def __init_eth_infos(self) -> None:
        """
        Initializes Ethereum balance and sold information.
        """
        self.__balance_eth()
        self.__sold_eth()

    def __balance_tokens(self) -> None:
        """
        Retrieves and sets the balances of all tokens for the given security address.
        """
        try:
            for addr, token in self.tokens.items():
                balance = token.balance(self._security)
                self['tokens']['balances'][addr] = balance
        except Exception as e:
            raise Exception("Error retrieving token balances") from e
    
    def __sold_tokens(self) -> None:
        """
        Calculates and updates the sold value of all tokens based on their current prices.
        """
        try:
            for addr, token in self.tokens.items():
                token_price = token.get_token_price()
                token_balance = self['tokens']['balances'][addr]
                self['tokens']['sold'][addr] = (token_balance * token_price).quantize(ROUNDING_PRECISION, rounding=ROUND_DOWN)
        except Exception as e:
            raise Exception("Error calculating token sold values") from e

    def update_eth(self) -> None:
        """
        Updates Ethereum balance and sold information.
        """
        self.__init_eth_infos()

    def update_tokens(self) -> None:
        """
        Updates token balances and sold information.
        """
        self.__balance_tokens()
        self.__sold_tokens()

    def update_infos(self) -> None:
        """
        Updates all information including Ethereum and tokens.
        """
        self.update_eth()
        self.update_tokens()
