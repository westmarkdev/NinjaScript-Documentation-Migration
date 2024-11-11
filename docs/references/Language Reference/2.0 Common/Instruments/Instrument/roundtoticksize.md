---
section: references
title: RoundToTickSize()
pathName: roundtoticksize
parent: instrument
status: review
---

## Definition

Returns a value that is rounded up to the nearest valid value evenly divisible by the instrument's tick size.

## Method Return Value

A **double** value.

## Syntax

**Instrument.MasterInstrument.RoundToTickSize(double price)**

## Parameters

{% table %}

* Parameter
* Description

---

* **price**
* A **double** value representing a price
{% /table %}

## Examples

```csharp
//Takes the last 3 closes, divides them by 3, and rounds the value up to the nearest valid tick size
Value[0] = Instrument.MasterInstrument.RoundToTickSize((Close[0] + Close[1] + Close[2]) / 3);
```
