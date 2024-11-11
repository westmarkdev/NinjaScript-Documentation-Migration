---
title: BarWidthArray
pathName: barwidtharray
parent: chartcontrol
section: references
status: review
---

## Definition

An array containing the values of the [BarWidth](chartcontrol_barwidth) properties of all Bars objects applied to the chart.

## Property Value

An array of double variables containing the values of the BarWidth properties of Bars objects on the chart.

## Syntax

**ChartControl.BarWidthArray[]**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Assign BarWidthArray to a new array
   double[] barWidths = chartControl.BarWidthArray;
 
   double referenceWidth = barWidths[0];
 
   // Trigger an alert if bar widths on the chart differ
   foreach (double width in barWidths)
   {
       if (width != referenceWidth)
           Alert("mismatchWidths", Priority.Low, "Bar widths on the chart do not match!", " ", 20, Brushes.White, Brushes.Black);
   }
}
```
