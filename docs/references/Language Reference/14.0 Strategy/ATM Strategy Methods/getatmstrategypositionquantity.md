---
title: GetAtmStrategyPositionQuantity()
pathName: getatmstrategypositionquantity
parent: atm_strategy_methods
section: references
status: review
---

## Definition

Gets the current position quantity of the specified ATM Strategy.

{% callout type="note" %}

Changes to positions will not be reflected till at least the next **OnBarUpdate()** event after an order fill.

{% /callout %}

## Method Return Value

An **int** value representing the quantity.

## Syntax

**GetAtmStrategyPositionQuantity(string atmStrategyId)**

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
     // Check if flat
     if (GetAtmStrategyMarketPosition("idValue") != MarketPosition.Flat)
         Print("Position size is " + GetAtmStrategyPositionQuantity("idValue").ToString());
}
```
