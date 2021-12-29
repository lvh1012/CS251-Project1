from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret('cQepZdCep3bg8G5epLdwiWCyviDzx5rGsStMT6uiVvxWjNqfVjyu')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret('cSjQKmkHtFwzBS9yYptTjFtFjch1nMfFQrwrz1FCCB2TB1x5CFvu')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret('cR5Hctq9oxzYoCjwWCqa1tqopbpua43ZCev72JwzTEFxZsUN817s')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3
# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.
Q3a_txout_scriptPubKey = [
        OP_2,
        my_public_key,
        cust1_public_key,
        cust2_public_key,
        cust3_public_key,
        OP_4,
        OP_CHECKMULTISIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00002 # amount of BTC in the output you're sending minus fee
    txid_to_spend = ('ec80d770cc0ca7837fabf5a4172e56d8a6a22f4895ab79de752641cbb60441d7')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
