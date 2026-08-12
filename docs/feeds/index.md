# External Feeds

TAK.NZ isn't limited to positions reported by people running a TAK client. **External feeds** bring in live data from outside sources — sensors, public data services, and third-party systems — and display it on the Common Operating Picture alongside your team's own positions.

## How feeds work

Every external feed is converted into the same Cursor on Target (CoT) format used by every other item on the map (see [What is TAK?](../concepts/index.md#cursor-on-target-cot)). This means an aircraft tracked via ADS-B, a vessel tracked via AIS, or a future feed type all appear on your map exactly like any other marker — with a position, an icon, and a Remarks field you can click for more detail. You don't need any special client feature to view a feed; if it's enabled on a channel you're subscribed to, it just appears.

Feeds are enabled per-deployment by your TAK.NZ administrator and typically appear as their own overlay category or dedicated channel, so you can turn a feed on or off independently of your other channels.

## Available feeds

<div class="grid cards" markdown>

- :material-airplane:{ .lg .middle } **ADS-B (Aircraft)**

    ---

    Live aircraft positions from ADS-B transponder data, including automatic identification of firefighting aircraft.

    [:octicons-arrow-right-24: ADS-B feed](adsb.md)

- :material-ferry:{ .lg .middle } **AIS (Vessels)**

    ---

    Live vessel positions from Automatic Identification System (AIS) data in and around New Zealand waters.

    [:octicons-arrow-right-24: AIS feed](ais.md)

</div>

More feeds are planned as TAK.NZ's ecosystem grows — this page will be updated as new feed types come online.

## Why this matters for public safety

External feeds extend the Common Operating Picture beyond what any single agency can generate on its own. During a wildfire, ADS-B lets everyone on the incident see firefighting aircraft in the air alongside ground crews, without needing a separate air traffic display. During a maritime search or a weather event, AIS gives visibility of vessels in the area, useful for both safety and coordination.

Because these feeds appear using the same map, the same channels, and the same interaction model as everything else in TAK.NZ, there's no separate tool to learn — they're just more dots on the map you're already using.
