# Intelligent DJ Selection Prototype

An experimental Python project exploring context-aware music selection for DJ sessions.

## Current capabilities

- Selects a small predefined playlist from a session mood or atmosphere.
- Defines a Spotify connector that searches for a track and retrieves available audio features such as tempo, energy, valence, and danceability.

## Project status

This repository is a prototype, not a production-ready autonomous DJ system.

The current selector uses predefined example tracks. The streaming and feedback modules are placeholders, and the Spotify connector requires valid API credentials supplied by the developer.

## Project files

| File | Purpose |
| --- | --- |
| `selector.py` | Scenario-based playlist selection prototype |
| `api_connector.py` | Spotify search and audio-feature connector |
| `callback.html` | OAuth callback page |
| `streamer.py` | Placeholder for future playback/streaming work |
| `feedback.py` | Placeholder for future feedback logic |

## Setup

Use Python 3. Install the Spotify client library:

```bash
pip install spotipy
```

Spotify API credentials should be provided through a secure local configuration or environment variables. Do not commit secrets.

## Roadmap

- Replace hard-coded playlists with a configurable selection strategy.
- Add robust handling for missing Spotify audio features and API errors.
- Implement playback/streaming and feedback modules.
- Add tests and configuration documentation.

## Related work

This repository remains independent from the separate multi-agent DJ interface prototype.
