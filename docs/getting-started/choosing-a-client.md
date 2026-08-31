# Choosing a Client

TAK.NZ works across four clients, all connected to the same TAK Server and showing the same Common Operating Picture. Which one you use depends on your device and your role.

| Client | Platform | Install required? | Best for |
|---|---|---|---|
| **[CloudTAK](../clients/cloudtak.md)** | Any browser | No | Quick access, evaluators, desktop/dispatch use |
| **[ATAK](../clients/atak.md)** | Android phone/tablet | Yes | Field operators — most features, most actively developed |
| **[TAK Aware](../clients/takaware.md)** | iPhone/iPad | Yes | Field operators on Apple devices |
| **[WinTAK](../clients/wintak.md)** | Windows laptop/desktop | Yes | Vehicle-mounted displays, command posts, planning |

!!! note "iTAK"
    **iTAK** is also available on iPhone/iPad as an alternative to TAK Aware, and can be enrolled the same way via a dedicated QR code tab in Team Manager's Enrollment page. TAK Aware is the recommended default for most Apple users, but iTAK is there if you prefer it or a specific feature you need is only available there.

## If you're not sure

Start with **CloudTAK**. It requires no installation, runs in any modern browser, and gives you the full Common Operating Picture — channels, map icons, overlays, data packages, and chat — without needing to enrol a device first. It's the fastest way to get a feel for the platform.

Once you're comfortable with the basics, move to a mobile client (ATAK or TAK Aware) if you need TAK in the field, on a device that goes with you and reports your live position.

## Feature comparison at a glance

- **ATAK** has the broadest feature set and the most active development, since it's the reference implementation most plugins and integrations are built for.
- **TAK Aware** covers the core situational awareness and coordination features but doesn't yet have full feature parity with ATAK.
- **WinTAK** covers most ATAK features on a Windows desktop or laptop, useful where a larger screen or keyboard/mouse input is more practical than a phone.
- **CloudTAK** runs anywhere with a browser and is TAK.NZ's own web client, actively developed alongside the rest of the platform.

## Enrolling a device

Every client — including WinTAK — is enrolled the same way, self-service, through Team Manager's **Enrollment** page (`/enrollment`, also linked from your Dashboard's "Add Device" button). You'll see a summary of what will be enrolled (your TAK Server address, username, callsign, colour, role, and how many active devices you already have) before anything is created.

Click **Generate Enrollment Data** to create a one-time enrollment code, valid for **30 minutes**, shown across separate tabs:

- **ATAK** (Android) and **TAK Aware** / **iTAK** (iOS) — support **QR code enrolment**, which connects a device to the TAK.NZ server without manually typing in server addresses or credentials. If you're viewing the Enrollment page on the device itself, you'll see a direct "Enroll this device now" link instead — you can skip the QR code entirely and enrol on the spot. The QR code is only needed when generating the enrolment from a *different* device, for example an admin setting up a device on someone else's behalf (you can't scan your own screen).
- **Manual / WinTAK** — WinTAK doesn't support QR code scanning, so this tab gives you everything to type in by hand instead: server address, port, username, and a password you can copy to your clipboard (it's never shown as plain text).

Your enrolled device's certificate is valid for about a year; when it's getting close to expiring, come back to the Enrollment page and generate a new one. Full steps for each client are covered on its own page:

- [ATAK enrolment](../clients/atak.md#enrolling-your-device)
- [TAK Aware enrolment](../clients/takaware.md#enrolling-your-device)
- [WinTAK connection](../clients/wintak.md#connecting-to-the-taknz-server)

## Next steps

Pick your client from the list above, or head to the [Clients overview](../clients/index.md) to compare them side by side before installing.
