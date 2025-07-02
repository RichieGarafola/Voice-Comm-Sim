# Provide hash creation and chunk validation
import hashlib



def hash_data(data):
    """
    Create a SHA-256 hash of the input data string.

    Args:
        data (str): The message or chunk data to hash.

    Returns:
        str: Hexadecimal representation of the hash.
    """
    return hashlib.sha256(data.encode()).hexdigest()



def create_chunk(index, data):
    """
    Create a secure message chunk containing the index, data, and its hash.

    Args:
        index (int): Sequence number of the chunk.
        data (str): The actual message data for this chunk.

    Returns:
        dict: A dictionary representing the chunk with index, data, and hash.
    """
    return {
        # Order identifier for reassembly
        "index": index,
        # The actual content of the message
        "data": data,
        # Secure hash for data integrity
        "hash": hash_data(data)
    }



def validate_chunk(chunk):
    """
    Validate a message chunk by comparing its stored hash to a recomputed one.

    Args:
        chunk (dict): A dictionary containing 'data' and its expected 'hash'.

    Returns:
        bool: True if the data is intact (hashes match), False otherwise.
    """
    return chunk["hash"] == hash_data(chunk["data"])

