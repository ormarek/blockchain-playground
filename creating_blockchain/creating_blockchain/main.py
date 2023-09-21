import datetime, hashlib, json
from flask import Flask, jsonify

import datetime
import hashlib
import json
from typing import List, Dict, Union

class Blockchain:
    def __init__(self) -> None:
        self.chain: List[Dict[str, Union[int, str]]] = []
        self.create_block(proof=1, previous_hash=None)

    def create_block(self, proof: int, previous_hash: str) -> Dict[str, Union[int, str]]:
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block
    
    def get_first_block(self) -> Dict[str, Union[int, str]]:
        return self.chain[0]
    
    def get_last_block(self) -> Dict[str, Union[int, str]]:
        return self.chain[-1]
    
    def _is_proof_valid(self, new_proof: int, previous_proof: int) -> bool:
        hash_operation = hashlib.sha256(f"{new_proof**2 - previous_proof**2}".encode()).hexdigest()
        return hash_operation[:4] == '0000'
    
    def proof_of_work(self, previous_proof: int) -> int:
        new_proof = 1
        while not self._is_proof_valid(new_proof, previous_proof):
            new_proof += 1
        return new_proof
    
    def hash(self, block: Dict[str, Union[int, str]]) -> str:
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain: List[Dict[str, Union[int, str]]]) -> bool:
        previous_block = self.get_first_block()

        for current_block in chain[1:]:
            if current_block['previous_hash'] != self.hash(previous_block):
                return False
            
            if not self._is_proof_valid(current_block['proof'], previous_block['proof']):
                return False

            previous_block = current_block

        return True

def main():
    print('Hello world!')

if __name__ == '__main__':
    main()
