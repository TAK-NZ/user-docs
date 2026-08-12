# What is TAK?

TAK stands for **Team Awareness Kit**. It's a "dots on a map" technology: a live, shared map where every responding unit, vehicle, aircraft, hazard, and point of interest is visible to everyone who's looking at the same channel.

TAK was originally developed by the US Air Force Research Laboratory for military use, and was adopted by the US Department of Homeland Security from 2017 onwards for disaster response coordination between agencies. It has since become the standard shared situational awareness platform for public safety agencies internationally, precisely because it solves a problem every emergency response has: **knowing who is where, in real time, across agencies that don't normally share a radio channel or a records system.**

TAK.NZ brings this same platform to New Zealand, tailored for our agencies, our regions, and the way our emergency response actually works.

## The problem TAK solves

During a multi-agency response — a wildfire, a flood, a search and rescue operation, a major traffic incident — every agency involved usually has its own radios, its own mapping tools, and its own way of tracking its people. That means:

- FENZ can see FENZ crews, but not where Police or LandSAR are operating
- Coordinating in the same physical area, agencies still spend time on the radio just confirming positions
- Hazard information (fire perimeters, flood extents, road closures) has to be relayed verbally or shared as static PDFs and screenshots, which go out of date immediately

TAK addresses this by giving every responder — regardless of agency — a live position on a **single shared map**, along with the ability to draw, annotate, chat, and share data layers on top of it.

## Core concepts

### Common Operating Picture (COP)

The Common Operating Picture is the shared map itself: everyone's position, plus any markers, shapes, hazard overlays, or data feeds that have been added to the channels you're subscribed to. Everyone looking at the same channel sees the same COP, updated in real time.

### Cursor on Target (CoT)

Every dot on the map — a person, a vehicle, an aircraft, a marker — is represented internally as a small piece of data called **Cursor on Target (CoT)**. CoT is the common "language" that lets ATAK, TAK Aware, WinTAK, CloudTAK, external sensors (like ADS-B aircraft feeds), and the TAK Server all talk to each other, regardless of which client or device produced the data. You don't need to understand CoT to use TAK.NZ, but it's why data flows so easily between very different types of devices and feeds.

### TAK Server

The TAK Server is the central hub that all clients connect to. It's what makes the "shared" part of the Common Operating Picture possible — it receives position updates, chat messages, and data from every connected client, and distributes them to everyone else who should see them, based on channel membership. TAK.NZ operates and manages this infrastructure so agencies don't have to run their own.

### Channels

Channels work like radio channels: to see other users, you both need to be on the same channel. TAK.NZ uses a three-layer channel structure — national, regional, and organisation — designed specifically around how NZ agencies coordinate. See [Channel Structure](../reference/channels.md) for the full breakdown.

### Clients

A client is the app you actually use to view and interact with the Common Operating Picture:

| Client | Platform | Best for |
|---|---|---|
| **CloudTAK** | Any web browser | Quick access, no install, desktop dispatch/coordination |
| **ATAK** | Android phone/tablet | Field operators, most features, most actively developed |
| **TAK Aware** | iPhone/iPad | Field operators on Apple devices |
| **WinTAK** | Windows laptop/desktop | Vehicle-mounted or command post displays |

All four clients connect to the same TAK Server and show the same underlying data — they just present it differently depending on the device. See [Choosing a Client](../clients/index.md) for a full comparison.

### Callsigns and colour coding

Every user on the map has a standardised callsign (e.g. `FENZ-AUK-JSmith`) and appears as a colour-coded dot based on their organisation (Red for FENZ, Blue for Police, Green for ambulance, and so on). This lets you identify who you're looking at on the map at a glance, even during a large multi-agency response. See [Callsigns](../reference/callsigns.md) and [Colour Coding](../reference/colour-coding.md) for the full schema.

## Next steps

Ready to get hands-on? Head to [Getting Started](../getting-started/index.md) to create your account, or read on to [The TAK.NZ Network](tak-nz-network.md) to understand how New Zealand's specific deployment is put together.
