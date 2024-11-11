---
title: AtmStrategyClose()
pathName: atmstrategyclose
parent: atm_strategy_methods
section: references
status: imported
---

## Definition

Cancels any working orders and closes any open position of a strategy using the default [ATM strategy close behavior](closing_a_position_or_atm_stra).

## Method Return Value

Returns true if the specified ATM strategy was found; otherwise false.

{% callout type="note" %}

A method return value of true in NO WAY indicates that the strategy in fact is closed. It indicates that the the specified ATM strategy was found and the internal close routine was triggered.
{% /callout %}

## Syntax

AtmStrategyClose(string atmStrategyId)

## Parameters

{% table %}

* atmStrategyId

---

* The unique identifier for the ATM strategy
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Check for valid condition and create an ATM Strategy
     if (GetAtmStrategyUnrealizedProfitLoss("idValue") > 500)
         AtmStrategyClose("idValue");
}
```
