# Channel Structure

TAK.NZ uses a structured channel hierarchy to balance shared situational awareness across agencies with the operational privacy each organisation needs for internal coordination.

!!! note "All channels are active by default"
    New users start with every channel active. You're expected to deactivate channels that aren't relevant to your current operational context, to keep your map focused. See [Known limitation](#known-limitation) below for why this is currently manual.

The structure has two layers:

1. **Response and Support channels** — the primary coordination layer for emergency events within a geographic area, split by who needs access (see below)
2. **Organisation and sub-team channels** — for internal coordination within a single agency

## Response and Support channels

Regional coordination is split into two parallel channel families, one channel per NZ region plus Chatham Islands, so that day-to-day multi-agency response and wider disaster coordination each get the right audience:

- **Response channels** (`Response - [Region]`) — restricted to **Emergency Services** agencies. This is where typical multi-agency incident response is coordinated, keeping traffic on a need-to-know basis and respecting each agency's operational privacy. There is no nationwide `Response` channel — Response coordination is always regional.
- **Support channels** (`Support - [Region]`, plus `Support - All of New Zealand`) — open to **all agencies**, including lifeline utilities and welfare organisations that aren't Emergency Services. When an incident escalates into a declared disaster and needs broader participation beyond Emergency Services, coordination moves from the relevant Response channel(s) to the matching Support channel(s).

| Channel family | Access | Nationwide channel? |
|---|---|---|
| `Response - [Region]` | Emergency Services only | No — regional only |
| `Support - [Region]` | All agencies | Yes — `Support - All of New Zealand` |

One pair of Response/Support channels exists per NZ region, aligned to ISO 3166-2:NZ subdivision boundaries, plus Chatham Islands:

`Northland` · `Auckland` · `Waikato` · `Bay of Plenty` · `Gisborne` · `Hawkes Bay` · `Taranaki` · `Manawatu-Whanganui` · `Wellington` · `Tasman` · `Nelson` · `Marlborough` · `West Coast` · `Canterbury` · `Otago` · `Southland` · `Chatham Islands`

For example, Canterbury has both `Response - Canterbury` and `Support - Canterbury`.

### Who counts as Emergency Services

| Emergency Services (Response + Support) | Support only |
|---|---|
| Fire and Emergency New Zealand (FENZ) | National Emergency Management Agency (NEMA) |
| New Zealand Police (NZP) | CDEM Groups |
| Ambulance (St John / Wellington Free Ambulance) | New Zealand Red Cross |
| Air Ambulance & Rescue Helicopter | New Zealand Defence Force (NZDF) |
| Land Search and Rescue (LandSAR) | Department of Conservation (DOC) |
| Coastguard New Zealand | New Zealand Customs Service |
| Surf Life Saving New Zealand | Road network operators (NZTA and partners) |
| Health New Zealand (Te Whatu Ora) | Vendor / technical support |

NEMA and CDEM Groups coordinate *declared* emergencies and wider disaster response rather than routine incidents, so they sit in Support alongside lifeline utilities and welfare organisations — this is the clearest example of the Response-to-Support escalation described above. See [Callsigns](callsigns.md) for the full organisation prefix list.

Regional Response and Support channels are the **primary coordination layer** for any incident. Within their tier, all responding agencies can see each other's tracks and share situational awareness on the relevant regional channel(s) without any additional configuration.

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

Foreign partner personnel (e.g. Australian fire crews supporting FENZ during a wildfire) join the relevant **Response** or **Support** channel for the incident, rather than getting a dedicated country or organisation channel. Which tier depends on their [function code](callsigns.md): Emergency Services functions (`FIRE`, `POL`, `MED`, `LSAR`, `MSAR`) get both Response and Support access, the same as their domestic counterparts; non-Emergency-Services functions (`MIL`, `MAR`, `CDEM`, `UTIL`, `LOG`) get Support access only. Their [callsign](callsigns.md) prefix (e.g. `AUS-FIRE-NSWRFS-Unit1`) already provides nationality and functional identification on the map. For large or sustained deployments, a temporary mission-scoped channel may be created on demand (e.g. `AUS-FIRE-STL-2026`) and deactivated once the deployment ends.

## Vendor channels

Vendors and technical support personnel are assigned to the `VND` channel only, without default access to Response, Support, or organisation channels. Temporary access to a specific channel is granted by a TAK Team Manager administrator and revoked once complete.

## Overseas deployment channels

When NZ personnel deploy overseas — primarily in the South Pacific — TAK.NZ serves as the operational Common Operating Picture where no local TAK instance exists. These channels use an `Overseas -` prefix (e.g. `Overseas - Tonga`) to distinguish them from domestic `Response -`/`Support -` channels, with one channel per country.

**Standing Pacific channels** are maintained permanently, reflecting NZ's ongoing regional leadership role: `Overseas - Cook Islands` · `Overseas - Fiji` · `Overseas - Kiribati` · `Overseas - Niue` · `Overseas - Papua New Guinea` · `Overseas - Samoa` · `Overseas - Solomon Islands` · `Overseas - Tokelau` · `Overseas - Tonga` · `Overseas - Tuvalu` · `Overseas - Vanuatu`.

**Temporary channels** are created on demand for other deployments (e.g. a NZ USAR team responding to an earthquake elsewhere): a deployment coordinator requests the channel via TAK Team Manager, personnel subscribe (automatically or self-service), and the channel is deactivated after the deployment ends.

NZ personnel use their standard domestic callsign prefix while deployed (no schema change needed). Foreign partners use the standard `[COUNTRY]-[FUNCTION]-[SUFFIX]` schema and join the same `Overseas -` channel. Pacific partner agencies may retain access to their country's standing channel beyond a deployment, to support ongoing familiarity and joint preparedness.

## Why this structure

The hierarchy is intentionally limited in depth: **regional Response/Support channels** are the natural coordination unit during an emergency (a Southland flood involves every agency's Southland team, not their national HQs), **organisation** channels let agencies coordinate internally without broadcasting to every other responder, and a further level (e.g. `FENZ-STL-Station12`) would fragment awareness rather than support it. Splitting regional coordination into Response and Support tiers lets Emergency Services coordinate on a need-to-know basis for routine incidents, while still giving a clear escalation path to bring in lifeline utilities, welfare organisations, and other non-Emergency-Services agencies once an incident becomes a declared disaster. Foreign partners join the regional channel(s) matching their function rather than a country-specific one, since geography — not nationality — is the right coordination boundary; their callsign prefix already handles identity.

## Known limitation

All channels are currently activated by default for new users, since TAK.NZ doesn't yet enforce per-operator channel profiles at enrolment. With the Response/Support split, an Emergency Services operator may see 35+ active regional channels initially (17 Response + 18 Support) and needs to manually deactivate irrelevant ones; non-Emergency-Services operators see the 18 Support channels only. A planned TAK Team Manager enhancement will auto-configure each operator's active channels based on home region and organisation at enrolment.

## Related

- [Callsigns](callsigns.md) — how individual tracks are named within these channels
- [Colour Coding](colour-coding.md) — how organisations appear visually on the map
