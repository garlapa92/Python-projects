from hashlib import sha256
import time

MAX_NONCE = 10000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number)+ transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! successfully mined bitcoins with nonce value:{nonce}")
            return new_hash
    raise BaseException(f"couldn't find correct has after trying {MAX_NONCE} times")

if __name__ == "__main__":
    transactions = """
    players1->players->2-> 200, 
    player3->player4-> 450
    """
    difficulty = 6 

    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,"000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7",difficulty,)

    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)                  
