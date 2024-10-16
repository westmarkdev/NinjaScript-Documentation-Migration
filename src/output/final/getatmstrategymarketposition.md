---
title: "GetAtmStrategyMarketPosition()"
pathName: /docs/desktop/getatmstrategymarketposition
---

## Definition

Gets the current market position of the specified ATM Strategy.

{% callout type="note" %}

1. Changes to positions will not be reflected till at least the next [OnBarUpdate()](/docs/desktop/onbarupdate) event after an order fill.
2. If the ATM Strategy does not exist then MarketPosition.Flat returns.
3. Please note this provides access to the current ATM strategy position, which should not be confused with the NinjaScript strategy position or account position. For more information please see the [Using ATM Strategies](/docs/desktop/using_atm_strategies) section.
{% /callout %}

## Method Return Value

- `MarketPosition.Flat`
- `MarketPosition.Long`
- `MarketPosition.Short`

## Syntax

```csharp
GetAtmStrategyMarketPosition(string atmStrategyId)
```

## Parameters

|  |  |
| --- | --- |
| atmStrategyId | The unique identifier for the ATM strategy |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Check if flat
    if (GetAtmStrategyMarketPosition("id") == MarketPosition.Flat)
        Print("ATM Strategy position is currently flat");
}
```
