---
title: Dividends
pathName: dividends
parent: masterinstrument
section: references
status: review
---

## Definition

An collection of Dividends configured for the **Master Instrument properties** used in for stocks.

## Property Value

A collection of Dividends configured for the current instrument.

Possible values are:

{% table %}

* Amount
* Date

---

* A **double** value representing the amount in dollars which was paid on the date of the dividend
* A DateTime structure representing the date of the dividend
{% /table %}

## Syntax

**Bars.Instrument.MasterInstrument.Dividends**

## Examples

```csharp
foreach(Dividend dividends in Bars.Instrument.MasterInstrument.Dividends)
{
   Print(dividends.Amount);
   Print(dividends.Date);
}
```
