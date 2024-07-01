import aiohttp
import asyncio
import base64
from typing import List, TypedDict, Optional
from solana.transaction import VersionedTransaction, TransactionError
from solana.rpc.async_api import AsyncClient as Connection
from solana.rpc.commitment import Confirmed
from solana.keypair import Keypair
from solana.rpc.types import TxOpts
from solana.rpc.core import SendTransactionError
import base58

class SwapResponse(TypedDict):
    base64Transaction: str
    signers: List[str]

class Swap:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
    
    async def get_swap_raw(self, owner: str, from_mint: str, to_mint: str, amount: int, slippage: int, provider: str, pool: Optional[str] = None) -> SwapResponse:
        body = {
            'owner': owner,
            'fromMint': from_mint,
            'toMint': to_mint,
            'amount': amount,
            'slippage': slippage,
            'provider': provider,
            'pool': pool
        }

        headers = {
            'X-API-KEY': self.api_key
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/swap', params=body, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['data']
                else:
                    error_message = await response.text()
                    print(f'Error fetching swap data: {error_message}')
                    raise Exception('Failed to fetch swap data')
                
    async def get_swap(self, owner: str, from_mint: str, to_mint: str, amount: float, slippage: float, provider: str, pool: Optional[str] = None, from_mint_decimals: int = 9) -> SwapResponse:
        amount = amount * 10**from_mint_decimals  # convert to lamports
        slippage = slippage * 100  # convert to bps

        return await self.get_swap_raw(owner, from_mint, to_mint, int(amount), int(slippage), provider, pool)
    
    async def create_transaction(self, swap_transaction_data: str) -> VersionedTransaction:
        swap_transaction_buf = base64.b64decode(swap_transaction_data)
        return VersionedTransaction.deserialize(swap_transaction_buf)
    
    async def send_transaction(self, rpc_endpoint: str, transaction: VersionedTransaction, private_key: str, additional_signers: Optional[List[str]] = None, retries: int = 3) -> str:
        connection = Connection(rpc_endpoint)
        secret_key = base58.b58decode(private_key)
        keypair = Keypair.from_secret_key(secret_key)

        # Convert additional signers to Keypair objects
        signers: List[Keypair] = []
        if additional_signers is not None:
            signers = [Keypair.from_secret_key(base58.b58decode(signer_key)) for signer_key in additional_signers]

        for attempt in range(retries):
            try:
                # Fetch the latest blockhash and last valid block height
                latest_blockhash = await connection.get_latest_blockhash(Confirmed)
                blockhash = latest_blockhash['result']['value']['blockhash']
                last_valid_block_height = latest_blockhash['result']['value']['lastValidBlockHeight']

                # Update the transaction with the latest blockhash
                transaction.recent_blockhash = blockhash

                # Sign the transaction with the main keypair and additional signers
                transaction.sign(keypair, *signers)

                # Serialize the transaction
                serialized_transaction = transaction.serialize()

                # Send the transaction immediately after signing
                signature = await connection.send_raw_transaction(serialized_transaction, opts=TxOpts(skip_preflight=False, preflight_commitment='confirmed'))

                # Confirm the transaction using the new method
                confirmation = await connection.confirm_transaction(signature, commitment='confirmed')
                
                if confirmation['result']['value']['err']:
                    raise TransactionError(confirmation['result']['value']['err'])

                return signature
            except SendTransactionError as error:
                if 'TransactionExpiredBlockheightExceededError' in str(error) and attempt < retries - 1:
                    print(f'Transaction expired, retrying... Attempt: {attempt + 1}')
                    continue
                print("Error sending transaction:", error)
                print("Transaction logs:", error.logs if hasattr(error, 'logs') else "No logs available")
                raise
            except Exception as error:
                print("Error sending transaction:", error)
                raise

        raise Exception('Failed to send transaction after multiple attempts')
    
