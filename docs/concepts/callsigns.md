# Callsigns

TAK.NZ uses a standardised callsign prefix schema so every track on the Common Operating Picture is immediately identifiable by organisation, and optionally by region or sub-unit.

The callsign and the [colour](colour-coding.md) carry different information, and the split is deliberate: **the callsign identifies who you are, the colour identifies what you do.** The callsign gives an organisation, nationality and region; the colour gives an operational function. Read together they tell you that an Australian fire crew (`AUS-FIRE-`) is doing the same job as the FENZ crew beside it, and that both appear Red.

## Schema

**Domestic NZ organisations:**

```
[ORG]-[REGION]-[SUFFIX]
```

**Foreign partner organisations:**

```
[COUNTRY]-[FUNCTION]-[SUFFIX]
```

| Component | Required | Description |
|---|---|---|
| `ORG` | Mandatory | Organisation prefix (see table below). All domestic callsigns must begin with this prefix. |
| `REGION` | Optional | Regional identifier derived from ISO 3166-2:NZ (country prefix omitted). |
| `SUFFIX` | Mandatory | Individual or unit identifier. Format is determined by each organisation (full name, initials, radio ID, badge number, etc.). |
| `COUNTRY` (foreign) | Mandatory | ISO 3166-1 alpha-3 country code for foreign partners (e.g. `AUS`, `USA`). |
| `FUNCTION` (foreign) | Mandatory | Standardised function abbreviation (see table below). |

The hyphen (`-`) is the only permitted separator between all components — no underscores or spaces.

## Organisation prefixes (domestic)

| Organisation | Prefix |
|---|---|
| Fire and Emergency New Zealand (FENZ) | `FENZ` |
| New Zealand Police | `NZP` |
| Hato Hone St John / Wellington Free Ambulance | `AMBU` |
| Air Ambulance & Rescue Helicopter | `RHT` |
| National Emergency Management Agency (NEMA) | `NEMA` |
| CDEM Groups (regional Civil Defence Emergency Management) | `CDEM` |
| Land Search and Rescue NZ (LandSAR) | `LSAR` |
| Health New Zealand (Te Whatu Ora) | `HNZ` |
| New Zealand Red Cross | `NZRC` |
| Coastguard New Zealand | `CGRD` |
| Surf Life Saving New Zealand | `SLS` |
| New Zealand Customs Service | `CUST` |
| New Zealand Defence Force (NZDF) | `NZDF` |
| Department of Conservation (DOC) | `DOC` |
| Road network operators (NZTA and partners) | `NZTA` |
| Vendor / technical support | `VND` |

Organisations not yet listed — including Maritime New Zealand, lifeline utility operators and welfare providers other than Red Cross — are assigned a prefix when they are onboarded.

## Function codes (foreign partners)

| Function | Code | Covers |
|---|---|---|
| Fire | `FIRE` | Fire brigades, wildfire crews |
| Police / Law Enforcement | `POL` | Police, border force, federal agents |
| Military | `MIL` | Army, Navy, Air Force, National Guard |
| Medical / Ambulance | `MED` | Paramedics, field hospitals, medical teams |
| Land Search and Rescue | `LSAR` | Land, alpine and cave search and rescue teams |
| Marine Search and Rescue | `MSAR` | Coastguard, lifeguard and marine rescue crews |
| Maritime / Aviation Authority | `MAR` | Maritime safety authorities, rescue coordination centres, harbour and airport authorities |
| Civil Defence / Emergency Management | `CDEM` | FEMA equivalents, state emergency services, EOC staff |
| Lifeline Utilities | `UTIL` | Electricity, water, gas, fuel, telecommunications crews |
| Logistics / Support | `LOG` | Supply, transport, engineering support |

Each code maps to exactly one [colour](colour-coding.md), so a foreign track is coloured by the same rule as a domestic one.

!!! note "Two codes have changed"
    Land SAR is now `LSAR`, not `SAR`, so it pairs symmetrically with `MSAR` for marine SAR — a bare `SAR` read as
    "all search and rescue" when it only ever meant the land category. And `MAR` has been split: marine *rescue* is
    `MSAR` (Teal) while maritime *authority* remains `MAR` (Magenta), because a rescue asset and the centre
    coordinating it shouldn't look identical on the map. Foreign partners tagged with the older `SAR` or single
    `MAR` code should be re-tagged.

    `LSAR` deliberately means land search and rescue in **both** namespaces — it is the domestic prefix for LandSAR
    and the foreign function code. Position tells them apart: `LSAR-CAN-TeamA` is the New Zealand organisation,
    `AUS-LSAR-Team1` is an Australian land SAR team.

## Regional identifiers (optional, domestic)

Regions use the official ISO 3166-2:NZ subdivision codes, with the `NZ-` country prefix omitted since it's redundant in a NZ-only context. A few examples: `AUK` (Auckland), `WGN` (Wellington), `CAN` (Canterbury), `STL` (Southland). Regional identifiers are optional and at each organisation's discretion — not every organisation uses them.

## Examples

| Callsign | Interpretation |
|---|---|
| `FENZ-STL-JSmith` | FENZ, Southland, individual J. Smith |
| `FENZ-AUK-01` | FENZ, Auckland, unit 01 |
| `NZP-WGN-Badge4521` | NZ Police, Wellington, badge number 4521 |
| `LSAR-CAN-TeamA` | LandSAR, Canterbury, Team A |
| `VND-AcmeCorp-Tech1` | Vendor, Acme Corp, technician 1 |
| `AUS-FIRE-NSWRFS-Unit1` | Australian, fire function, NSW Rural Fire Service, Unit 1 |
| `AUS-MIL-Jones` | Australian military, Jones |
| `GBR-MED-Medic1` | British medical personnel, Medic 1 |
| `SLS-BOP-Tower3` | Surf Life Saving, Bay of Plenty, Tower 3 |
| `AUS-MSAR-Vessel2` | Australian marine search and rescue, Vessel 2 |

## Rules and guidance

- **Mandatory prefix, hyphen-separated.** Every callsign must start with the organisation prefix (domestic) or country code (foreign), using `-` as the only separator. Tracks without a recognised prefix should be flagged as misconfigured.
- **Suffix format is organisation-specific** — a surname (`JSmith`), initials (`JS`), a radio/badge ID (`Badge4521`), or a unit number (`01`, `Alpha1`).
- **Keep it short.** TAK truncates long callsigns on smaller screens — aim for 20 characters or fewer.
- **Special cases use a sub-identifier after the primary prefix** — for example, personnel embedded with or operating under another organisation's command (`NZDF-INT-[suffix]`), or a vendor supporting a specific agency (`VND-FENZ-[suffix]`). Personnel holding roles in more than one organisation use the prefix for whichever role they're performing during the current incident.
- **Some prefixes cover a whole sector, not one employer.** `NZTA` covers all road network operators, not just Waka Kotahi staff — contracted maintenance and alliance partners use it too. Lifeline utility operators (electricity, water, gas, fuel, telecommunications) follow the same pattern and identify their employer in the suffix rather than taking a prefix each.
- **Everyone is coloured by function, not organisation — foreign partners included.** An `AUS-FIRE-` track appears Red alongside FENZ; `AUS-MIL-` appears Brown alongside NZDF. The callsign identifies nationality, the colour identifies function, and foreign partners operate under the supporting NZ agency's incident command — they're never assigned the White (vendor) colour. See [Colour Coding](colour-coding.md) for the full function mapping.
- **Country codes** follow ISO 3166-1 alpha-3 (`AUS`, `USA`, `GBR`, `FJI`, etc.).

## Related

- [Colour Coding](colour-coding.md) — how each organisation appears visually on the map
- [Channel Structure](channels.md) — how channels group these callsigns together
