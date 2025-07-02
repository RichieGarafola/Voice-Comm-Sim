# Unit tests for hashing and chunk validation functions

from stream.integrity import create_chunk, validate_chunk


def test_valid_chunk():
    """
    Test that a properly created chunk passes validation.

    The hash should match the data, so validation should return True.
    """
    # Create chunk with index 0 and data "Hello"
    chunk = create_chunk(0, "Hello")
    # Should pass because data is unchanged
    assert validate_chunk(chunk)


def test_invalid_chunk():
    """
    Test that a tampered chunk fails validation.

    The data is modified after the hash was generated, so validation should fail.
    """
    # Create chunk with index 1 and data "World"
    chunk = create_chunk(1, "World")
    # Tamper with the chunk after creation
    chunk["data"] = "Tampered"
    # Should fail validation
    assert not validate_chunk(chunk)
