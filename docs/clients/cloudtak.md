---
description: How to access and use CloudTAK, TAK.NZ's browser-based client, including first login, drawing tools, overlays, and channels.
---

# CloudTAK

CloudTAK is TAK.NZ's browser-based client — the fastest way to get onto the Common Operating Picture with no installation. If you're new to TAK.NZ, start here.

## Accessing CloudTAK

1. Log in to the [account portal](../getting-started/index.md) at your organisation's TAK.NZ URL.
2. Select **CloudTAK** from your account dashboard.
3. CloudTAK opens directly in your browser — no download or install required.

CloudTAK works in any modern browser on desktop, tablet, or mobile, though a larger screen makes it easier to work with overlays and drawing tools.

## First login

The first time you log in, you'll be asked to set your **callsign** and device preferences:

1. **Callsign** — follow the TAK.NZ [Callsigns](../reference/callsigns.md) schema (`[ORG]-[REGION]-[SUFFIX]`), for example `FENZ-AUK-JSmith`.
2. **Marker colour** — this is set automatically based on your organisation. See [Colour Coding](../reference/colour-coding.md) if you want to understand why your dot is the colour it is.
3. **Role** — choose your role on the team (Team Member, Team Lead, Medic, etc.). If you're not sure, **Team Member** is the safe default.
4. When prompted, select **Allow** so CloudTAK can access your location. If your device doesn't have GPS (e.g. a desktop browser), you'll need to set your location manually — click the location button in the bottom-left corner and select your position on the map.

## Moving around the map

- **Pan** — click and drag.
- **Recenter on yourself** — click your callsign, or click the location button.
- **Rotate** — hold Ctrl and drag left or right.
- **Change perspective (tilt)** — hold Ctrl and drag up or down.
- **Zoom** — use the mouse wheel, or the **+**/**−** buttons in the top-right corner.
- **Search for an address** — use the search box at the top of the left panel, similar to a normal navigation app. Selecting a result recentres the map on that location.

## The basics

### Channels

Click **Channels** to see what's available to your account. Some channels are already enabled for you by default.

- Channels work like radio channels — to see other users, you both need to be on the same channel.
- **Regional channels** (e.g. `Regions - Canterbury`) are the primary coordination layer. When an emergency happens, all responding agencies activate that region's channel.
- **Organisation channels** (e.g. `FENZ`, `NZP-WGN`) are for internal agency coordination without broadcasting to everyone else.
- **National channels** (e.g. `Regions - All of New Zealand`) broadcast to all users nationwide, used for major events affecting the whole country.

Each channel shows two icons:

- An **eye** icon — open means the channel is on and sharing your location with everyone else on it; a slash through it means your presence is hidden from that channel.
- An **arrow** icon — a plain arrow means users on that channel can see each other; an arrow with a slash means the channel only supplies data (e.g. aircraft or hazard feeds) without mutual user visibility.

Your list of channels is unique to your account — some are created by your agency administrator and limited to your organisation, while others are shared across agencies for mutual aid. Only turn on mutual aid channels when you actually need them, and follow your agency's own policy on this. See [Channel Structure](../reference/channels.md) for the full national/regional/organisation breakdown.

!!! tip
    When you enable a new channel, wait 20–30 seconds for the map to populate with its icons and shapes.

### Basemaps

Click **Base Maps** to change the map style. Pick whichever basemap best suits the task at hand — imagery, topographic, or a simplified view.

### Map icons

Click on any icon on the map (for example, a flood gauge or a hazard marker) and read the **Remarks** field for additional detail about that item.

### Draw Tools

Click the pencil icon in the top-right corner to open the drawing tools:

| Tool | What it does |
|---|---|
| **Coordinate Input** | Places a marker at coordinates you type in |
| **Range & Bearing** | Draws a line at a specified bearing and distance from a chosen point |
| **Range Rings** | Draws rings at specified distances from a point — useful for evacuation planning, searches, or manhunts |
| **Draw Point** | Drops a marker from a choice of icons at a location you click |
| **Draw Line** | Places points to form a straight line; double-click to finish |
| **Draw Polygon** | Places points to form any shape; double-click the last point to close it |
| **Draw Rectangle** | Drop two points to set the height, then a third to set the width |
| **Draw Circle** | First click sets the centre, second sets the radius |
| **Draw Sector** | First click sets the centre, second sets the perimeter of the sector |
| **Lasso Select** | Draw a lasso around existing features to select them for sharing, deleting, or adding to a Data Package or Data Sync |
| **GeoJSON Import** | Imports a smaller GeoJSON file directly as editable features (these appear under **Your Features**, not as a toggleable overlay) |

Once a marker or shape is placed, click it to open its **radial menu** with options to edit, drag to reposition, lock (useful for tracked assets like aircraft or GPS trackers), delete, or open the side panel to edit its name, coordinates, icon, notes, attachments, or share it with other users. All shapes share a common radial menu for editing colour, opacity, line style, and centre coordinates.

CloudTAK supports many iconsets, selectable via a feature's **Style → Select Icon** menu. Specialty iconsets may not render correctly on other TAK clients — if unsupported, they typically show as a plain yellow clover icon on ATAK, TAK Aware, or WinTAK instead.

### Your Features

Open the hamburger menu (three lines, top-right) and select **Your Features** to see everything you've created, or that's been shared with you. Click a feature to snap the map to it. Every feature here is editable, and recently deleted features can be recovered.

### Overlays

Open **Overlays** to toggle data layers on or off using the eye icon. Click the **+** button to add pre-existing overlays such as NOAA-style radar, cell coverage maps, or boundary layers, depending on what's configured for TAK.NZ. Files you've imported can also be added here as overlays (see **Imports** below).

### Contacts

Open **Contacts** to see everyone online, plus anyone who recently disconnected. Use the filter/search bar to find a specific person. Clicking an online contact recentres the map on their position; clicking the chat bubble next to their name opens a direct chat with them.

### Data Sync (Missions)

CloudTAK supports Data Sync — TAK.NZ calls these **Missions**. A Mission is a shared "folder" hosted on the TAK Server, synchronised in real time to everyone subscribed. To create one, click the **+** button under Data Sync, name it, choose which channel(s) it's available on, and (optionally) set a password and roles (Owner, Subscriber, or Viewer). Selecting **Make Active** means anything you create in CloudTAK from then on is automatically added to the Mission.

This page covers the CloudTAK-specific controls; for the full concept and cross-client workflow (roles, adding content, sync status, deletion), see [Data Sync & Missions](../data-sync/index.md) and [Using Missions](../data-sync/using-missions.md).

### Data Packages

A Data Package bundles a set of features to share with other TAK users as a single unit — useful for things like a set of staging area markers or a hazard overlay.

To create one: use the **Lasso Select** tool to select features, click the three dots on the resulting menu, then **New Data Package**. Name it and choose which channel(s) it's available on; you can optionally attach a file.

!!! note
    Data Packages are cleared from the server every two months by default. Add `#permanent` under **Hashtags** if you want a package to stay available indefinitely.

To import an existing Data Package: make sure the right channel is active, select the package, and click **Import Package**. If it includes a file (e.g. a `.kmz`), select it under **Import Results** to add it to your overlays.

### Videos

Use the **Streams** tab to view any video feeds currently available on your channels. A "Video Server Error" usually means the stream isn't currently broadcasting, or isn't in a supported format. Use the **Leases** tab to set up a video lease and broadcast your own stream (for example, from a UAS) to other users on your channel.

### Chat

Open **Chat** to see all your current conversations, including [RELAY](../reference/relay.md), TAK.NZ's built-in AI assistant. Click the **+** button to start a new chat.

### Routes

Create and save a route between two points — either freehand (**No Snapping**) or snapped to roads and trails (**Roads & Trails**). Click once to start the route and again to finish; routes can be edited and shared like any other feature.

### Uploaded Files & Imports

Files you've imported appear under **Uploaded Files**. Selecting one lets you add it to the map as an overlay (toggle it via **Overlays**), download it, add it to a Data Sync or Data Package, or rename/delete it. Use **Imports → New Import** to upload a new file from your device.

### Settings

Open **Settings** to change your callsign, device preferences, and unit type (e.g. metric vs imperial) at any time.

## Tips for getting comfortable

- You can't break anything by clicking around — explore freely.
- Start with a small number of channels active (your region, plus your organisation) rather than everything at once, to avoid a cluttered map.
- If something looks wrong or missing, wait — CoT updates can take a few seconds to reach every client.

## Learning more

This page covers CloudTAK as configured for TAK.NZ. For the complete upstream CloudTAK user guide (which this page is adapted from), see:

- :material-web: [CloudTAK User Guide](https://docs.cloudtak.io/user/) — official CloudTAK documentation

## Next steps

Once you're comfortable with the basics, explore [Data Sync & Missions](../data-sync/index.md) or check the [Reference](../reference/callsigns.md) section for callsigns, channels, and colour coding.
