# Reassemble chunks in order, validate each

from .integrity import validate_chunk

def reassemble(chunks):
    """
    Reassemble a complete message from a list of indexed chunks.

    Each chunk is a tuple: (index, chunk_dict)
    Chunks are sorted by their index, validated using SHA-256,
    and combined to reconstruct the original message.

    Args:
        chunks (list of tuples): List of (index, chunk) pairs.

    Returns:
        str: The fully reassembled message string.

    Raises:
        ValueError: If any chunk fails hash validation.
    """
    # Sort chunks based on their index to ensure proper message order
    sorted_chunks = sorted(chunks, key=lambda x: x[0])

    message = ""

    for idx, chunk in sorted_chunks:
        # Validate chunk using its hash
        if not validate_chunk(chunk):
            raise ValueError("Chunk failed validation")

        # Append validated data to the full message
        message += chunk["data"]

    return message