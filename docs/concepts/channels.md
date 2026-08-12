# Channel Structure

TAK.NZ uses a structured channel hierarchy to balance shared situational awareness across agencies with the operational privacy each organisation needs for internal coordination.

!!! note "All channels are active by default"
    New users start with every channel active. You're expected to deactivate channels that aren't relevant to your current operational context, to keep your map focused. See [Known limitation](#known-limitation) below for why this is currently manual.

The structure has three layers:

1. **National channel** — for events affecting the entire country
2. **Regional channels** — the primary coordination layer for emergency events within a geographic area
3. **Organisation and sub-team channels** — for internal coordination within a single agency

## National channels

| Channel | Purpose |
|---|---|
| `Regions - All of New Zealand` | Nationwide coordination. Used for major events affecting multiple regions simultaneously (e.g. national-scale earthquakes, pandemic response, multi-region storms). |
| `Regions - Chatham Islands` | Geographically isolated from the mainland, with its own response challenges — kept separate to avoid irrelevant traffic on mainland regional channels. |

## Regional channels

One channel per NZ region, aligned to ISO 3166-2:NZ subdivision boundaries:

`Regions - Northland` · `Regions - Auckland` · `Regions - Waikato` · `Regions - Bay of Plenty` · `Regions - Gisborne` · `Regions - Hawkes Bay` · `Regions - Taranaki` · `Regions - Manawatu-Whanganui` · `Regions - Wellington` · `Regions - Tasman` · `Regions - Nelson` · `Regions - Marlborough` · `Regions - West Coast` · `Regions - Canterbury` · `Regions - Otago` · `Regions - Southland`

Regional channels are the **primary coordination layer**. When an emergency happens in a region, all responding agencies activate that region's channel. This means FENZ, Police, LandSAR, Health NZ, and any other responders can see each other's tracks and share situational awareness without any additional configuration.

## Organisation channels

Each organisation has one or more dedicated channels for internal coordination — not intended for cross-agency situational awareness, but to let teams coordinate internally without broadcasting to every other agency on the regional channel.

**Format:** `[ORG]` for the national org channel, `[ORG]-[REGION]` for regional sub-teams.

| Channel | Organisation |
|---|---|
| `FENZ` | Fire and Emergency New Zealand — national |
| `FENZ-STL` | FENZ — Southland sub-team |
| `FENZ-AKL` | FENZ — Auckland sub-team |
| `NZP` | New Zealand Police — national |
| `NZP-WGN` | NZ Police — Wellington sub-team |
| `NZDF` | New Zealand Defence Force — national |
| `NZDF-STL` | NZDF — Southland sub-team |
| `AMB` | Hato Hone St John / Wellington Free Ambulance / Air Ambulance & Rescue Helicopter — national |
| `AMB-CAN` | Ambulance / Air Ambulance — Canterbury sub-team |
| `NEMA` | National Emergency Management Agency |

Not every organisation needs regional sub-team channels — these are only created where there's a genuine operational need (e.g. FENZ, NZ Police, NZDF, LandSAR). Organisations with a smaller field footprint (e.g. Maritime NZ, NZ Red Cross) typically operate on their national channel only.

## Foreign partner channels

Foreign partner personnel (e.g. Australian fire crews supporting FENZ during a wildfire) join the relevant **regional** channel for the incident, rather than getting a dedicated country or organisation channel. Their [callsign](callsigns.md) prefix (e.g. `AUS-FIRE-NSWRFS-Unit1`) already provides nationality and functional identification on the map. For large or sustained deployments, a temporary mission-scoped channel may be created on demand (e.g. `AUS-FIRE-STL-2026`) and deactivated once the deployment ends.

## Vendor channels

Vendors and technical support personnel are assigned to the `VND` channel only, without default access to regional or organisation channels. Temporary access to a specific channel is granted by a TAK Team Manager administrator and revoked once complete.

## Overseas deployment channels

When NZ personnel deploy overseas — primarily in the South Pacific — TAK.NZ serves as the operational Common Operating Picture where no local TAK instance exists. These channels use an `Overseas -` prefix (e.g. `Overseas - Tonga`) to distinguish them from domestic `Regions -` channels, with one channel per country.

**Standing Pacific channels** are maintained permanently, reflecting NZ's ongoing regional leadership role: `Overseas - Cook Islands` · `Overseas - Fiji` · `Overseas - Kiribati` · `Overseas - Niue` · `Overseas - Papua New Guinea` · `Overseas - Samoa` · `Overseas - Solomon Islands` · `Overseas - Tokelau` · `Overseas - Tonga` · `Overseas - Tuvalu` · `Overseas - Vanuatu`.

**Temporary channels** are created on demand for other deployments (e.g. a NZ USAR team responding to an earthquake elsewhere): a deployment coordinator requests the channel via TAK Team Manager, personnel subscribe (automatically or self-service), and the channel is deactivated after the deployment ends.

NZ personnel use their standard domestic callsign prefix while deployed (no schema change needed). Foreign partners use the standard `[COUNTRY]-[FUNCTION]-[SUFFIX]` schema and join the same `Overseas -` channel. Pacific partner agencies may retain access to their country's standing channel beyond a deployment, to support ongoing familiarity and joint preparedness.

## Why this structure

The three-layer hierarchy is intentionally limited in depth: **regional** channels are the natural coordination unit during an emergency (a Southland flood involves every agency's Southland team, not their national HQs), **organisation** channels let agencies coordinate internally without broadcasting to every other responder, and a fourth level (e.g. `FENZ-STL-Station12`) would fragment awareness rather than support it. Foreign partners join the regional channel rather than a country-specific one, since geography — not nationality — is the right coordination boundary; their callsign prefix already handles identity.

## Known limitation

All channels are currently activated by default for new users, since TAK.NZ doesn't yet enforce per-operator channel profiles at enrolment — an operator may see 18+ active channels initially and needs to manually deactivate irrelevant ones. A planned TAK Team Manager enhancement will auto-configure each operator's active channels based on home region and organisation at enrolment.

## Related

- [Callsigns](callsigns.md) — how individual tracks are named within these channels
- [Colour Coding](colour-coding.md) — how organisations appear visually on the map
