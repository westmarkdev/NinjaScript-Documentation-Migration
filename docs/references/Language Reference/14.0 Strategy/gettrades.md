---
title: GetTrades()
pathName: gettrades
parent: strategy
section: references
status: imported
---

## Definition

Returns a **TradeCollection** object representing all trades that make up the specified position.

## Method Return Value

A **TradeCollection** object.

## Syntax

**<`tradecollection`>.GetTrades(string instrument, string entrySignalName, int instance)**

## Parameters

{% table %}

---

* **instrument**
* An instrument name such as "MSFT"

---

* **entrySignalName**
* The name of your entry signal

---

* **instance**
* The occurrence to check for (1 is the most recent, 2 is the 2nd most recent position, etc...)
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     TradeCollection myTrades = SystemPerformance.AllTrades.GetTrades("MSFT", "myEntrySignal", 1);
     Print("The last position was comprised of " + myTrades.Count + " trades.");
}
```
