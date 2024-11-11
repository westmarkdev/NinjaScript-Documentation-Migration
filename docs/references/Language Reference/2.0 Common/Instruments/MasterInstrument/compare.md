---
title: Compare()
pathName: compare
parent: masterinstrument
section: references
status: review
---

## Definition

Compares two price values with respect to the Instrument **TickSize** to ensure accuracy when dealing with floating point math.

## Method Return Value

An **int** value.

* A value of "1" is returned if price1 is greater than price2.
* A value of "-1" is returned if price1 is less than price2.
* A value of "0" if price1 is equal to price2.

## Syntax

**Instrument.MasterInstrument.Compare(double price1, double price2)**

## Parameters

{% table %}

---

* price1
* A **double** value representing a price.

---

* price2
* A **double** value representing a price.
{% /table %}

## Examples

```csharp
double newPrice = Close[0] + High[0] + Open[0];
if (Instrument.MasterInstrument.Compare(newPrice, Close[1]) == 1)
     // Do something since price1 is greater than price2

```
