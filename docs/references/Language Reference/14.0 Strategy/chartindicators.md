---
title: ChartIndicators
pathName: chartindicators
parent: strategy
section: references
status: imported
---

## Definition

Contains a collection of Indicators which have been added to the strategy instance using **AddChartIndicator()**.

## Property Value

An **Indicator** object

## Syntax

**ChartIndicators[int index]**

## Examples

```csharp
if (State == State.DataLoaded)
{
   AddChartIndicator(SMA(20));
   
   // Set the plots color for the added indicator 
   ChartIndicators[0].Plots[0].Brush = Brushes.Blue;
   
   // Set the added indicator to panel 1 (specified index needs to be >= 1)
   ChartIndicators[0].Panel = 1;
}
```
