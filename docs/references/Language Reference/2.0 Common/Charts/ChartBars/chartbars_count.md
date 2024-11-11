---
title: Count
pathName: count
parent: chartbars
section: references
status: review
---

## Definition

The total number of **ChartBars** in the charts primary data series.

## Property Value

An **int** value representing the total number of bars.

## Syntax

**ChartBars.Count**

## Examples

```csharp

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if(ChartBars != null)
   {
     Print("ChartBars contain " + ChartBars.Count + " bars");
     //Output:  ChartBars contain 73 bars
   }
}

```
