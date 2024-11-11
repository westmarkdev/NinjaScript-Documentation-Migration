---
status: double_check
pathName: volumeseries
title: VolumeSeries<double>
parent: iseriest
section: references
lg2m: true
---

## Definition

Represents historical volume data as ISeries<`double`> interface which can be used for custom NinjaScript object calculations

{% callout type="note" %}

In most cases, you will access the historical volume series using a core event handler such as OnBarUpdate.  For more advance developers, you may find situations where you wish to access historical volume series outside of the core event methods, such as your own custom mouse click.  In these advanced scenarios, you may run into situations where the barsAgo pointer is not in sync with the current bar, which may cause errors when trying to obtain this information.  In those cases, use the Bars.Get...() methods with the absolute bar index, e.g., [Bars.GetVolume()](getvolume).

{ /callout }

## Single ISeries<`double`>

{% table %}

* Property

* Description

---

* [Volume](source_files/iseries_volume.md)

* A collection of historical bar volume values.

---

{% /table %}

## Multi-Time Frame ISeries<`double`>

{% table %}

* Property

* Description

---

* [Volumes](source_files/iseries_volumes.md)

* Holds an array of ISeries<`double`> objects holding historical bar volume.

---

{% /table %}
