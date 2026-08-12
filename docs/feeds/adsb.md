# ADS-B (Aircraft)

The ADS-B feed brings live aircraft positions onto your TAK.NZ map, sourced from ADS-B (Automatic Dependent Surveillance–Broadcast) transponder data — the same technology used in modern air traffic tracking.

## What you'll see

Aircraft appear on the map as standard aviation icons, positioned and updated in real time as their transponders broadcast. Selecting an aircraft's icon shows available details in its Remarks field, such as altitude, heading, and identification where available.

## Firefighting aircraft detection

TAK.NZ's ADS-B feed automatically detects and classifies firefighting aircraft based on their transponder squawk code, using the code reserved for firefighting and reconnaissance duties under NZ Civil Aviation Rule Part 91.247 (squawk code `0111`).

Aircraft transmitting this code are automatically shown with a distinct icon:

- **Fixed-wing firefighting aircraft** — shown with a dedicated multi-use fire aircraft icon
- **Firefighting helicopters** — shown with a dedicated fire rotor icon

This override happens automatically — you don't need to do anything to see firefighting aircraft distinguished from general air traffic once the feed is enabled.

## Why this matters

During a wildfire or vegetation fire response, being able to see aircraft in the area — firefighting or otherwise — alongside ground crews on the same map removes the need for a separate air picture. Incident controllers and ground crews can see aerial assets without radio calls just to confirm "is there an aircraft overhead right now?"

## Enabling the feed

The ADS-B feed is enabled per-deployment by your TAK.NZ administrator, typically as its own channel or overlay layer. If you don't see aircraft on your map and expect to, check with your administrator that the feed is enabled for your channel access.

## Related

- [AIS (Vessels)](ais.md) — the equivalent feed for maritime traffic
- [Colour Coding](../reference/colour-coding.md) — how other map items are colour-coded by organisation
