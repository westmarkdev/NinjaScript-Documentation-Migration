---
title: "OrderFillResolution"
pathName: /docs/desktop/orderfillresolution
---

## Definition

Determines how strategy orders are filled during historical states.  

Please see [Understanding Historical Fill Processing](/docs/desktop/understanding_historical_fill_) for general information on historical fill processing.

## Property Value

An enum value that determines how the strategy orders are filled.  Default value is set to `OrderFillResolution.Standard`.  Possible values are:

|  |  |
| --- | --- |
| OrderFillResolution.Standard  | Faster - Uses the existing bar type and interval that you are running the backtest on to fill your orders.   |
| OrderFillResolution.High | More granular - Allows you to set a secondary bar series to be used as the price data to fill your orders.   (See also [OrderFillResolutionType](/docs/desktop/orderfillresolutiontype) and [OrderFillResolutionValue](/docs/desktop/orderfillresolutionvalue)) |

## Syntax

```csharp
## OrderFillResolution
```

{% callout type="warning" %}
This property should ONLY be set from the [OnStateChange()](/docs/desktop/onstatechange) method during State.SetDefaults
{% /callout %}

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "ExampleStrategy";
        OrderFillResolution = OrderFillResolution.Standard;
    }
}
```
