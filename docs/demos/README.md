# Algeria hotel demo scenarios

Four fictional Algerian properties, used to exercise ZIRI PMS end to end with
DZD rates, Algerian taxes, French dates and realistic front-desk work. Each
scenario has five genuine screenshots taken from the isolated staging
deployment on **27 October 2026**.

| Scenario | City | Profile | What it demonstrates |
|---|---|---|---|
| [Hôtel El Bahdja](hotel-el-bahdja.md) | Alger | Four-star waterfront city hotel, 6 demo rooms | City-hotel arrivals, OTA/phone/walk-in mix, partial and closed folios |
| [Dar Cirta Boutique Hotel](dar-cirta.md) | Constantine | Boutique maison above the Rhumel gorges, 6 demo rooms | High-rate, low-count inventory; suite-led revenue; dirty-room arrival |
| [Hôtel Cap Gouraya](hotel-cap-gouraya.md) | Béjaïa | Family beach hotel at Aiguades, 6 demo rooms | Family suite and bungalow inventory; highest revenue of the set |
| [Maison du M'Zab](maison-du-mzab.md) | Ghardaïa | Courtyard guesthouse near Beni Isguen, 6 demo rooms | Small leisure property; low base rate; roof-terrace room |

## What every scenario contains

- **A real day at the front desk** — arrivals, in-house guests, room board,
  occupancy percentage, posted revenue, RevPAR and open housekeeping tasks.
- **Eight reservations** per property spanning Confirmed, Checked In, Checked
  Out, Cancelled and No Show.
- **Three folios** — two open with partial payments, one closed with a GST
  invoice number.
- **Three open housekeeping tasks** plus a completed checkout clean.
- **Five screenshots** — Today, Reservations, Tape Chart, Rooms and Billing.

The screenshots are the application's own UI. They were not mocked up,
redrawn or assembled from parts: each one is a viewport capture of the staging
SPA after the page had loaded its data.

## Data provenance

All guest names, phone numbers, email addresses, reservation references,
payments and invoice numbers are synthetic. Email domains use the reserved
`.example` TLD. No production database, guest record or payment was read,
copied or modified.

The four properties share one isolated staging database and were seeded with a
repeatable script (idempotent per record). The pre-existing staging property
was preserved. Screenshots were captured as the seeded staging administrator;
the `Demo Admin` label in the header is the account, not a real person.

The production deployment was not used for any screenshot, and its containers
were not restarted or reconfigured.

## Reproducing the demo data

The four properties, their room types, rooms, guests, reservations, folios and
housekeeping tasks were created with
[`kamra/scripts/seed_algeria_demos.py`](../../kamra/scripts/seed_algeria_demos.py),
which is idempotent per record. It refuses to run unless explicitly confirmed,
so a mistyped site name cannot add demo records to a live hotel:

```bash
bench --site staging.kamra.local execute kamra.scripts.seed_algeria_demos.run \
  --kwargs '{"confirm": "SEED_SYNTHETIC_DEMO_DATA"}'
```

Use it only against an isolated staging site. It does not delete anything; the
pre-existing staging property is left untouched.

## Reading order

Start with [Hôtel El Bahdja](hotel-el-bahdja.md) for the fullest city-hotel
story, then compare the boutique, beach and guesthouse variants. The
[repository documentation index](../README.md) lists the rest of the in-repo
guides.
