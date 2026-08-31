# WinTAK (Windows)

WinTAK is the TAK client for Windows laptops and desktops. It covers most of ATAK's feature set, and is well suited to vehicle-mounted displays, command posts, or planning work where a larger screen and keyboard/mouse input are more practical than a phone.

## Installing WinTAK

1. Download WinTAK from the source provided by your TAK.NZ administrator (WinTAK isn't distributed through a public app store).
2. Run the installer and follow the setup prompts.
3. Launch WinTAK. You'll be prompted to configure a server connection.

## Connecting to the TAK.NZ server

Unlike ATAK and TAK Aware, WinTAK doesn't support QR code enrolment — but connecting is still self-service, through [Team Manager](../getting-started/index.md)'s Enrollment page, not something you need to request from an administrator.

1. Log in to [Team Manager](../getting-started/index.md) and open the **Enrollment** page (or click **Add Device** from your Dashboard).
2. Click **Generate Enrollment Data**, then select the **Manual / WinTAK** tab. You'll see your server address, port, username, and a password you can copy to your clipboard.
3. In WinTAK, open **Settings > Network Preferences > TAK Servers** (menu location may vary slightly by version).
4. Add a new server connection using the address, port, username, and password from Team Manager.
5. Once connected, your position reports to the TAK Server (subject to your active channels) and you'll see other users and map data.

!!! note
    Your enrollment code and password are only valid for 30 minutes, and your device certificate is valid for about a year. If it expires, come back to the Enrollment page to generate a new one.

## The basics

### The map and your position

WinTAK shows the same Common Operating Picture as ATAK, TAK Aware, and CloudTAK. Your position appears on the map, and other users appear as colour-coded markers by organisation — see [Colour Coding](../concepts/colour-coding.md).

### Placing markers

Use WinTAK's marker tools to drop standard map markers, similar to ATAK's Point Dropper. Select an icon and click a location on the map to place it, then edit its details as needed.

### Channels

Manage your active channels from WinTAK's settings. See [Channel Structure](../concepts/channels.md) — the same Response/Support/organisation hierarchy applies across every client.

### GeoChat

WinTAK supports GeoChat for messaging individuals and groups, including [RELAY](../reference/relay.md).

### Downloading basemaps

WinTAK supports downloading basemaps for offline use — useful for command posts or vehicles operating with intermittent connectivity. Check with your administrator for recommended NZ basemap sources.

### Data Sync (Missions)

WinTAK supports Data Sync / Missions for sharing map items, files, and updates with your team. See [Data Sync & Missions](../data-sync/index.md).

## Next steps

- [Data Sync & Missions](../data-sync/index.md) — sharing map items with your team
- [Clients Overview](index.md) — compare WinTAK against other clients
