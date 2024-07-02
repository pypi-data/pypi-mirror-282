# Mem0: Long-Term Memory for LLMs

Mem0 provides a smart, self-improving memory layer for Large Language Models, enabling personalized AI experiences across applications.

## Features

- Persistent memory for users, sessions, and agents
- Self-improving personalization
- Simple API for easy integration
- Cross-platform consistency

## Quick Start

### Installation

```bash
pip install mem0
```

## Usage

```python
from mem0 import Mem0

# Initialize client
client = Mem0(api_key="your-api-key")

# Add memory
client.add("User preference: dark mode", user_id="user123")

# Retrieve memories
memories = client.get_all(user_id="user123")

# Update memory
client.update(memory_id, data="Updated information")

# Delete memory
client.delete(memory_id)
```

## Documentation

For detailed usage and API reference, visit our [documentation](https://docs.mem0.ai).

## Getting Started

1. Sign up at Mem0 Platform
2. Get your API key from the dashboard
3. Install the SDK and start integrating

## Support

Join our [slack](https://mem0.ai/slack) or [discord](https://mem0.ai/discord) community for support and discussions.

## License

[Apache 2.0](https://github.com/apache/.github/blob/main/LICENSE)
