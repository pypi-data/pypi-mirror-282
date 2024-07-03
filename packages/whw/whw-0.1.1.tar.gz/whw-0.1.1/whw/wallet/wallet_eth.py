from web3 import Web3
from web3.exceptions import ProviderConnectionError, TransactionNotFound, InvalidAddress, Web3ValidationError, ContractLogicError, Web3Exception
from decimal import Decimal
from typing import Literal, Dict, Any

from whw.security.security import Security
from whw.wallet.utils import WalletUtils
from whw.transaction.transaction import TransactionHistory
from whw.transaction.mdl_transaction import ModelTransactionReceipt
from whw.infos_wallet.infos import Infos


class WalletEth(dict):
    def __init__(self, security: Security, http_provider: str) -> None:
        """
        Initializes the WalletEth instance with a security object and an HTTP provider.
        Args:
            security (Security): An instance of the Security class containing private key information.
            http_provider (str): The HTTP provider URL to connect to the Ethereum network.
        """
        self.security = security
        self.__http_provider = http_provider
        self.web3 = None
        self.transactions = None
        self.infos = None
        super().__init__()
        self.__connect()

    def __connect(self) -> None:
        """
        Establishes connection to the Ethereum network using the provided HTTP provider.
        """
        try:
            self.web3 = Web3(Web3.HTTPProvider(self.__http_provider))
            if not self.web3.is_connected():
                raise ProviderConnectionError("Provider not valid")
            self.transactions = TransactionHistory(self.web3)
            self.infos = Infos(self.web3, self.security)
        except (ProviderConnectionError, Web3Exception, Exception) as e:
            raise ProviderConnectionError("Error connecting to the blockchain") from e

    def send(self, to: str, amount: Decimal, speed: Literal['fast', 'average', 'slow'] = 'fast') -> ModelTransactionReceipt:
        """
        Sends a transaction to the specified address with the given amount and speed.
        Args:
            to (str): The recipient's Ethereum address.
            amount (Decimal): The amount of Ether to send.
            speed (Literal['fast', 'average', 'slow']): The transaction speed preference.
        Returns:
            ModelTransactionReceipt: A model containing the transaction receipt.
        """
        try:
            res = WalletUtils.build_transaction(self.web3, self.security, to, amount, speed)
            self.transactions._wait_transaction(res)
            self.infos.update_infos()
            return ModelTransactionReceipt(self.transactions, res)
        except (TransactionNotFound, InvalidAddress, Web3ValidationError, ContractLogicError, Web3Exception) as e:
            raise Web3Exception("Transaction failed") from e

    def estimate_gas_cost(self, to: str, amount: Decimal, speed: Literal['fast', 'average', 'slow'] = 'fast') -> Dict[str, Any]:
        """
        Estimates the gas cost for a transaction.
        Args:
            to (str): The recipient's Ethereum address.
            amount (Decimal): The amount of Ether to send.
            speed (Literal['fast', 'average', 'slow']): The transaction speed preference.
        Returns:
            Dict[str, Any]: A dictionary containing the estimated gas cost in various currencies.
        """
        try:
            gas_price = WalletUtils.get_gas_price(self.web3, speed)
            gas_limit = WalletUtils.get_gas_limit(self.web3, self.security, to, amount)
            gas_cost_eth = gas_price * gas_limit
            gas_cost_eth = self.web3.from_wei(gas_cost_eth, "ether")

            ether_price = self.infos.ether_price

            gas_cost_btc = gas_cost_eth * Decimal(ether_price['BTC'])
            gas_cost_usd = gas_cost_eth * Decimal(ether_price['USD'])
            gas_cost_eur = gas_cost_eth * Decimal(ether_price['EUR'])
            return {
                'eth': gas_cost_eth,
                'btc': gas_cost_btc,
                'usd': gas_cost_usd,
                'eur': gas_cost_eur
            }
        except (TransactionNotFound, InvalidAddress, Web3ValidationError, ContractLogicError, Web3Exception) as e:
            raise Exception("Error estimating gas cost") from e

    def verify_addr(self, addr: str, raise_exception: bool = False) -> bool:
        """
        Verifies if the provided address is a valid Ethereum address.
        Args:
            addr (str): The Ethereum address to verify.
            raise_exception (bool): Whether to raise an exception if the address is invalid.
        Returns:
            bool: True if the address is valid, False otherwise.
        """
        try:
            if Web3.is_address(addr):
                return True
            if raise_exception:
                raise InvalidAddress("Invalid address")
            else:
                return False
        except (Web3Exception, Exception) as e:
            raise Exception("Error verifying address") from e
