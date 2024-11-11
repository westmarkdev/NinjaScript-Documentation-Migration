---
section: references
title: RoundDownToTickSize()
pathName: rounddowntoticksize
parent: instrument
status: review
---

## Definition

Returns a value that is rounded down to the nearest valid value evenly divisible by the instrument's tick size.

## Method Return Value

A **double** value.

## Syntax

**Instrument.MasterInstrument.RoundDownToTickSize(double price)**

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
//Takes the last 3 closes, divides them by 3, and rounds the value down to the nearest valid tick size**
Value[0] = Instrument.MasterInstrument.RoundDownToTickSize((Close[0] + Close[1] + Close[2]) / 3);
```
