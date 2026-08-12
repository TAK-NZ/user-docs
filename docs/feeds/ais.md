# AIS (Vessels)

The AIS feed brings live vessel positions onto your TAK.NZ map, sourced from the Automatic Identification System (AIS) — the maritime equivalent of ADS-B, used internationally for vessel tracking and collision avoidance.

## What you'll see

Vessels appear on the map as maritime icons, positioned and updated as their AIS transponders broadcast. The feed is scoped to New Zealand waters by default, and vessel details — including type classification — are shown in the Remarks field when you select a vessel's icon.

## How vessels are classified

The AIS feed maps each vessel's reported AIS ship type to an appropriate icon and classification, and determines affiliation (domestic versus foreign) based on the vessel's flag. This means, for example, a New Zealand-flagged vessel and a foreign-flagged vessel of the same type will appear with the same base icon but different affiliation styling, consistent with how [Colour Coding](../reference/colour-coding.md) works elsewhere in TAK.NZ.

Where a specific vessel needs a manual override — for example, a known vessel that should always appear with a particular icon regardless of its reported AIS type — this can be configured by MMSI (Maritime Mobile Service Identity) at the administrator level.

## Why this matters

For maritime search and rescue, Coastguard operations, or general maritime domain awareness, having live vessel positions on the same Common Operating Picture as your team's own tracked assets means responders don't need a separate maritime tracking tool alongside TAK.NZ. This is particularly useful for coordinating a marine search, monitoring vessel traffic near an incident, or maintaining general situational awareness of activity in NZ waters.

## Enabling the feed

The AIS feed is enabled per-deployment by your TAK.NZ administrator, typically as its own channel or overlay layer. If you don't see vessels on your map and expect to, check with your administrator that the feed is enabled for your channel access.

## Related

- [ADS-B (Aircraft)](adsb.md) — the equivalent feed for air traffic
- [Colour Coding](../reference/colour-coding.md) — how map items are colour-coded by organisation and affiliation
