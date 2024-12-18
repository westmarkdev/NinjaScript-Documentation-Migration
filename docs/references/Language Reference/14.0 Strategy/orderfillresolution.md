---
title: OrderFillResolution
pathName: orderfillresolution
parent: strategy
section: references
status: review
---

## Definition

Determines how strategy orders are filled during historical states.

Please see [Understanding Historical Fill Processing](understanding_historical_fill_) for general information on historical fill processing.

## Property Value

An enum value that determines how the strategy orders are filled. Default value is set to **OrderFillResolution.Standard**. Possible values are:

* **OrderFillResolution.Standard**  | Faster - Uses the existing bar type and interval that you are running the backtest on to fill your orders.
* **OrderFillResolution.High** | More granular - Allows you to set a secondary bar series to be used as the price data to fill your orders. (See also [OrderFillResolutionType](orderfillresolutiontype) and [OrderFillResolutionValue](orderfillresolutionvalue))
{% /table %}

## Syntax

**OrderFillResolution**

{% callout type="warning" %}

* Warning: This property should ONLY be set from the [OnStateChange()](onstatechange) method during State.SetDefaults
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
