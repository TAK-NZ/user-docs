# RELAY Assistant

**RELAY** (Rapid Emergency Liaison and Advisory for You) is TAK.NZ's built-in AI assistant. It's available directly in **GeoChat** on any client that supports it — ATAK, TAK Aware, WinTAK, or CloudTAK — so there's no separate app, no browser, and no new login. You just message it like any other contact.

## What RELAY can do

- Answer questions about New Zealand emergency doctrine, including CIMS (Coordinated Incident Management System), the FENZ Act, and the CDEM Act
- Provide live road closure data from NZTA Waka Kotahi
- Report current volcanic alert levels and recent earthquake data from GeoNet
- Place markers and overlays directly on your map based on your questions — RELAY is agentic, not just a chatbot, so it can act on the map rather than only answering in text
- Factor in your current location when answering, so responses are relevant to where you actually are

## Finding RELAY

RELAY is available in the **`Bots - All Users`** channel, accessible to every TAK.NZ user. Open GeoChat, select that channel, and start typing — or use voice-to-text if your device supports it, since RELAY is designed with hands-free field use in mind.

Example questions you might ask:

- "What are the current road closures near me?"
- "What's the current volcanic alert level for Ruapehu?"
- "What are the core principles of CIMS?"
- "Place a marker at the nearest fire station"
- "Where am I?"

!!! tip
    Be conversational — you don't need exact phrasing. Answers can take a few seconds, since RELAY queries its knowledge base and live data sources, and reasons about your location before responding. If a marker doesn't appear immediately, check whether it was placed just outside your current map view.

!!! note "Location privacy"
    RELAY uses your device's current position to answer location-aware questions. Your location is shared with RELAY to generate a response, but not with other users in the channel.

## SENTINEL — the NZDF equivalent

TAK.NZ also runs **SENTINEL**, a sibling bot focused on NZDF defence doctrine, joint operations, and CoT type guidance rather than civilian emergency management. SENTINEL is available in the **`Bots - New Zealand Defence Force`** channel and is only accessible to NZDF users. If you're not NZDF, you won't see this channel — that's expected, and RELAY is the right bot for civilian public safety questions.

## What's behind RELAY

RELAY is powered by a retrieval-augmented generation (RAG) knowledge base built from New Zealand emergency management reference material, including:

- Standardised callsign, channel, and colour-coding schemas used on TAK.NZ (see [Callsigns](../concepts/callsigns.md), [Channel Structure](../concepts/channels.md), and [Colour Coding](../concepts/colour-coding.md))
- Maritime radio and distress procedures, and Maritime Operator Safety System (MOSS) requirements
- Fire service radio codes and NZ Police operational codes
- Coordinated Incident Management System (CIMS) doctrine and the National CDEM Plan
- Fire and Emergency New Zealand Act legislative framework
- Fire station locations and the NZ Gazetteer place name database
- TAK map marker iconsets for incidents, infrastructure, and hazards

RELAY draws on this material to give doctrine-accurate, NZ-specific answers rather than generic guidance, and can combine information across multiple documents — for example, answering a question about a marine search and rescue by pulling in relevant radio procedures, safety system requirements, and training obligations together.

RELAY is implemented as a TAK Server-side plugin backed by AWS Bedrock, using custom NZ first responder map icons for any markers it places, so its output looks native on your Common Operating Picture. The underlying AI model is swappable as better models become available, without requiring any changes on your client.

If a place isn't in RELAY's knowledge base, it will try to resolve it using ArcGIS geocoding instead — so it can generally still help with locations outside New Zealand.

## Getting help beyond RELAY

RELAY is useful for doctrine questions and quick platform guidance, but for account issues, missing channel access, or anything specific to your organisation's TAK.NZ setup, contact your agency's TAK.NZ administrator directly — see [Account Management](../getting-started/account-management.md).
