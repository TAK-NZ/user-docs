# Callsigns

TAK.NZ uses a standardised callsign prefix schema so every track on the Common Operating Picture is immediately identifiable by organisation, and optionally by region or sub-unit.

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
| Land Search and Rescue NZ (LandSAR) | `LSAR` |
| Health New Zealand (Te Whatu Ora) | `HNZ` |
| New Zealand Red Cross | `NZRC` |
| Coastguard New Zealand | `CGRD` |
| New Zealand Customs Service | `CUST` |

## Function codes (foreign partners)

| Function | Code | Covers |
|---|---|---|
| Fire | `FIRE` | Fire brigades, wildfire crews |
| Police / Law Enforcement | `POL` | Police, border force, federal agents |
| Military | `MIL` | Army, Navy, Air Force, National Guard |
| Medical / Ambulance | `MED` | Paramedics, field hospitals, medical teams |
| Search and Rescue | `SAR` | Search and rescue teams |
| Maritime | `MAR` | Coast guard, maritime safety |
| Civil Defence / Emergency Management | `CDEM` | FEMA equivalents, state emergency services |
| Logistics / Support | `LOG` | Supply, transport, engineering support |

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

## Rules and guidance

- **Mandatory prefix, hyphen-separated.** Every callsign must start with the organisation prefix (domestic) or country code (foreign), using `-` as the only separator. Tracks without a recognised prefix should be flagged as misconfigured.
- **Suffix format is organisation-specific** — a surname (`JSmith`), initials (`JS`), a radio/badge ID (`Badge4521`), or a unit number (`01`, `Alpha1`).
- **Keep it short.** TAK truncates long callsigns on smaller screens — aim for 20 characters or fewer.
- **Special cases use a sub-identifier after the primary prefix** — for example, personnel embedded with or operating under another organisation's command (`NZDF-INT-[suffix]`), or a vendor supporting a specific agency (`VND-FENZ-[suffix]`). Personnel holding roles in more than one organisation use the prefix for whichever role they're performing during the current incident.
- **`NZTA` covers all road network operators**, not just Waka Kotahi staff — contracted maintenance and alliance partners use it too.
- **Foreign partners are coloured by function, not nationality.** An `AUS-FIRE-` track appears Red alongside FENZ; `AUS-MIL-` appears Brown alongside NZDF. The callsign identifies nationality, colour identifies function, and foreign partners operate under the supporting NZ agency's incident command — they're never assigned the White (vendor) colour.
- **Country codes** follow ISO 3166-1 alpha-3 (`AUS`, `USA`, `GBR`, `FJI`, etc.).

## Related

- [Colour Coding](colour-coding.md) — how each organisation appears visually on the map
- [Channel Structure](channels.md) — how channels group these callsigns together
