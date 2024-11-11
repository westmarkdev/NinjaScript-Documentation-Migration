---
title: GetNextExpiry()
pathName: getnextexpiry
parent: masterinstrument
section: references
status: review
---

## Definition

Returns the current futures expiry compared to the time of the input value used for the method.

## Method Return Value

A **DateTime** structure

## Syntax

**Bars.Instrument.MasterInstrument.GetNextExpiry(DateTime afterDate)**

## Parameters

{% table %}

---

* **afterDate**
* A **DateTime** value representing to be compared
{% /table %}

## Examples

```csharp
// Indicates what the current expiry is in the bottom right of the chart
Draw.TextFixed(this, "tag1", "The current expiry is " + Bars.Instrument.MasterInstrument.GetNextExpiry(DateTime.Now).ToString("MM-yy"), TextPosition.BottomRight);
```
