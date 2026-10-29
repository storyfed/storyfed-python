# Storyfed Python SDK

The official Python wrapper for the Storyfed AI Video Generation API.

## Installation
```bash
pip install storyfed
```

## Quick Start

```bash
from storyfed import Storyfed

client = Storyfed(api_key="YOUR_API_KEY")

video = client.generate_video(
    prompt="[Scene 1]\nA cinematic shot of space.",
    quality_tier="Budget",
    ratio="16:9"
)

print(f"Success! Watch here: {video['url']}")
```
