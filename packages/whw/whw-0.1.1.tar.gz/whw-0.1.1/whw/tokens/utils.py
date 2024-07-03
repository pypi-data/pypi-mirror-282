from web3 import Web3
from web3.contract import Contract
from decimal import Decimal
from typing import Literal, Dict, Any

from whw.security.security import Security
from whw.wallet.utils import WalletUtils as wu

class TokenUtils:
    @staticmethod
    def estimate_gas_for_buy(
        contract: Contract,
        addr: str,
        value: Decimal,
        nonce: int
    ) -> int:
        """
        Estimates the gas required to buy tokens from a contract.
        """
        value_in_wei = Web3.to_wei(value, "ether")
        return contract.functions.buyTokens().estimate_gas(
            {'from': addr,
             "value": value_in_wei,
             "nonce": nonce}
        )
    
    @staticmethod
    def estimate_gas_transfer(
        contract: Contract,
        addr: str,
        to: str,
        value: Decimal
    ) -> int:
        """
        Estimates the gas required to transfer tokens.
        """
        return contract.functions.transfer(to, int(value)
            ).estimate_gas({'from': addr})

    @staticmethod
    def build_tx(_from: str, **kwargs) -> dict:
        """
        Builds a transaction dictionary with the given parameters.
        """
        kwargs['from'] = _from
        return kwargs
    
    @staticmethod
    def build_transaction_transfer(
        web3: Web3,
        contract: Contract,
        security: Security,
        to: str,
        value: Decimal,
        speed: Literal['fast', 'average', 'slow'] = 'fast',
    ) -> dict:
        """
        Builds, signs, and sends a token transfer transaction.
        """
        try:
            gas_price = wu.get_gas_price(web3, speed)
            nonce = wu.get_nonce(web3, security)
            gas_limit = TokenUtils.estimate_gas_transfer(
                contract,
                security.addr_ethereum,
                to,
                value)
            tx_params = TokenUtils.build_tx(
                _from=security.addr_ethereum,
                nonce=nonce,
                gas=gas_limit,
                gasPrice=gas_price,
                chainId=web3.eth.chain_id)
            tx = contract.functions.transfer(to, int(value)
                ).build_transaction(tx_params)        
            signed_tx = wu.sign_transaction(security, tx)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return {
                'hash_transaction': tx_hash.hex(),
                "build_transaction": tx_params
            }
        except Exception as e:
            raise Exception("Error building or sending transaction") from e

    @staticmethod
    def build_transaction_approve(
        web3: Web3,
        contract: Contract,
        security: Security,
        spender: str,
        value: Decimal,
        speed: Literal['fast', 'average', 'slow'] = 'fast',
    ) -> dict:
        """
        Builds, signs, and sends a token approve transaction.
        """
        try:
            gas_price = wu.get_gas_price(web3, speed)
            nonce = wu.get_nonce(web3, security)
            gas_limit = contract.functions.approve(spender, int(value)).estimate_gas(
                {'from': security.addr_ethereum}
            )
            tx_params = TokenUtils.build_tx(
                _from=security.addr_ethereum,
                nonce=nonce,
                gas=gas_limit,
                gasPrice=gas_price,
                chainId=web3.eth.chain_id)
            tx = contract.functions.approve(spender, int(value)).build_transaction(tx_params)
            signed_tx = wu.sign_transaction(security, tx)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return {
                'hash_transaction': tx_hash.hex(),
                "build_transaction": tx_params
            }
        except Exception as e:
            raise Exception("Error building or sending approve transaction") from e

    @staticmethod
    def build_transaction_transfer_from(
        web3: Web3,
        contract: Contract,
        security: Security,
        sender: str,
        recipient: str,
        value: Decimal,
        speed: Literal['fast', 'average', 'slow'] = 'fast',
    ) -> dict:
        """
        Builds, signs, and sends a token transferFrom transaction.
        """
        try:
            gas_price = wu.get_gas_price(web3, speed)
            nonce = wu.get_nonce(web3, security)
            gas_limit = contract.functions.transferFrom(sender, recipient, int(value)).estimate_gas(
                {'from': security.addr_ethereum}
            )
            tx_params = TokenUtils.build_tx(
                _from=security.addr_ethereum,
                nonce=nonce,
                gas=gas_limit,
                gasPrice=gas_price,
                chainId=web3.eth.chain_id)
            tx = contract.functions.transferFrom(sender, recipient, int(value)).build_transaction(tx_params)
            signed_tx = wu.sign_transaction(security, tx)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return {
                'hash_transaction': tx_hash.hex(),
                "build_transaction": tx_params
            }
        except Exception as e:
            raise Exception("Error building or sending transferFrom transaction") from e

    @staticmethod
    def get_token_price(contract: Contract) -> Decimal:
        """
        Retrieves the current price of the token. Assumes the contract has a `getPrice` function.
        """
        try:
            price = contract.functions.getPrice().call()
            return Decimal(price)
        except Exception as e:
            raise Exception("Error retrieving token price") from e
