---
title: BarsRequiredToPlot
pathName: barsrequiredtoplot
parent: indicator
section: references
status: imported
---

## Definition

The number of bars on a chart required before the script plots. By default, the value is 20 bars.

{% callout type="note" %}

This property is NOT the same as a minimum number of bars required to calculate the script values.  OnBarUpdate will always start calculating for the first bar on the chart (CurrentBar 0)

{% /callout %}

## Property Value

An **int** value that represents the minimum number of bars required.

## Syntax

**BarsRequiredToPlot**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          BarsRequiredToPlot = 10; // Do not plot until the 11th bar on the chart
          AddPlot(Brushes.Orange, "SMA");
     }     
}
```
