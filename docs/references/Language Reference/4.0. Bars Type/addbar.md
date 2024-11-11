---
title: AddBar()
pathName: addbar
parent: bars_type
status: imported
order: 0
section: references
---

## Definition

Adds new data points for the Bars Type.

## Syntax

**AddBar**(Bars bars, double open, double high, double low, double close, DateTime time, long volume)
**AddBar**(Bars bars, double open, double high, double low, double close, DateTime time, long volume, double bid, double ask)

## Parameters

{% table %}

* bars
* The Bars object of your bars type

---

* open
* A **double** value representing the open price

---

* high
* A **double** value representing the high price

---

* low
* A **double** value representing the low price

---

* close
* A **double** value representing the close price

---

* time
* A DateTime value representing the time

---

* volume
* A long value representing the volume

---

* bid
* A **double** value representing the bid price

---

* ask
* A **double** value representing the ask price
{% /table %}

## Examples

```csharp
AddBar(bars, open, high, low, close, time, (long)Math.Min(volumeTmp, bars.BarsPeriod.Value));
```
