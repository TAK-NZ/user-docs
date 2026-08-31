---
description: How to manage members, sub-teams, devices, and channels as a team admin in TAK Team Manager.
---

# Team Administration

This page is for **team admins** — members who additionally manage a team, or a whole organisation and its sub-teams — in **TAK Team Manager** at [https://team.tak.nz/](https://team.tak.nz/). If you're looking for general account help instead, see [Account Management](account-management.md).

You become a team admin either by being promoted by another admin, or by being an admin of an ancestor team above yours in the hierarchy — admin rights flow downward through sub-teams automatically.

## Finding your team

The **Orgs & Teams** page (`/teams`) lists every organisation and team you belong to, with quick counts for Members, Team Devices, Team Admins, and Sub-teams — click any of those counts to jump straight to that tab on the team's own page.

## Adding members

From your team's page, click **Add Member**. You have two options:

- **Create New User** — for someone brand new. Fill in their email, first and last name, and (depending on your organisation's settings) a callsign suffix. Their account and TAK credentials are created right away.
- **Add Existing User** — for someone who already has an account elsewhere and needs to join your team. You'll also get a chance to review and correct their name and callsign suffix before adding them.

## Managing members

Your team's **Members** tab lists everyone on the team. Each row has a set of actions:

- **Edit** — correct their name, TAK role, or callsign suffix.
- **Resend welcome email** — if someone missed or lost their original welcome email, this sends it again. You'll be asked to confirm before it sends.
- **Transfer** — move this member to a different team.
- **View Devices** — see the TAK devices this member has enrolled, and revoke one on their behalf if needed.
- **Delete** — the one genuinely irreversible action here: it permanently removes their account everywhere, including from Authentik. You'll need to type their email address to confirm before it happens. Use this only when someone is truly leaving for good, not as a way to remove them from just your team — use **Transfer** for that.

## Managing team admins

The **Team Admins** tab shows everyone with admin rights on your team. The only action here is **Remove as admin** — this takes away their admin rights but leaves their account and team membership completely untouched; they simply become a regular member again. You'll be asked to confirm first. To make someone an admin, use **Add Admin** from your team page's menu (this promotes an existing member).

## Managing team devices

The **Team Devices** tab is for devices that belong to the team itself rather than to any one person — a shared tablet or a vehicle-mounted radio, for example. From here you can enrol a new team device (the same QR-code flow described in [Choosing a Client](choosing-a-client.md), just bound to the team rather than to an individual) or revoke an existing one's certificate.

## Managing channels

The **Channels** tab shows your team's TAK channels — its primary channel plus any custom ones — along with each channel's sync status and member count. You can create a new channel from your team's menu, up to 3 per team. See [Channel Structure](../concepts/channels.md) for how TAK.NZ's national, regional, and organisation channels fit together.

## Managing sub-teams

The **Sub-teams** tab lists any teams nested underneath yours. You can create a new sub-team from here (there's a maximum nesting depth, so the option disables itself once you've reached it), or delete an existing sub-team.

## Reviewing access requests

If people have requested to join your team, the **Requests** page (`/requests`, visible to any team admin) shows them as cards:

- **New account requests** show the person's email, requested team, submission date, and their stated reason for requesting access. You can adjust their name and callsign suffix before approving. Click **Approve** to let them in, or **Deny** (you'll be asked to give a written reason, which gets emailed to them).
- **Transfer requests** show a member moving from one team to another, who requested it, and a note that approving it will remove their admin rights on their old team if they had any.

## Notifications your members might receive

- **Email verification** — when they first request access, confirming their email address.
- **Welcome/approval email** — sent once their access request is approved, with their account details.
- **Denial email** — sent if their request is denied, including your stated reason.
- **Resend welcome email** — you can trigger this again if they missed the original.

## Related

- [Account Management](account-management.md) — general account features available to every member
- [Channel Structure](../concepts/channels.md) — how channels are structured across TAK.NZ
