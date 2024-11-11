---
section: references
title: TickSize
pathName: ticksize
parent: analytical
status: review
---

## Definition

The minimum fluctuation value which is always a value of 1-tick for the corresponding master instrument.

## Property Value

A **double** value that represents the minimum fluctuation of an instrument.

## Syntax

**TickSize**

## Warning

{% callout type="note" %}

This property should NOT be accessed during State.SetDefaults from within the **OnStateChange()** method, all bars series would be guaranteed to have loaded in **State.DataLoaded**.

{% /callout %}

## Examples

```csharp
// Prints the ticksize to the output window
Print("The ticksize of this instrument is " + TickSize);
// Prints the value of the current bar low less one tick size
double value = Low[0] - TickSize;
Print(value);
```
