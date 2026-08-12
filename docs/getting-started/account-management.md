# Account Management

TAK.NZ's account management portal is built on **Authentik**, an open source identity provider. This is where you manage your TAK.NZ identity: your profile, your login methods, your device enrolments, and (depending on your role) your channel access.

## Logging in

1. Go to your organisation's account portal (e.g. [https://account.demo.tak.nz/](https://account.demo.tak.nz/)).
2. Sign in with your password, or with a linked Google, Apple, or LinkedIn account.
3. You'll land on the **Application Dashboard** — the main Authentik landing page, showing the applications you have access to (such as CloudTAK and TAK device enrolment).

## Setting up a passkey (recommended)

Remembering a password and keeping it in sync across devices is a hassle. TAK.NZ supports **passkeys** via Authentik's built-in WebAuthn support — a modern sign-in method tied to your device's fingerprint, Face ID, PIN, or a hardware security key, instead of a typed password.

To add a passkey:

1. Log in to the account portal.
2. Click the **gear icon** in the top-right corner to open your user settings.
3. Go to the **Credentials** tab.
4. Under **MFA Devices**, select the option to enrol a new device and choose **WebAuthn device**.
5. Follow your browser or device's prompt to create the passkey (fingerprint, Face ID, PIN, or security key), then give the device a recognisable name (e.g. "Work laptop" or "Personal phone").

Repeat this for each device you use to log in. Once a passkey is set up, you can use it to sign in on that device instead of typing your password.

!!! note
    Authentik also supports TOTP (authenticator app) and static recovery tokens as additional MFA options under the same **Credentials** tab, alongside WebAuthn passkeys.

Passkeys apply to the web-based account portal and CloudTAK. Mobile clients (ATAK/TAK Aware) still require a username and password during initial device enrolment — see [Choosing a Client](choosing-a-client.md).

## What you can do in the portal

- **View and edit your profile** — under your user settings (gear icon), the **User details** tab covers your username, display name, email, and locale, plus changing your password
- **Manage credentials** — the **Credentials** tab is where you add MFA devices (including passkeys), manage access tokens, and app passwords
- **View active sessions** — the **Sessions** tab lists every device currently signed in, and lets you sign out a specific session remotely
- **Manage connected accounts** — the **Connected services** tab lists linked social logins (Google, Apple, LinkedIn) and lets you connect or disconnect them
- **Enrol a device** — from the Application Dashboard, select TAK Device Enrollment to generate a QR code or credentials to connect ATAK or TAK Aware (see [Choosing a Client](choosing-a-client.md))
- **See your active channels** — which national, regional, and organisation channels you have access to
- **Request additional access** — if your role changes or you need a channel you don't currently have

## Administrator functions

If you're a team administrator, you'll also see:

- **Pending access requests** — new users from your organisation waiting for approval
- **Team structure** — your organisation's hierarchy of teams and sub-teams
- **Channel management** — creating or approving additional channels for your team

Administrator access and delegated team management are being progressively rolled out as part of TAK.NZ's identity and access management system. If you believe you should have administrator access and don't, contact your central TAK.NZ administrator.

## Need help?

If you're locked out, can't find an expected channel, or aren't sure who your administrator is, reach out through your agency's usual TAK.NZ point of contact, or ask **RELAY** in GeoChat once you have a client set up — see [RELAY Assistant](../reference/relay.md).
