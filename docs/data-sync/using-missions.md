# Using Missions

This page walks through the day-to-day workflow for Missions (Data Sync) — creating one, joining one, adding content, and managing it. The steps below use ATAK terminology since it has the most complete Data Sync interface, but the same concepts apply on TAK Aware, WinTAK, and CloudTAK.

!!! tip "Full reference guide"
    For the complete, illustrated walkthrough of every Data Sync screen and option, download the :material-file-pdf-box: [ATAK Data Sync User Guide (PDF)](../assets/downloads/atak-data-sync-user-guide-5.8.0.pdf).

## Finding available Missions

Open the **Data Sync** tool (in ATAK, this is a plugin available from the toolbar or Additional Tools menu). You'll see the feed list of Missions available on your currently connected TAK Server, with options to:

- Refresh the list
- Create a new Mission
- Switch to timeline view
- Sort by status, update time, or name
- Search by name or hashtag

## Creating a Mission

1. Select **Create New Feed** (Mission).
2. Give it a **Name** — this identifies the Mission to everyone browsing the feed list.
3. Choose the **Server** the Mission will be accessible on (usually your organisation's TAK Server).
4. Configure the optional settings:
    - **Default Role** — the role automatically assigned to anyone who joins (Read-Only, Subscriber, or Owner)
    - **Password** — restrict access to only those who know the password or have been directly invited
    - **Description** — short text shown alongside the Mission name in the feed list
    - **Chatroom** — attach an XMPP chatroom if the TAK Chat plugin is installed
    - **Hashtags** — tags applied to the Mission and everything added to it, making search easier later
5. Select **Done**. The Mission now appears in the feed list for others to find and join.

## Joining an existing Mission

There are two ways to join:

- **From the feed list** — tap the Mission's entry, review its details (creator, last update, subscriber count, default role), then choose:
    - **Download Once** — get the current contents, but don't receive future updates automatically
    - **Download & Sync** — get the current contents and receive live updates as they happen (recommended for active coordination)
- **From a QR code** — select **Add from QR Code** and scan a code from another device already subscribed to the Mission. This is the fastest way to bring a new team member into an active Mission in the field.

If the Mission is password-protected, you'll be prompted to enter the password before you're granted access.

## Adding content to a Mission

Once you've joined a Mission, open its dashboard and select **Add Items**. You can add:

- **Map Select** — tap existing items on the map to add them
- **Overlays** — select items or categories from the Overlay Manager
- **File Select** — attach files or folders from your device
- **User Log** — create a timestamped log entry with text, hashtags, attachments, and linked map items
- **Gallery** — attach a photo from your device
- **Video Alias** — attach a configured video stream
- **Geofence** — attach a shape with a geofence; anyone whose position crosses the boundary can be automatically invited to the Mission
- **Lasso** — draw a lasso around a group of map items to add them all at once
- **Invite** — invite specific users to the Mission directly, even while they're offline (they'll receive the invite next time they connect)

Anything you add while online becomes immediately available to other online Mission members. Anything added while offline syncs automatically once you reconnect.

## Updating items in a Mission

Editing an item that's part of a Mission — moving a marker, changing its details, editing a shape's points — prompts you to publish the change to the Mission. Once published, other subscribed users see the update immediately if they're online, or the next time they reconnect if they're not.

If the same item is edited by two people while one was offline, a **deconfliction prompt** appears for the offline user once they reconnect, letting them choose which version to keep. Changes can be reverted at any time using an item's history.

## Mission status indicators

Downloaded Missions show a status colour on the sync icon:

| Colour | Meaning |
|---|---|
| **Grey** | Downloaded, not checking for updates (Download Once was selected, or you unsubscribed from changes) |
| **Green** | Downloaded and up to date, actively checking for changes |
| **Yellow** | Downloaded but not fully up to date — usually because a large file hasn't finished downloading |
| **Red** | Downloaded and accessible, but you're currently offline |

## Leaving or deleting a Mission

When a Mission is no longer needed, select **Delete** on its feed list entry. Depending on your role, you'll see up to three options:

- **Unsubscribe** — leave the Mission; stop receiving updates, but keep the content already on your device
- **Delete local content** — leave the Mission and remove its content from your device
- **Delete from server** — (Owners only) permanently remove the Mission and its content from the server for everyone

Both confirmation sliders must be moved to the locked position before a deletion is confirmed, to prevent accidental loss of shared content.

## Tips

- Use a clear, specific Mission name tied to the incident or task — avoid generic names that make old Missions hard to distinguish later.
- Set a sensible default role. **Subscriber** is usually right for an active response team; **Read-Only** suits Missions meant for broad situational awareness without edit access.
- Clean up Missions once an incident or exercise concludes, unless the content is meant to be a standing reference.
