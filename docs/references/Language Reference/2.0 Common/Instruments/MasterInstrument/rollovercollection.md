---
title: RolloverCollection
pathName: rollovercollection
parent: masterinstrument
section: references
status: review
---

## Definition

Indicates the rollovers that have been configured for the **Master Instrument properties** used in for futures.

## Property Value

A **RolloversCollection** configured for the current instrument.

Possible values are:

{% table %}

* Parameter

* Description

---

* ContractMonth

* A DateTime structure representing the expiry month of a futures contract

---

* Date

* A DateTime structure representing the date of the rollover

---

* Offset

* A double value representing the number of points between contracts

---

{% /table %}

## Syntax

**Bars.Instrument.MasterInstrument.RolloverCollection**

## Examples

```csharp
foreach(var rollover in Bars.Instrument.MasterInstrument.RolloverCollection)
{
     Print(rollover.ContractMonth);
     Print(rollover.Date);
     Print(rollover.Offset);
}
```
