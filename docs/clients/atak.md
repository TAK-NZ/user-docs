# ATAK (Android)

ATAK (Android Team Awareness Kit) is the most feature-complete TAK client, and the one most field operators use day to day. It runs on Android phones and tablets.

## Installing ATAK

1. Install ATAK from the Google Play Store, or from an APK provided by your agency if you're on a managed device.
2. Open the app. The first time it runs, ATAK will:
    - Generate an encryption passphrase automatically (you can change this later under **Settings > Callsign and Device Preferences > Encryption Password**)
    - Ask you to accept the End User License Agreement (EULA)
    - Request permissions for location, storage, camera, and other device features ATAK needs to function
3. You'll land on the **TAK Device Setup** screen. You can adjust these settings later, so don't worry about getting everything right immediately.

## Enrolling your device

The fastest way to connect ATAK to the TAK.NZ server is by scanning a QR code, rather than manually typing in server addresses and credentials.

1. Log in to the [account portal](../getting-started/index.md) and select **TAK Device Enrollment**.
2. Choose **ATAK** as your device type. The portal will generate a QR code (and, if needed, a one-time username and password shown alongside it).
3. On your Android device, open ATAK and go to the server connection screen (usually presented automatically on first launch, or under **Settings > Network Preferences > TAK Servers**).
4. Select the option to scan a QR code, then scan the code shown in the account portal.
5. ATAK will connect to the TAK.NZ server and enrol your device automatically.

Once enrolled, your position will start reporting to the TAK Server (subject to your active channels) and you'll be able to see other users, markers, and overlays on the map.

!!! tip "Enrolling directly from your Android device"
    The account portal and TAK Device Enrollment app work fine in a mobile browser too. If you open them directly on the Android phone or tablet you're enrolling, you can enrol that device without scanning a QR code at all — the QR code is only needed when enrolling from a separate device.

## The basics

### Your Self-Marker

By default, your position is shown as a blue arrowhead with a white outline. Other users appear as colour-coded circles based on their organisation (see [Colour Coding](../concepts/colour-coding.md)), with a letter inside indicating their role — for example, **TL** for Team Lead, **HQ** for Headquarters, **+** for Medic.

- A **solid** marker means the user has GPS reception.
- A marker with a **diagonal line** means GPS location isn't currently available for that user.

You can customise the appearance of your own marker under **Settings > Display Preferences > My Location Color/Size**.

### Placing markers (Point Dropper)

Use the **Point Dropper** tool to place a standardised marker on the map:

1. Select the Point Dropper icon from the toolbar.
2. Choose an affiliation (Unknown, Neutral, Red, Friendly) and an icon from the palette.
3. Tap a location on the map to drop the marker.

You can long-press a location instead to manually enter coordinates, and edit a marker's details (name, type, remarks, status) afterwards using its radial menu.

### The radial menu

Tapping any marker or your own Self-Marker brings up a **radial menu** with quick actions — Fine Adjust (reposition), Details, Send, Delete, and more, depending on the marker type. Long-press specific radial options (like Fine Adjust) to open sub-menus with additional controls.

### Channels

Manage which channels you're subscribed to under **Settings** or via the channel/groups selector, depending on your ATAK version. See [Channel Structure](../concepts/channels.md) for how TAK.NZ's national, regional, and organisation channels work.

### GeoChat

Use **GeoChat** to send messages to individuals or groups. Messages are tied to geographic context, so you can see where a message originated. GeoChat is also where you can talk to [RELAY](../reference/relay.md), TAK.NZ's built-in AI assistant — just message RELAY like you would any other contact.

### Overlay Manager

The **Overlay Manager** organises everything on your map — markers, shapes, data packages, hashtags, and more — into categories you can filter and search. This is a good place to find something you know is on the map but can't immediately see.

### Data Sync (Missions)

ATAK's **Data Sync** plugin lets you join or create a Mission to share map items, files, photos, and updates with your team in real time, including while offline (changes sync when you reconnect). See [Data Sync & Missions](../data-sync/index.md) for a full walkthrough.

## Learning more

ATAK has a large feature set beyond the basics above — including routes and navigation (Bloodhound), drawing tools, CASEVAC, video feeds, and elevation tools. For the full picture, download the official reference guides:

- :material-file-pdf-box: [ATAK Software User Manual (PDF)](../assets/downloads/atak-user-guide-5.8.pdf) — the complete ATAK manual, covering every tool in detail
- :material-file-pdf-box: [ATAK Data Sync User Guide (PDF)](../assets/downloads/atak-data-sync-user-guide-5.8.0.pdf) — a focused guide to the Data Sync plugin covered in [Data Sync & Missions](../data-sync/index.md)

## Next steps

- [Data Sync & Missions](../data-sync/index.md) — sharing map items with your team
- [Callsigns](../concepts/callsigns.md) and [Colour Coding](../concepts/colour-coding.md) — understanding what you see on the map
