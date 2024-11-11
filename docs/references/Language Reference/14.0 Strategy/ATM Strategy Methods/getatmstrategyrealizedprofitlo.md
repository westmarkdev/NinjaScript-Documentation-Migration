---
title: GetAtmStrategyRealizedProfitLoss()
pathName: getatmstrategyrealizedprofitloss
parent: atm_strategy_methods
section: references
status: imported
---

## Definition

Gets the realized profit and loss value of the specified ATM Strategy.

## Method Return Value

A **double** value representing the realized profit and loss.

## Syntax

**GetAtmStrategyRealizedProfitLoss(string atmStrategyId)**

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
     Print("PnL is " + GetAtmStrategyRealizedProfitLoss("id").ToString());
}
```
