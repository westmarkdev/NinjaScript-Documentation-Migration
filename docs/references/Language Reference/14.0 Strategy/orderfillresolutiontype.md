---
title: OrderFillResolutionType
pathName: orderfillresolutiontype
parent: strategy
section: references
status: imported
---

## Definition

Determines the bars type which will be used for historical fill processing.

{% callout type="note" %}

This property will only be valid if the **OrderFillResolution** is set to **OrderFillResolution.High**.

{% /callout %}

## Property Value

A **BarsPeriodType** representing the type of bars during historical order processing. Default value is set to **BarsPeriodType.Minute**.

## Syntax

**OrderFillResolutionType**

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults**.

{% /callout %}

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {                
        Name = "ExampleStrategy";

        // use one second bars for filling orders
        OrderFillResolution       = OrderFillResolution.High;                 
        OrderFillResolutionType   = BarsPeriodType.Second;
        OrderFillResolutionValue   = 1; 
    }
}
```
