from web3 import Web3
from web3.contract import Contract
from whw.security.security import Security
from decimal import Decimal
from typing import Literal, Dict, Any
import requests


class WalletUtils:
    ETHERSCAN_API_KEY = "V1P5278I5K7FJ4ABUN2AFC5PQ5NFAUCKJK"
    
    @staticmethod
    def get_gas_price(
        web3: Web3, 
        speed: Literal['fast', 'average', 'slow'] = 'fast'
    ) -> int:
        """
        Retrieves the current gas price from Etherscan based on the specified speed.
        """
        if speed not in ['slow', 'average', 'fast']:
            raise ValueError("Speed must be 'slow', 'average', or 'fast'.")
        
        etherscan_url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={WalletUtils.ETHERSCAN_API_KEY}"
        try:
            response = requests.get(etherscan_url)
            if response.status_code != 200:
                raise Exception(f"HTTP Error {response.status_code} while fetching gas price")
            
            try:
                data = response.json()
            except requests.exceptions.JSONDecodeError as e:
                raise Exception("Error decoding JSON response") from e
            
            prices = {
                'slow': int(data['result']['SafeGasPrice']),
                'average': int(data['result']['ProposeGasPrice']),
                'fast': int(data['result']['FastGasPrice'])
            }
            return web3.to_wei(prices[speed], 'gwei')
        except requests.RequestException as e:
            raise Exception("Error fetching gas price") from e

    @staticmethod
    def get_gas_limit(
        web3: Web3, 
        security: Security, 
        to: str, 
        amount: Decimal
    ) -> int:
        """
        Estimates the gas limit for a transaction.
        """
        return web3.eth.estimate_gas({
            'from': security.addr_ethereum,
            'to': to,
            'value': web3.to_wei(amount, "ether")
        })

    @staticmethod
    def get_nonce(
        web3: Web3, 
        security: Security
    ) -> int:
        """
        Retrieves the nonce for the given security's Ethereum address.
        """
        return web3.eth.get_transaction_count(security.addr_ethereum)

    @staticmethod
    def sign_transaction(
        security: Security, 
        tx: dict
    ) -> dict:
        """
        Signs a transaction using the security's private key.
        """
        return security.sign_transaction(tx)

    @staticmethod
    def receipt_transaction(
        web3: Web3, 
        tx_hash: str
    ) -> str:
        """
        Waits for the transaction receipt and returns the transaction hash.
        """
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.transactionHash.hex()
    
    @staticmethod
    def build_tx(
        _from: str = None,
        _to: str = None,
        _value: int = None,
        _gas: int = None,
        _gas_price: int = None,
        _nonce: int = None,
        **kwargs
    ) -> dict:
        """
        Builds a transaction dictionary with the provided parameters.
        """
        tx = {
            'from': _from,
            'to': _to,
            'value': _value,
            'gas': _gas,
            'gasPrice': _gas_price,
            'nonce': _nonce
        }
        if kwargs:
            tx.update(kwargs)

        return tx

    @staticmethod
    def optimize_gas_limit(
        web3: Web3, 
        security: Security, 
        tx: dict
    ) -> int:
        """
        Optimizes the gas limit for a transaction by adding a 20% safety margin.
        """
        estimated_gas = web3.eth.estimate_gas(tx)
        safety_margin = int(estimated_gas * 0.2)  # Add 20% safety margin
        return estimated_gas + safety_margin
    
    @staticmethod
    def build_transaction(
        web3: Web3, 
        security: Security, 
        to: str, 
        value: Decimal, 
        speed: Literal['fast', 'average', 'slow'] = 'fast',
    ) -> dict:
        """
        Builds, signs, and sends a transaction.
        """
        gas_price = WalletUtils.get_gas_price(web3, speed)
        gas_limit = WalletUtils.get_gas_limit(web3, security, to, value)
        nonce = WalletUtils.get_nonce(web3, security)

        tx = WalletUtils.build_tx(
            _from=security.addr_ethereum,
            _to=to,
            _value=web3.to_wei(value, 'ether'),
            _gas=gas_limit,
            _gas_price=gas_price,
            _nonce=nonce,
        )
        signed_tx = WalletUtils.sign_transaction(security, tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        response = {
            "hash_transaction": tx_hash,
            "build_transaction": tx,
        }
        return response
