import os

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from bitcoin.utils.constants import default_host


class BitcoinRPC:
    rpc_user = os.environ.get("RPC_USER")
    rpc_password = os.environ.get("RPC_PASSWORD")
    rpc_host = os.environ.get("RPC_HOST", default_host)
    rpc_port = os.environ.get("RPC_PORT", 8332)

    def __init__(self):
        rpc_string = f"http://{self.rpc_user}:{self.rpc_password}@{self.rpc_host}:{self.rpc_port}"
        self.rpc_connection = AuthServiceProxy(rpc_string)

    def get_transaction(self, txid: str) -> dict:
        return self.rpc_connection.getrawtransaction(txid, True)


if __name__ == '__main__':
    rpc = BitcoinRPC()
    txid = '8dc035d6816cf61074d12148777b28d28aa2f76b0f45ceafd310a85b1518aab8'
    try:
        transaction = rpc.get_transaction(txid)
        print(transaction)
    except JSONRPCException as e:
        print(f"An error occurred: {e}")