---
title: GetAtmStrategyPositionAveragePrice()
pathName: getatmstrategypositionaverageprice
parent: atm_strategy_methods
section: references
status: imported
---

## Definition

Gets the current position's average price of the specified ATM Strategy.

{% callout type="note" %}

Changes to positions will not be reflected till at least the next **OnBarUpdate()** event after an order fill.

{% /callout %}

## Method Return Value

A **double** value representing the average price.

## Syntax

**GetAtmStrategyPositionAveragePrice(string atmStrategyId)**

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
     if (GetAtmStrategyMarketPosition("id") != MarketPosition.Flat)
         Print("Average price is " + GetAtmStrategyPositionAveragePrice("id").ToString());
}
```
