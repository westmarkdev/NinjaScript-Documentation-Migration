---
section: references
title: Splits
pathName: splits
parent: masterinstrument
status: review
---

## Definition

Indicates the Splits that have been configured for the **Master Instrument properties** used in for stocks.

## Property Value

A collection of Splits configured for the current instrument.

Possible values are:

{% table %}

* Date
* Factor

---

* A DateTime structure representing the date of the split
* A **double** value representing the number of points the stock split
{% /table %}

## Syntax

**Bars.Instrument.MasterInstrument.Splits**

## Examples

```csharp
 foreach (Split split in Bars.Instrument.MasterInstrument.Splits)
{
     Print(split.Date);
     Print(split.Factor);
}
```
