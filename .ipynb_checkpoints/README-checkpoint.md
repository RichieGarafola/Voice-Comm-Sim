# Voice Communication Simulator

![CI](https://github.com/RichieGarafola/Voice-Comm-Sim/actions/workflows/ci.yml/badge.svg)

This project simulates how a voice or message communication system might securely transmit and reassemble data in a controlled, verifiable way. The goal is to model how real-time data (like audio or text) is broken into smaller pieces, verified for integrity, and put back together in the correct order.

It also includes a full suite of automated tests and a continuous integration (CI) pipeline using GitHub Actions, showing how software quality and reliability are ensured through modern DevOps practices.

---

## Why This Matters

In secure communications (such as military, government, or enterprise systems), it's critical to:
- Break large messages into smaller, manageable parts (or "packets")
- Ensure no part has been tampered with
- Reassemble the full message accurately, even in the presence of network disruptions

This project simulates those core ideas in a simplified, easy-to-understand Python environment.

---

## What the Project Does

### Message Chunking
The system splits a message (like `"Hello World"`) into smaller pieces, e.g. `"Hello"` and `"World"`. Each piece has:
- An index (its position in the message)
- The actual text
- A **SHA-256 hash** to ensure it hasn't been altered

### Integrity Validation
Each chunk has a hash that’s used to verify the data hasn't been changed. If even one character in the chunk is altered, the hash won’t match and the system will detect it.

### Reassembly
Once all chunks are received:
- They are sorted by their index
- Each is validated for integrity
- Then they are reassembled into the original full message

---

## Automated Testing

All core functionality is tested using `pytest`:
- Valid chunk creation and validation
- Detection of tampered chunks
- Correct message reassembly from multiple parts

These tests are run automatically on every code change using **GitHub Actions**, ensuring that the code stays correct and reliable over time.

---

## Project Structure

```
voice_comm_sim/
│
├── stream/
│   ├── sender.py         # Splits messages into chunks
│   ├── receiver.py       # Reassembles and validates message
│   └── integrity.py      # Hashing and validation logic
│
├── tests/
│   ├── test_integrity.py # Tests for chunk integrity validation
│   └── test_reassembly.py # Tests full message reassembly
│
├── .github/workflows/
│   └── ci.yml            # GitHub Actions CI pipeline
│
├── requirements.txt      # Project dependencies
└── README.md             # This file
```

---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/RichieGarafola/voice_comm_sim.git
cd voice_comm_sim
```

### 2. Install Dependencies
Make sure Python is installed, then:
```bash
pip install -r requirements.txt
```

### 3. Run the Tests
```bash
pytest
```

If everything is working correctly, you'll see all tests pass.

---

## Continuous Integration (CI)

A GitHub Actions workflow (`.github/workflows/ci.yml`) is included to:
- Run tests automatically on every push
- Ensure code remains bug-free and maintainable

---

## Key Concepts Demonstrated

| Concept | What It Shows |
|--------|----------------|
| **Chunking** | Simulates packet-based communication |
| **Hashing** | Ensures data integrity |
| **Validation** | Detects tampering or corruption |
| **Automated Testing** | Promotes robust, bug-free development |
| **CI/CD** | Emulates real-world DevOps practices |

---

## Future Enhancements

If you'd like to expand the project further:
- Add message encryption (e.g., RSA)
- Simulate packet loss or out-of-order delivery
- Build a CLI or web interface using Streamlit or Typer
- Log each transmission and reassembly event

---

## Author

**Richie Garafola**  
[GitHub](https://github.com/RichieGarafola) • [LinkedIn](https://linkedin.com/in/RichieGarafola)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
