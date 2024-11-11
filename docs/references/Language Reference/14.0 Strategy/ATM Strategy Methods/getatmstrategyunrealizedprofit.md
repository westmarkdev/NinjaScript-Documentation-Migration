---
title: GetAtmStrategyUnrealizedProfitLoss()
pathName: getatmstrategyunrealizedprofitloss
parent: atm_strategy_methods
section: references
status: imported
---

## Definition

Gets the unrealized profit and loss value of the specified ATM Strategy.

## Method Return Value

A **double** value representing the unrealized profit and loss.

## Syntax

**GetAtmStrategyUnrealizedProfitLoss(string atmStrategyId)**

## Parameters

{% table %}

---

* **atmStrategyId**
* The unique identifier for the ATM strategy
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     Print("Unrealized PnL is " + GetAtmStrategyUnrealizedProfitLoss("id").ToString());
}
```
