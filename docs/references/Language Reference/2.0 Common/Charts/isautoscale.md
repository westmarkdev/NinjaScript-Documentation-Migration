---
title: IsAutoScale
pathName: isautoscale
parent: charts
section: references
status: review
---

## Definition

If true, the object will call **CalculateMinMax()** in order to determine the object's **MinValue** and **MaxValue** value used to scale the Y-axis of the chart.

## Property Value

This property returns true if the object's are included in the y-scale; otherwise, false. Default set to false for **DrawingTools**, but set to true for **Indicators**.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults or State.Configure.

{% /callout %}

## Syntax

**IsAutoScale**

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {         
     Name                 = "Example Indicator";         
     // set this to true to call CalculateMinMix() to ensure drawing tool is fully rendered in chart scale
     IsAutoScale = true;  
   }
   else if (State == State.Configure)
   {
   }
}
```
