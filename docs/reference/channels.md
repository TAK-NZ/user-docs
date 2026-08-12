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

Foreign partner personnel (for example, Australian fire crews supporting FENZ during a wildfire) don't get dedicated country or organisation channels. They join the relevant **regional** channel for the incident they're supporting (e.g. `Regions - Southland`). Their [callsign](callsigns.md) prefix (e.g. `AUS-FIRE-NSWRFS-Unit1`) provides nationality and functional identification on the map — no separate channel is needed.

For large or sustained foreign deployments requiring internal coordination, a temporary mission-scoped channel may be created on demand (e.g. `AUS-FIRE-STL-2026`) and deactivated once the deployment ends.

## Vendor channels

Vendors and technical support personnel are assigned to the `VND` channel only, without default access to regional or organisation channels. Temporary access to a specific channel for testing or verification is granted by a TAK Team Manager administrator and revoked once complete.

## Overseas and international deployment channels

When NZ personnel are deployed overseas — primarily in the South Pacific, but potentially anywhere internationally — TAK.NZ serves as the operational Common Operating Picture where no local TAK instance exists.

Overseas channels use the `Overseas -` prefix to clearly distinguish them from NZ domestic regional channels (`Regions -`) in the channel list.

**Format:** `Overseas - [Country Name]` (e.g. `Overseas - Tonga`). One channel per country — sub-national granularity isn't used, since Pacific Island nations are small enough that a single country channel covers the entire operational area.

### Standing Pacific channels

These reflect New Zealand's ongoing regional leadership role in the South Pacific and are maintained permanently, allowing Pacific partner agencies to keep access and familiarity with TAK.NZ between deployments:

`Overseas - Cook Islands` · `Overseas - Fiji` · `Overseas - Kiribati` · `Overseas - Niue` · `Overseas - Papua New Guinea` · `Overseas - Samoa` · `Overseas - Solomon Islands` · `Overseas - Tokelau` · `Overseas - Tonga` · `Overseas - Tuvalu` · `Overseas - Vanuatu`

### Temporary deployment channels

For deployments outside the standing Pacific list (for example, a NZ USAR team deploying following an earthquake elsewhere in the world), a temporary channel is created on demand:

1. **Request** — a deployment coordinator (typically NEMA or NZDF logistics) requests the channel via TAK Team Manager, specifying the country and expected duration.
2. **Creation** — the channel is created and activated for the deploying organisation's personnel.
3. **Self-subscription** — individual personnel can subscribe via the account portal if not automatically enrolled.
4. **Expiry** — the channel is deactivated and removed after the deployment ends, or after a period of inactivity.

### Pacific partner agency access

Pacific Island nation emergency management agencies that participate in a NZ-led response may retain access to their country's standing channel beyond the deployment itself, supporting ongoing familiarity, joint preparedness exercises, and faster readiness for future responses. They're treated as foreign partners: using the `[COUNTRY]-[FUNCTION]-[SUFFIX]` callsign schema (e.g. `TON-CDEM-Smith`), with access managed through TAK Team Manager and limited to their own `Overseas -` channel by default.

### Callsign convention for overseas deployments

NZ personnel on overseas deployment use their standard domestic callsign prefix (e.g. `NZDF-`, `NZRC-`, `NEMA-`) — no schema change is required. Foreign partners operating alongside NZ personnel use the standard foreign partner schema (`[COUNTRY]-[FUNCTION]-[SUFFIX]`), joining the same `Overseas -` channel for the deployment.

## Why this structure

**Regional channels as the coordination layer.** In an emergency, the geographic boundary is the natural unit of coordination — a Southland flood involves FENZ-STL, NZP-STL, LSAR-STL, and DOC-STL, not their national counterparts. The regional channel brings all of these together automatically.

**Organisation channels for internal coordination.** Agencies need space to coordinate internally without broadcasting to every other responder — for example, a FENZ incident controller issuing internal tasking shouldn't need to appear on the regional Common Operating Picture.

**Hierarchy depth is intentionally limited.** The structure caps out at three levels: national → regional → org/sub-team. A fourth level (e.g. `FENZ-STL-Station12`) would push operators into silos and undermine the shared awareness TAK.NZ is designed to provide.

**Foreign partners join regional channels, not country channels.** A country-specific channel would silo foreign partners away from the NZ responders they're working alongside. The regional channel is the right coordination layer regardless of national origin — the callsign prefix already handles identity.

## Known limitation

TAK.NZ currently activates all channels by default for new users, since the platform doesn't yet enforce per-operator channel activation profiles at enrolment. This means a FENZ operator in Te Anau will initially see all 16 regional channels, their national org channel, and any sub-team channels — potentially 18 or more active channels at once. Manually deactivating irrelevant channels is currently an operator responsibility.

A future TAK Team Manager enhancement will use the TAK Server's group activation API to automatically configure each operator's active channels based on their home region and organisation at enrolment, reducing this manual step. Until then, channel hygiene should be covered as part of operator onboarding.

## Related

- [Callsigns](callsigns.md) — how individual tracks are named within these channels
- [Colour Coding](colour-coding.md) — how organisations appear visually on the map
