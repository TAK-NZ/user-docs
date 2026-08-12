# Colour Coding

Every user on the TAK.NZ map is shown as a colour-coded dot based on their organisation. This lets you identify who you're looking at during a multi-agency response at a glance, without needing to check every callsign individually.

## Colour mapping

| Colour | Organisation |
|---|---|
| :material-circle:{ style="color: #E53935" } Red | Fire and Emergency New Zealand (FENZ) |
| :material-circle:{ style="color: #1E88E5" } Blue | New Zealand Police |
| :material-circle:{ style="color: #43A047" } Green | Hato Hone St John / Wellington Free Ambulance / Air Ambulance & Rescue Helicopter |
| :material-circle:{ style="color: #00ACC1" } Cyan | Health New Zealand (Te Whatu Ora) |
| :material-circle:{ style="color: #FB8C00" } Orange | Land Search and Rescue NZ (LandSAR) |
| :material-circle:{ style="color: #8E24AA" } Purple | National Emergency Management Agency (NEMA) |
| :material-circle:{ style="color: #6D4C41" } Brown | New Zealand Defence Force (NZDF) |
| :material-circle:{ style="color: #00897B" } Teal | Coastguard New Zealand |
| :material-circle:{ style="color: #FDD835" } Yellow | Road Network Operations (NZTA; contracted maintenance and alliance partners) |
| :material-circle:{ style="color: #1A237E" } Dark Blue | New Zealand Customs Service |
| :material-circle:{ style="color: #1B5E20" } Dark Green | Department of Conservation (DOC) |
| :material-circle:{ style="color: #D81B60" } Magenta | Maritime New Zealand |
| :material-circle:{ style="color: #6A1B1A" } Maroon | New Zealand Red Cross |
| :material-circle:{ style="color: #E0E0E0; border: 1px solid #999;" } White | Vendor / Technical Support |

## Why these colours were chosen

Colours follow internationally recognised conventions wherever possible:

- **Red for fire** and **Blue for police** are universal, widely recognised standards.
- **Green for medical and ambulance** aligns with New Zealand's ambulance livery and the broader clinical response community, including air ambulance assets.
- **Orange for search and rescue** reflects the international safety-orange convention used in SAR equipment and operations.
- **Dark Blue for Customs** reflects both the blue livery of NZ Customs vessels and the enforcement nature of their role, positioning them adjacent to Police in the law enforcement spectrum.
- **Teal for Coastguard** distinguishes this volunteer rescue organisation from enforcement agencies — teal is a maritime colour reflecting sea-rescue identity without implying enforcement authority.
- **Dark Green for DOC** directly reflects the green uniforms, vehicles, and signage used by DOC rangers in the field.
- **Brown for NZDF** reflects the brown and tan tones of NZDF field uniforms (DPCU camouflage). Blue is reserved for NZ Police — TAK.NZ is a civilian emergency management Common Operating Picture, not a military battlespace management system, so the "blue force" convention used in defence contexts doesn't apply here.
- **Yellow for road network operations** reflects the high-visibility safety yellow universally associated with roading, construction, and traffic management, covering NZTA/Waka Kotahi and contracted partners like Downer and Milford Road Alliance.
- **Magenta for Maritime NZ** distinguishes the regulatory and coordination authority from operational maritime responders like Coastguard and Customs.
- **White is reserved for vendors and technical support** as a neutral, non-operational colour.

Air Ambulance and Rescue Helicopter assets share Green with ground ambulance, since they operate within the same clinical and coordination umbrella.

## Organisations without a dedicated colour

Not every government organisation gets its own colour slot. The principle applied is that TAK.NZ represents **operational field presence** — organisations that coordinate, support, or have jurisdiction but don't deploy personnel to incident scenes are better handled through a liaison role within an existing colour group, rather than occupying a dedicated slot:

- **NZIC** (New Zealand Intelligence Community) doesn't deploy to incident scenes. An embedded intelligence liaison operates under NZDF (Brown) using a `NZDF-INT-` callsign prefix.
- **Corrections NZ** isn't a primary emergency responder. Where Corrections staff have a rare field role (e.g. perimeter security or prisoner transport during an evacuation), they operate under NZ Police (Blue) using a `CORR-` callsign prefix, reflecting the command relationship in those scenarios.

## Related

- [Callsigns](callsigns.md) — the standardised naming schema that identifies each track alongside its colour
- [Channel Structure](channels.md) — how these organisations are grouped for coordination
