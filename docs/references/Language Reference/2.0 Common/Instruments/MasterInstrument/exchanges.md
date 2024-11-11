---
title: Exchanges
pathName: exchanges
parent: masterinstrument
section: references
status: review
---

## Definition

A collection of exchange(s) configured for the **Master Instrument properties**.

## Property Value

A collection of Exchanges which represent the exchanges configured for the current instrument.

## Syntax

**Bars.Instrument.MasterInstrument.Exchanges**

## Examples

```csharp
foreach(Exchange exchange in Bars.Instrument.MasterInstrument.Exchanges)
{
 Print(exchange); // Default, Nasdaq, NYSE
}
```
