---
title: OrderFillResolutionValue
pathName: orderfillresolutionvalue
parent: strategy
section: references
status: imported
---

## Definition

Determines the bars period interval value which will be used for historical fill processing.

{% callout type="note" %}

This property will only be valid if the **OrderFillResolution** is set to [OrderFillResolution.High](orderfillresolution.htm).

{% /callout %}

## Property Value

A int representing the interval used for the bars period during historical order processing. Default value is set to 1.

## Syntax

**OrderFillResolutionValue**

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults.

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
