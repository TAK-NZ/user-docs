# Data Packages

A **Data Package** is a portable bundle of content — map markers, overlays, routes, imagery, or configuration — packaged into a single file that can be shared, downloaded, and imported into a TAK client. Where [Missions](../data-sync/index.md) keep content live and synced over the network, Data Packages are a way to move a fixed snapshot of content between devices, including onto devices that are offline.

## What can be in a Data Package

A Data Package can contain a mix of:

- Map markers, drawings, and routes
- Overlay files (e.g. hazard boundaries, staging areas, pre-planned search sectors)
- Imagery and reference files
- Client configuration, such as server connection details or preference sets

Because a Data Package is just a file, it can be sent by any normal means — email, USB drive, file share, QR code, or a link — and then imported directly into ATAK, TAK Aware, WinTAK, or CloudTAK.

## Data Packages vs. Missions

| | Data Package | Mission |
|---|---|---|
| Content stays in sync automatically | No | Yes |
| Works fully offline | Yes | No (needs a server connection to sync) |
| Best for | A fixed set of content to distribute once | Ongoing, live collaboration |
| Typical use | Pre-loading a device before deployment | Coordinating an active incident |

In practice, the two are often used together: a Data Package might be used to pre-load a device with reference overlays before an operation starts, while a Mission is used to coordinate live updates once the operation is underway.

## Typical use cases

- **Pre-deployment setup** — bundling connection settings and reference overlays so a new device is ready to go without manual configuration
- **Sharing a pre-plan** — distributing a search sector plan, staging area layout, or hazard assessment to every team ahead of an operation
- **Working offline** — getting map content onto a device that won't have connectivity in the field, since importing a Data Package doesn't require a live server connection

## Importing a Data Package

The exact steps vary slightly by client. In general:

1. Obtain the Data Package file (from a colleague, your TAK.NZ administrator, or a shared link/QR code)
2. Open it with your TAK client, or use the client's import/Data Package menu to select the file
3. Review what's included before confirming the import — a Data Package can add overlays, markers, and settings to your client
4. Once imported, the content behaves like anything else on your map — it can be viewed, hidden, or removed like other overlays

See your specific client's guide — [CloudTAK](../clients/cloudtak.md), [ATAK](../clients/atak.md), [TAK Aware](../clients/takaware.md), or [WinTAK](../clients/wintak.md) — for exact menu locations.

## A note on trust

Only import a Data Package from a source you trust. Because a Data Package can include configuration such as server connection details, importing one from an unknown source could reconfigure your client to point at a server you didn't intend. If you're unsure where a Data Package came from, check with your TAK.NZ administrator before importing it.
