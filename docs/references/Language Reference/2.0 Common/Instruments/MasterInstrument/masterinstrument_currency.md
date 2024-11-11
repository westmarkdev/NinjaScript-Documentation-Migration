---
title: Currency
pathName: currency
parent: masterinstrument
section: references
status: review
---

## Definition

Indicates the currency configured for the **Master Instrument properties**.

## Property Value

A type of Currency which is configured for the current master instrument.

## Syntax

**Bars.Instrument.MasterInstrument.Currency**

## Examples

```csharp
if (Bars.Instrument.MasterInstrument.Currency != Currency.UsDollar)
{
    //Prints if the currency is not UsDollar and indicates what currency it is
    Print ("Warning: Instruments base currency is not UsDollar, it is " + Bars.Instrument.MasterInstrument.Currency);
}
```
