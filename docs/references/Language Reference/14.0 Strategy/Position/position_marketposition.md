---
title: MarketPosition
pathName: marketposition
parent: position
section: references
status: imported
---

## Definition

Gets the strategy's current market position

## Property Value

* **MarketPosition.Flat**
* **MarketPosition.Long**
* **MarketPosition.Short**

## Syntax

**Position.MarketPosition**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // If not flat print our open PnL
     if (Position.MarketPosition != MarketPosition.Flat)
         Print("Open PnL: " + Position.GetUnrealizedProfitLoss(PerformanceUnit.Points, Close[0]));
}
```
