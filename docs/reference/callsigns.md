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

Regions use the official ISO 3166-2:NZ subdivision codes, with the `NZ-` country prefix omitted since it's redundant in a NZ-only context:

| Region | Code |
|---|---|
| Northland | `NTL` |
| Auckland | `AUK` |
| Waikato | `WKO` |
| Bay of Plenty | `BOP` |
| Gisborne | `GIS` |
| Hawke's Bay | `HKB` |
| Taranaki | `TKI` |
| Manawatū-Whanganui | `MWT` |
| Wellington | `WGN` |
| Tasman | `TAS` |

Regional identifiers are optional and at each organisation's discretion — not every organisation uses them.

## Examples

### Domestic callsigns

| Callsign | Interpretation |
|---|---|
| `FENZ-STL-JSmith` | FENZ, Southland, individual J. Smith |
| `FENZ-AUK-01` | FENZ, Auckland, unit 01 |
| `FENZ-JSmith` | FENZ, no region specified, individual J. Smith |
| `NZP-WGN-Badge4521` | NZ Police, Wellington, badge number 4521 |
| `LSAR-CAN-TeamA` | LandSAR, Canterbury, Team A |
| `RHT-AUK-Westpac1` | Rescue Helicopter, Auckland, Westpac 1 |
| `NZDF-INT-LiaisonA` | NZDF intelligence liaison (embedded role) |
| `NZP-CORR-OfficerB` | Corrections NZ officer operating under Police command |
| `VND-AcmeCorp-Tech1` | Vendor, Acme Corp, technician 1 |
| `NZTA-STL-Downer01` | Road Network Operations, Southland, Downer contractor unit 1 |

### Foreign partner callsigns

| Callsign | Interpretation |
|---|---|
| `AUS-FIRE-NSWRFS-Unit1` | Australian, fire function, NSW Rural Fire Service, Unit 1 |
| `AUS-FIRE-Smith` | Australian firefighter, Smith |
| `AUS-MIL-Jones` | Australian military, Jones |
| `USA-MIL-Williams` | US military, Williams |
| `AUS-POL-AFP-Badge123` | Australian law enforcement, Australian Federal Police, badge 123 |
| `AUS-MAR-AMSA-Vessel1` | Australian maritime, AMSA, Vessel 1 |
| `GBR-MED-Medic1` | British medical personnel, Medic 1 |

## Rules and guidance

**Mandatory prefix.** Every callsign must begin with the organisation prefix (domestic) or country code (foreign). Tracks without a recognised prefix should be treated as misconfigured and flagged for correction.

**Hyphen separator.** The hyphen (`-`) is the only permitted separator between components.

**Suffix format.** Each organisation determines its own suffix format:

- Full surname: `JSmith`
- Initials: `JS`
- Radio or badge ID: `Badge4521`
- Unit or callsign number: `01`, `Alpha1`

**Keep callsigns concise.** TAK displays callsigns on the map and in track lists. Long callsigns get truncated on smaller screens — aim for no more than 20 characters total where possible.

**Multi-organisation personnel.** Where someone holds roles in more than one organisation (e.g. a St John paramedic who is also a LandSAR volunteer), use the prefix for the role you're performing during the current incident, not your primary employer.

**Embedded and liaison roles.** Personnel operating under another organisation's command use that organisation's prefix with a sub-identifier indicating their origin:

- NZIC liaison embedded with NZDF: `NZDF-INT-[suffix]`
- Corrections NZ officer under Police command: `NZP-CORR-[suffix]`

**NZTA prefix applies to all road network operators.** The `NZTA` prefix represents road network operations as a whole, not Waka Kotahi employees specifically — contracted maintenance and alliance partners (Downer, Milford Road Alliance, Fulton Hogan, and others) all use it.

**Foreign partner colour assignment.** Foreign partners share the functional colour of the NZ agency role they're performing — `AUS-FIRE-` tracks appear in Red alongside FENZ, `AUS-MIL-` tracks appear in Brown alongside NZDF. The callsign prefix identifies nationality; colour identifies function. Foreign partners are never assigned the White (vendor) colour.

**Foreign partners operate under NZ command.** When foreign partners support a NZ agency, they're operationally subordinate to that agency's incident command — the shared functional colour reflects this.

**Vendor sub-prefixes.** Vendors supporting a specific organisation identify both their vendor status and the organisation they support:

- `VND-FENZ-[suffix]` for a vendor embedded with FENZ
- `VND-[CompanyName]-[suffix]` for a vendor supporting TAK.NZ infrastructure directly

**Country codes.** Use ISO 3166-1 alpha-3 codes for foreign partner countries: `AUS` (Australia), `USA` (United States), `GBR` (United Kingdom), `CAN` (Canada), `FJI` (Fiji), `PNG` (Papua New Guinea), `WSM` (Samoa), etc.

## Related

- [Colour Coding](colour-coding.md) — how each organisation appears visually on the map
- [Channel Structure](channels.md) — how channels group these callsigns together
