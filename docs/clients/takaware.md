# TAK Aware (iPhone/iPad)

TAK Aware is the recommended TAK client for Apple devices on TAK.NZ. It's a lightweight client built for modern iOS, designed so that anyone already familiar with ATAK can be operational quickly, while covering the core situational awareness and coordination features.

!!! note "iTAK"
    **iTAK** is also available as an alternative iOS client, enrolled the same way via its own tab in Team Manager's Enrollment page. This page focuses on TAK Aware, since it's the recommended default, but the same enrolment process applies if you use iTAK instead.

## Installing TAK Aware

1. Install **TAK Aware** from the Apple App Store.
2. Open the app and accept the permissions it requests (location, camera, notifications) — these are needed for position reporting, marker attachments, and alerts.
3. You'll be prompted to add a server connection. This is where you'll enrol your device (see below).

## Enrolling your device

Like ATAK, TAK Aware supports QR code enrolment, which is the fastest way to connect to the TAK.NZ server without manually entering server addresses or credentials.

1. Log in to [Team Manager](../getting-started/index.md) and open the **Enrollment** page (or click **Add Device** from your Dashboard).
2. Click **Generate Enrollment Data**, then select the **TAK Aware** tab. This creates a one-time enrollment code, valid for 30 minutes, shown as a QR code (and, if needed, a one-time username and password shown alongside it).
3. In TAK Aware, open the server connection screen and choose the option to scan a QR code.
4. Scan the code shown in Team Manager. TAK Aware will connect and enrol your device automatically.

Once enrolled, your position reports to the TAK Server (subject to your active channels), and you'll see other users, markers, and overlays on the map. Your device's certificate is valid for about a year — when it's getting close to expiring, return to the Enrollment page and generate a new one.

!!! tip "Enrolling directly from your iPhone or iPad"
    Team Manager also works in Safari on iOS. If you open the Enrollment page directly on the device you're enrolling, you'll see a direct "Enroll this device now" link instead of a QR code — you can skip scanning entirely. The QR code is only needed when enrolling from a separate device (you can't scan your own screen).

## The basics

### Your position and other users

Your position appears on the map, and other users appear as colour-coded markers based on their organisation — see [Colour Coding](../concepts/colour-coding.md). Tap any marker to see its details.

### Placing markers

Use TAK Aware's marker/point-dropping tool to place standard map markers — tap the map tools, choose an icon, and tap a location to place it. You can edit a marker's details (name, remarks, type) after placing it by tapping on it.

### Channels

Manage which channels you're subscribed to from the app's settings or channel selector. See [Channel Structure](../concepts/channels.md) for how TAK.NZ's channel hierarchy works, and disable channels you don't need to keep your map focused.

### GeoChat

Use GeoChat to message individuals or groups, including [RELAY](../reference/relay.md), TAK.NZ's built-in AI assistant.

### Maps and basemaps

!!! note
    TAK Aware may require a custom map source for offline map download, depending on version — the default basemap may not support offline download on its own. Check with your administrator for the recommended NZ map sources for your deployment.

### Data Sync (Missions)

TAK Aware supports Data Sync / Missions, letting you join a shared mission to receive and contribute map items, files, and updates. See [Data Sync & Missions](../data-sync/index.md).

## Learning more

For the full official reference, see the developer's guide:

- :material-file-pdf-box: [TAK Aware User Guide (PDF)](https://www.flighttactics.com/files/TAKAwareUserGuide.pdf) — published by Flight Tactics, the developer of TAK Aware

## Next steps

- [Data Sync & Missions](../data-sync/index.md) — sharing map items with your team
- [ATAK](atak.md) — if you need a feature not yet available in TAK Aware, note that ATAK on Android currently has the broader feature set
