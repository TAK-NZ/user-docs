# Account Management

TAK.NZ's account portal is **TAK Team Manager**, at [https://team.tak.nz/](https://team.tak.nz/). This is where you manage your TAK.NZ identity day-to-day: your profile, your team, your device enrolments, and (depending on your role) your team's members and channels. It works the same way in a mobile browser as on desktop, so you can manage your account from your phone or tablet without needing a computer.

Behind the scenes, Team Manager talks to **Authentik**, TAK.NZ's identity provider, which handles the actual sign-in and a small number of security settings (passwords, passkeys, and other MFA devices) directly. You'll only need to visit Authentik itself for those — everything else, including your username, display name, TAK callsign, and channel membership, is managed in Team Manager.

## Logging in

1. Go to [https://team.tak.nz/](https://team.tak.nz/).
2. Clicking log in redirects you to Authentik to sign in — with a password, or with a linked Google or Apple account.
3. You're brought back to your Team Manager **Dashboard** automatically.

To log out, use the menu in Team Manager's top navigation bar. This also ends your Authentik session, not just your session in Team Manager itself.

## Setting up a passkey (recommended)

Remembering a password and keeping it in sync across devices is a hassle. TAK.NZ supports **passkeys** via Authentik's built-in WebAuthn support — a modern sign-in method tied to your device's fingerprint, Face ID, PIN, or a hardware security key, instead of a typed password.

To add a passkey:

1. Go to [https://account.tak.nz/](https://account.tak.nz/) — this is Authentik itself, separate from the Team Manager portal.
2. Log in, then click the **gear icon** in the top-right corner to open your user settings.
3. Go to the **Credentials** tab.
4. Under **MFA Devices**, select the option to enrol a new device and choose **WebAuthn device**.
5. Follow your browser or device's prompt to create the passkey (fingerprint, Face ID, PIN, or security key), then give the device a recognisable name (e.g. "Work laptop" or "Personal phone").

Repeat this for each device you use to log in. Once a passkey is set up, you can use it to sign in on that device instead of typing your password.

!!! note
    Authentik also supports TOTP (authenticator app) and static recovery tokens as additional MFA options under the same **Credentials** tab, alongside WebAuthn passkeys. The same page is also where you can change your password directly, and where the **Sessions** tab lets you view and sign out other devices currently logged in, and **Connected services** lets you link or unlink Google/Apple sign-in.

Passkeys apply to signing in to Team Manager and CloudTAK through Authentik. Mobile clients (ATAK/TAK Aware/iTAK) don't use your Authentik password at all — they connect using enrolment credentials generated per-device in Team Manager, covered below.

## Your Dashboard

After logging in to Team Manager, your Dashboard shows:

- **TAK Profile** — your callsign, your TAK role, your team's colour/function, your organisation, and your team (with a lock icon if your team is private). If you don't currently belong to a team, this reads literally "None" rather than being blank.
- **My Devices** — every TAK device you've enrolled, with its name, type, when it was last seen, and its status. From here you can add a new device or revoke one you no longer use.
- **My Channels** — a searchable, expandable folder tree of every TAK channel you have access to, each one marked Read, Write, or Read-Write.
- **Pending Requests** — if you're a team admin and there are requests waiting for review, a banner links you straight to the Requests page.

## Enrolling a device

From your Dashboard, click **Add Device** (or go to the Downloads and Enrollment pages directly) to connect ATAK, TAK Aware, iTAK, or WinTAK to the TAK.NZ server. See [Choosing a Client](choosing-a-client.md) for the full walkthrough, including QR code enrolment.

## Team admin functions

If you're a team admin — either promoted by another admin, or an admin of a team above yours in the hierarchy — you'll see additional pages and actions in Team Manager for managing your team's members, sub-teams, devices, and channels, and for reviewing access requests. See [Team Administration](team-administration.md) for the full guide.

## Need help?

If you're locked out, can't find an expected channel, or aren't sure who your administrator is, reach out through your agency's usual TAK.NZ point of contact, or ask **RELAY** in GeoChat once you have a client set up — see [RELAY Assistant](../reference/relay.md).
