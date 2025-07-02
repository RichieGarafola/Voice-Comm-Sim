# Unit test for reassembling secure message chunks

from stream.receiver import reassemble
from stream.integrity import create_chunk

def test_reassemble_valid():
    """
    Test that the reassemble function correctly rebuilds a message
    from multiple valid, indexed chunks.

    It ensures that:
    - Chunks are ordered by index
    - Each chunk passes validation
    - The final message is reassembled accurately
    """
    # Create two valid message chunks
    chunks = [create_chunk(0, "Hello "), create_chunk(1, "World")]

    # Pair each chunk with its index for reassembly
    indexed = [(chunk["index"], chunk) for chunk in chunks]

    # Reassemble the message and verify the result
    result = reassemble(indexed)
    assert result == "Hello World"
