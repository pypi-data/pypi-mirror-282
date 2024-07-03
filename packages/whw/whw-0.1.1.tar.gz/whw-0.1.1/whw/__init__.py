from whw.security.security import Security
from whw.security.config import WriteSecurity, LoadKeySecurity, OptionsSecurity, GeneratePrivateKey
from whw.transaction.transaction import TransactionHistory
from whw.transaction.mdl_transaction import ModelTransactionReceipt
from whw.wallet.utils import WalletUtils
from whw.wallet.wallet import WalletEth, Wallet
from whw.infos_wallet.infos import Infos
from whw.tokens.tokens import TokenContract, Tokens
from whw.tokens.utils import TokenUtils

from pathlib import Path
from typing import Literal, Union, Optional

global HTTP_PROVIDER

HTTP_PROVIDER = {
    "LOCALHOST": "http://127.0.0.1:7545"
}

def set_provider(name_provider: str, new_provider: str) -> None:
    """
    Sets a new HTTP provider.
    
    Args:
        name_provider (str): The name of the provider.
        new_provider (str): The URL of the new provider.
    """
    global HTTP_PROVIDER
    HTTP_PROVIDER[name_provider] = new_provider

def create_option(
        service: Literal['import', 'create'],
        key: Optional[str] = None,
        path_key: Optional[Union[Path, str]] = None) -> OptionsSecurity:
    """
    Creates an OptionsSecurity object.
    
    Args:
        service (Literal['import', 'create']): The service type.
        key (str, optional): The private key.
        path_key (Union[Path, str], optional): The path to the key file.
    
    Returns:
        OptionsSecurity: The created OptionsSecurity object.
    """
    return OptionsSecurity(service, key, path_key)

def get_security(options: OptionsSecurity, name: Optional[str] = None) -> Security:
    """
    Returns a Security object.
    
    Args:
        options (OptionsSecurity): The options for security.
        name (str, optional): The name for the security object.
    
    Returns:
        Security: The created Security object.
    """
    return Security(options, name)

def get_wallet(security: Security, http_provider: str) -> Wallet:
    """
    Returns a Wallet object.
    
    Args:
        security (Security): The security object.
        http_provider (str): The HTTP provider URL.
    
    Returns:
        Wallet: The created Wallet object.
    """
    return Wallet(security, http_provider)


class WalletProvider(Wallet):
    def __init__(
            self,
            http_provider: str, 
            name: str, 
            service: Literal['import', 'create'], 
            key: Optional[str] = None, 
            key_path: Optional[str] = None
    ) -> None:
        self.name = name
        options = OptionsSecurity(service, key, key_path)
        security = Security(options, name)
        super().__init__(security, http_provider)

    @staticmethod
    def get_wallet(
        http_provider: str,
        service: Literal['import', 'create'],
        key: Optional[str] = None,
        key_path: Optional[str] = None,
        name: Optional[str] = None
    ) -> Wallet:
        """
        Static method to create and return a Wallet object.
        
        Args:
            http_provider (str): The HTTP provider URL.
            service (Literal['import', 'create']): The service type.
            key (str, optional): The private key.
            key_path (str, optional): The path to the key file.
            name (str, optional): The name for the security object.
        
        Returns:
            Wallet: The created Wallet object.
        """
        options = OptionsSecurity(service, key, key_path)
        security = Security(options, name)
        return Wallet(security, http_provider)


    def __repr__(self) -> str:
        return f"WalletProvider(name={self.name}, addr={self.security.addr_ethereum})"