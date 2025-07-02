# Split message into chunks

def chunk_message(message, chunk_size=5):
    """
    Splits a message into fixed-size chunks with corresponding start indices.

    Args:
        message (str): The full message string to be chunked.
        chunk_size (int): The size of each chunk (default is 5 characters).

    Returns:
        list of tuples: Each tuple contains (index, chunk_string), where:
            - index (int): Starting character index of the chunk
            - chunk_string (str): Substring of the original message
    """
    return [(i, message[i:i+chunk_size]) 
            for i in range(0, len(message), chunk_size)]

