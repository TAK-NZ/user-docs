# The TAK.NZ Network

TAK.NZ is New Zealand's shared Common Operating Picture (COP) platform for emergency responders. It lets multiple agencies — Fire and Emergency NZ (FENZ), NZ Police, Hato Hone St John / Wellington Free Ambulance, Air Ambulance & Rescue Helicopter, Health NZ, LandSAR, NEMA, NZ Defence Force, Coastguard, and others — see each other on a shared map in real time during emergencies, training, or day-to-day operations.

## Who uses TAK.NZ

TAK.NZ is designed around New Zealand's public safety and emergency management sector, including:

- **Fire and Emergency New Zealand (FENZ)** — structure fires, wildfires, road crash rescue, hazardous materials
- **New Zealand Police** — law enforcement, search coordination, event security
- **Hato Hone St John / Wellington Free Ambulance / Air Ambulance & Rescue Helicopter** — medical response, including air assets
- **Health New Zealand (Te Whatu Ora)** — health system coordination
- **Land Search and Rescue NZ (LandSAR)** — search and rescue operations, particularly in remote or rural areas
- **National Emergency Management Agency (NEMA)** — civil defence emergency management coordination
- **New Zealand Defence Force (NZDF)** — support to civil authorities, humanitarian assistance and disaster relief
- **Coastguard New Zealand, NZ Customs, Maritime New Zealand** — maritime safety and enforcement
- **Department of Conservation (DOC), NZTA/Waka Kotahi and road network partners, NZ Red Cross** — supporting roles across environment, transport, and welfare

Every organisation on TAK.NZ has a standardised [callsign prefix](../reference/callsigns.md) and [colour](../reference/colour-coding.md), so anyone looking at the map can immediately tell who they're looking at.

## How the network is structured

TAK.NZ uses a three-layer **channel** structure to balance shared situational awareness with each organisation's need for internal coordination:

1. **National** — for events affecting the whole country (e.g. `Regions - All of New Zealand`)
2. **Regional** — one channel per NZ region, and the primary coordination layer for any emergency event (e.g. `Regions - Canterbury`)
3. **Organisation** — internal agency coordination that doesn't need to broadcast to every other responder (e.g. `FENZ`, `NZP-WGN`)

When an emergency happens in a region, every responding agency activates that region's channel and immediately sees everyone else who's active there — no manual configuration required. See [Channel Structure](../reference/channels.md) for the complete picture, including overseas deployment channels used when NZ personnel deploy to the Pacific or further afield.

## International partnerships

TAK.NZ is built on the same underlying platform as **COTAK** (the Colorado Team Awareness Kit), one of the most mature TAK deployments for civilian public safety in the world. This means training material, workflows, and lessons learned from COTAK's public safety community carry across directly to TAK.NZ.

New Zealand also has an established, ongoing role supporting Pacific Island nations during emergencies. TAK.NZ reflects this with standing `Overseas -` channels for Pacific partner countries, so agencies like NEMA and NZDF can maintain shared awareness and interoperability with the Pacific between deployments, not just during them.

## RELAY: the TAK.NZ AI assistant

TAK.NZ includes **RELAY** (Rapid Emergency Liaison and Advisory for You), a GenAI-powered assistant available directly inside GeoChat on any client. RELAY can answer questions about NZ emergency doctrine (CIMS, the FENZ Act, the CDEM Act), pull live road closure data, report current GeoNet earthquake and volcanic alert data, and even place markers on your map based on what you ask it. See [RELAY Assistant](../reference/relay.md) for details.

## Next steps

Head to [Getting Started](../getting-started/index.md) to create your TAK.NZ account.
