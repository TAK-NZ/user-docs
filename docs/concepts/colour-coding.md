# Colour Coding

Every user on the TAK.NZ map is shown as a colour-coded dot. **The colour tells you what someone does, not which organisation employs them.**

## Why function, not organisation

During a multi-agency response, the question you need answered in the half-second you spend looking at a dot is *what kind of responder is that?* — a fire crew, a paramedic, a police unit. The specific employer matters far less in that moment, and it is already carried by the [callsign](callsigns.md).

Naming the colours by function has three practical consequences:

- **Foreign partners fit without special handling.** Australian fire crews supporting FENZ during a wildfire appear Red, because they are doing fire and rescue. Their nationality is in the callsign (`AUS-FIRE-NSWRFS-Unit1`), not the colour.
- **New organisations don't need new colours.** TAK provides exactly **14 team colours and no more**. A scheme named after organisations runs out; a scheme named after functions absorbs newcomers into an existing category.
- **The map stays readable as the network grows.** Coastguard and Surf Life Saving both do marine rescue. On a coastal callout, "there is a marine rescue asset here" is the operationally useful fact — not which of the two organisations it belongs to.

## Colour mapping

| Colour | Function | Covers |
|---|---|---|
| :material-circle:{ style="color: #E53935" } Red | **Fire & Rescue** | Fire and Emergency New Zealand (FENZ), including rural fire and USAR; foreign fire services and wildfire crews |
| :material-circle:{ style="color: #1E88E5" } Blue | **Police, Border & Law Enforcement** | New Zealand Police; New Zealand Customs Service, Immigration New Zealand; foreign police and border agencies |
| :material-circle:{ style="color: #43A047" } Green | **Health & Ambulance** | Hato Hone St John, Wellington Free Ambulance, air ambulance and rescue helicopter; Health New Zealand (Te Whatu Ora), public health units; foreign medical teams and field hospitals |
| :material-circle:{ style="color: #FB8C00" } Orange | **Land Search & Rescue** | Land Search and Rescue NZ (LandSAR), Alpine Cliff Rescue, Cave SAR; foreign land SAR teams |
| :material-circle:{ style="color: #00897B" } Teal | **Marine Search & Rescue** | Coastguard New Zealand, Surf Life Saving New Zealand; foreign marine rescue crews |
| :material-circle:{ style="color: #D81B60" } Magenta | **Maritime & Aviation Authority** | Maritime New Zealand, Rescue Coordination Centre NZ (RCCNZ), harbourmasters, port authorities; Airways, airport authorities |
| :material-circle:{ style="color: #8E24AA" } Purple | **Emergency Management & Coordination** | National Emergency Management Agency (NEMA), CDEM Groups, EOC and ECC personnel, welfare coordination; foreign civil defence agencies |
| :material-circle:{ style="color: #6D4C41" } Brown | **Military** | New Zealand Defence Force (NZDF); foreign military |
| :material-circle:{ style="color: #1B5E20" } Dark Green | **Conservation & Land Management** | Department of Conservation (DOC); regional council land, river and flood management teams |
| :material-circle:{ style="color: #FDD835" } Yellow | **Roading & Transport Network** | NZTA and its contracted maintenance and alliance partners; territorial authority roading teams; KiwiRail |
| :material-circle:{ style="color: #1A237E" } Dark Blue | **Lifeline Utilities** | Electricity (Transpower, lines companies), water and wastewater, gas, fuel, telecommunications |
| :material-circle:{ style="color: #6A1B1A" } Maroon | **Humanitarian & Welfare** | New Zealand Red Cross, Salvation Army, Victim Support, iwi and community welfare providers |
| :material-circle:{ style="color: #E0E0E0; border: 1px solid #999;" } White | **Vendor & Technical Support** | TAK.NZ platform operators, integrators, and vendor technical staff |

Every foreign partner function code maps to exactly one colour in this table, so a foreign track is coloured by the same rule as a domestic one. See [Callsigns](callsigns.md) for the code list.

## Reserved colour

| Colour | Status |
|---|---|
| :material-circle:{ style="color: #00ACC1" } Cyan | Reserved — not currently assigned |

TAK's 14 team colours cannot be extended, so the last unassigned colour is held rather than spent. It will be allocated when a category emerges that genuinely cannot fold into an existing function — community and iwi response, and animal welfare, are the current candidates.

!!! note "Why some organisations share a colour"
    Health New Zealand shares Green with the ambulance services, and Customs shares Blue with Police, because in each case the field function is the same one. This also makes the palette easier to read: TAK's colour set contains four blues and two greens, and fewer near-identical colours means fewer misreads on a small screen in poor light.

## How your colour is assigned

Your colour follows from your organisation's function, so you don't normally choose it — it's configured when your account is set up and applied by your client automatically. See [Account Management](../getting-started/account-management.md) if your colour looks wrong for the work you do.

Personnel who hold roles in more than one organisation use the colour and [callsign prefix](callsigns.md) for whichever role they're performing during the current incident.

## Roles: the other half of your map symbol

Colour is only half of what your dot conveys. ATAK, WinTAK and TAK Aware also show a **role**, rendered as a letter or symbol inside the dot — for example **TL** for Team Lead, **HQ** for Headquarters, or **+** for Medic.

The two carry deliberately different information:

| | Carries | Changes |
|---|---|---|
| **Colour** | Your discipline — what kind of responder you are | Rarely. Set with your account. |
| **Role** | Your function in *this* response — team leader, incident management, medical, communications | Per incident, as your assignment changes |

That split matters for CIMS (the Coordinated Incident Management System): a FENZ station officer might lead a crew in the morning and sit in the Incident Management Team in the afternoon. Their colour stays Red; their role changes.

!!! warning "Role naming is not yet aligned to CIMS"
    The role options available in TAK come from the platform's military and US public-safety origins — including Sniper, Forward Observer and RTO — and don't map cleanly onto CIMS functions. Several CIMS functions, notably **Safety**, **Welfare** and **Public Information Management**, have no corresponding role at all. A revised role mapping is planned. Until then, choose the closest available option and rely on your callsign and radio for anything the role can't express.

## Related

- [Callsigns](callsigns.md) — the standardised naming schema that identifies each track alongside its colour
- [Channel Structure](channels.md) — how these functions are grouped for coordination
- [ATAK](../clients/atak.md) — how colours and role letters are drawn on the map
