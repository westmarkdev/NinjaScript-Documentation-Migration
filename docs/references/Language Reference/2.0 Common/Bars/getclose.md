---
title: GetClose()
pathName: getclose
parent: bars
section: references
status: review
---

## Definition

Returns the closing price at the current bar index value.

## Method Return Value

A **double** value that represents the close price at the desired bar index.

## Syntax

**Bars.GetClose(int index)**

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
   for(int barIndex = ChartBars.FromIndex; barIndex &lt;= ChartBars.ToIndex; barIndex++)
   {
     // get the close price at the selected bar index value
     double closePrice = Bars.GetClose(barIndex);
     Print("Bar #" + barIndex + " closing price is " + closePrice);
   }
}

```
