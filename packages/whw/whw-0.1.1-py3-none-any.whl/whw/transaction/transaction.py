import whw.wallet.utils as wu
import threading
from web3 import Web3
from typing import Any, Dict
from decimal import Decimal

class TransactionHistory(dict):
    def __init__(self, web3: Web3, *args: Any, **kwargs: Any) -> None:
        self._web3 = web3
        self.history = {}
        super().__init__(*args, **kwargs)
        self['history'] = self.history

    def _wait_transaction(self, transaction_info: Dict[str, Any]) -> None:
        """
        Initiates the waiting process for a transaction receipt and starts a thread to handle it.
        """
        tx_hash = transaction_info["hash_transaction"]
        self.__build_transaction(transaction_info)
        self.history[tx_hash]['loading'] = True
        receipt_thread = threading.Thread(target=self.__receipt_transaction, args=(tx_hash,))
        receipt_thread.start()

    def __build_transaction(self, transaction_info: Dict[str, Any]) -> None:
        """
        Builds the transaction details and stores them in the history.
        """
        tx_hash = transaction_info["hash_transaction"]
        if tx_hash not in self.history:
            self.history[tx_hash] = {
                'loading': False,
                'validated': False,
                'receipt': None,
                'details': {
                    'to': transaction_info['build_transaction']['to'],
                    'value': transaction_info['build_transaction']['value'],
                    'gas_price': transaction_info['build_transaction']['gasPrice'],
                    'gas_limit': transaction_info['build_transaction']['gas'],
                    'nonce': transaction_info['build_transaction']['nonce'],
                    'tx_hash': tx_hash
                }
            }

    def __receipt_transaction(self, tx_hash: str) -> None:
        """
        Waits for the transaction receipt and updates the history.
        """
        receipt = wu.WalletUtils.receipt_transaction(self._web3, tx_hash)
        self.history[tx_hash]['receipt'] = receipt
        self.history[tx_hash]['validated'] = True
        self.history[tx_hash]['loading'] = False
