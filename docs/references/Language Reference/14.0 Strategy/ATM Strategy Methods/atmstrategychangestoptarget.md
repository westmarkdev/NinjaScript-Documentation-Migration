---
title: AtmStrategyChangeStopTarget()
pathName: atmstrategychangestoptarget
parent: atm_strategy_methods
section: references
status: imported
---

## Definition

Changes the price of the specified order of the specified ATM strategy.

## Method Return Value

Returns true if the specified order was found; otherwise false.

## Syntax

**AtmStrategyChangeStopTarget(double limitPrice, double stopPrice, string orderName, string atmStrategyId)**

## Parameters

{% table %}

* limitPrice
* Order limit price

---

* stopPrice
* Order stop price

---

* orderName
* The order name such as "Stop1" or "Target2"

---

* atmStrategyId
* The unique identifier for the ATM strategy
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     AtmStrategyChangeStopTarget(0, SMA(10)[0], "Stop1", "AtmIdValue");
}
```
