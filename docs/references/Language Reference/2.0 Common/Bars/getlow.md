---
title: GetLow()
pathName: getlow
parent: bars
section: references
status: review
---

## Definition

Returns the low price at the selected bar index value.

## Method Return Value

A **double** value that represents the low price at the desired bar index.

## Syntax

**Bars.GetLow**(int index)

## Parameters

{% table %}

---

* **index**
* An int representing an absolute bar index value
{% /table %}

## Examples

```csharp

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
   // loop through only the rendered bars on the chart
   for(int barIndex = ChartBars.FromIndex; barIndex <= ChartBars.ToIndex; barIndex++)
   {
     // get the low price at the selected bar index value
     double lowPrice = Bars.GetLow(barIndex);
     Print("Bar #" + barIndex + " low price is " + lowPrice);
   }
}
```
