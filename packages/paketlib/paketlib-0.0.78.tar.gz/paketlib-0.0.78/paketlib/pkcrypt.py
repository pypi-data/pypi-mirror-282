class pkDesC:
    def __init__(self, key: int):
        self.key = key & 0xFFFFFFFFFFFFFFFF
        self.rounds = 16

    def _feistel_round(self, block: int, subkey: int) -> int:
        left = (block >> 4) & 0xFFFFFFF
        right = block & 0xFFFFFFF

        for _ in range(self.rounds):
            left, right = right, left ^ (right & subkey)

        return (left << 28) | right

    def _generate_subkeys(self) -> list:
        subkeys = []
        for i in range(self.rounds):
            subkey = self.key ^ i
            subkeys.append(subkey)
        return subkeys

    def _encrypt_block(self, block: int) -> int:
        subkeys = self._generate_subkeys()
        encrypted_block = block
        for subkey in subkeys:
            encrypted_block = self._feistel_round(encrypted_block, subkey)
        return encrypted_block

    def encrypt(self, plaintext: str) -> int:
        block = int.from_bytes(plaintext.encode(), 'big')
        return self._encrypt_block(block)

    def decrypt(self, ciphertext: int) -> str:
        block = self._encrypt_block(ciphertext)
        return block.to_bytes((block.bit_length() + 7) // 8, 'big').decode()
    

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(
        d ^ key[i % len(key)]
        for i, d in enumerate(data)
    )