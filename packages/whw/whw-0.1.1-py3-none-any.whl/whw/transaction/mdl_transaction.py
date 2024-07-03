from whw.transaction.transaction import TransactionHistory
from typing import Dict, Any

class ModelTransactionReceipt(dict):
    def __init__(self, transaction_history: TransactionHistory, res_transaction: Dict[str, Any]) -> None:
        """
        Initializes the ModelTransactionReceipt with transaction details and receipt information.

        Args:
            transaction_history (TransactionHistory): An instance of TransactionHistory containing transaction receipts.
            res_transaction (Dict[str, Any]): A dictionary containing the transaction hash and build transaction details.
        """
        super().__init__()

        # Validate res_transaction contains necessary keys
        if 'build_transaction' not in res_transaction or 'hash_transaction' not in res_transaction:
            raise ValueError("res_transaction must contain 'build_transaction' and 'hash_transaction' keys")

        # Initialize the receipt model with build transaction and transaction receipt details
        self['build_transaction'] = res_transaction['build_transaction']
        self['transaction_receipt'] = transaction_history.history.get(res_transaction['hash_transaction'])

        if self['transaction_receipt'] is None:
            raise ValueError(f"No transaction receipt found for hash {res_transaction['hash_transaction']}")
