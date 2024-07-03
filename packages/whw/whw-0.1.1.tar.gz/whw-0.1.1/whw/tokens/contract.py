from web3.contract import Contract
from web3 import Web3
from typing import Any, Literal, Dict, Tuple
from decimal import Decimal
from whw.security.security import Security
from whw.tokens.utils import TokenUtils as wu
from whw.transaction.transaction import TransactionHistory
from whw.transaction.mdl_transaction import ModelTransactionReceipt

class TokenContract:
    def __init__(
            self,
            wallet_provider: Web3,
            addr_contract: str,
            abi_contract: dict,
            wallet_infos: Any
    ) -> None:
        self._web3 = wallet_provider
        self._addr_contract = addr_contract
        self._abi_contract = abi_contract
        self.contract = self.__connect_contract()
        self.wallet_infos = wallet_infos
        self.transactions = TransactionHistory(self._web3)
        self.__name, self.__symbol = self.__connect_infos()

    def __connect_infos(self) -> Tuple[str, str]:
        """
        Connects to the contract to retrieve its name and symbol.
        """
        try:
            name = self.contract.functions.name().call()
            symbol = self.contract.functions.symbol().call()
            return name, symbol
        except Exception as e:
            raise Exception("Error retrieving contract information") from e

    def __connect_contract(self) -> Contract:
        """
        Connects to the smart contract.
        """
        try:
            return self._web3.eth.contract(
                address=self._web3.to_checksum_address(self._addr_contract),
                abi=self._abi_contract)
        except Exception as e:
            raise Exception("Error connecting to contract") from e

    def balance(self, security: Security) -> Decimal:
        """
        Retrieves the balance of the specified security.
        """
        try:
            return Decimal(self.contract.functions.balanceOf(security.addr_ethereum).call())
        except Exception as e:
            raise Exception("Error retrieving balance") from e

    def transfer(
            self,
            security: Security,
            amount_token: Decimal,
            to: str,
            speed: Literal['fast', 'average', 'slow'] = 'fast'
    ) -> ModelTransactionReceipt:
        """
        Transfers tokens from the security to the specified address.
        """
        try:
            res = wu.build_transaction_transfer(
                self._web3,
                self.contract,
                security,
                to,
                amount_token,
                speed)
            self.transactions._wait_transaction(res)
            self.wallet_infos.update_infos()
            return ModelTransactionReceipt(self.transactions, res)
        except Exception as e:
            raise Exception("Error transferring tokens") from e

    def approve(
            self,
            security: Security,
            spender: str,
            amount_token: Decimal,
            speed: Literal['fast', 'average', 'slow'] = 'fast'
    ) -> ModelTransactionReceipt:
        """
        Approves the specified amount of tokens for the spender.
        """
        try:
            res = wu.build_transaction_approve(
                self._web3,
                self.contract,
                security,
                spender,
                amount_token,
                speed)
            self.transactions._wait_transaction(res)
            self.wallet_infos.update_infos()
            return ModelTransactionReceipt(self.transactions, res)
        except Exception as e:
            raise Exception("Error approving tokens") from e

    def transfer_from(
            self,
            security: Security,
            sender: str,
            recipient: str,
            amount_token: Decimal,
            speed: Literal['fast', 'average', 'slow'] = 'fast'
    ) -> ModelTransactionReceipt:
        """
        Transfers tokens from the sender to the recipient using the allowance mechanism.
        """
        try:
            res = wu.build_transaction_transfer_from(
                self._web3,
                self.contract,
                security,
                sender,
                recipient,
                amount_token,
                speed)
            self.transactions._wait_transaction(res)
            self.wallet_infos.update_infos()
            return ModelTransactionReceipt(self.transactions, res)
        except Exception as e:
            raise Exception("Error transferring tokens from") from e

    def allowance(self, owner: str, spender: str) -> Decimal:
        """
        Retrieves the allowance of tokens that the spender is allowed to transfer on behalf of the owner.
        """
        try:
            return Decimal(self.contract.functions.allowance(owner, spender).call())
        except Exception as e:
            raise Exception("Error retrieving allowance") from e

    def get_token_price(self) -> Decimal:
        """
        Retrieves the current price of the token from the contract.
        """
        try:
            price = self.contract.functions.getPrice().call()
            return Decimal(price)
        except Exception as e:
            raise Exception("Error retrieving token price") from e

    @property
    def name(self) -> str:
        """
        Returns the name of the token.
        """
        return self.__name

    @property
    def symbol(self) -> str:
        """
        Returns the symbol of the token.
        """
        return self.__symbol
