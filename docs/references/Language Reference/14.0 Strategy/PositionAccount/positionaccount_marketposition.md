---
title: MarketPosition
pathName: marketposition
parent: positionaccount
section: references
status: imported
---

## Definition

Gets the account's current market position

## Property Value

* **MarketPosition.Flat**
* **MarketPosition.Long**
* **MarketPosition.Short**

## Syntax

**PositionAccount.MarketPosition**

## Examples

```csharp
protected override void OnBarUpdate()
{ 
    // If not flat print our open PnL
    if (PositionAccount.MarketPosition != MarketPosition.Flat) 
        Print("Open PnL: " + PositionAccount.GetUnrealizedProfitLoss(PerformanceUnit.Points, Close[0]));
}
```
