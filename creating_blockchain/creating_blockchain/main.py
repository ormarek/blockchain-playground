import datetime, hashlib, json
from flask import Flask, jsonify

class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.create_block(proof = 1, prev_hash = None)

    def create_block(self, proof, prev_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'prev_hash': prev_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain(-1)
    
    def proof_of_work(self, prev_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_operation[:4] is '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
def main():
    print('Hello world!')

if __name__ == '__main__':
    main()
