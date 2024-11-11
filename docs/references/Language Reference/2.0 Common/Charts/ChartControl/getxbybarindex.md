---
title: GetXByBarIndex()
pathName: getxbybarindex
parent: chartcontrol
section: references
status: review
---

## Definition

Returns the chart-canvas x-coordinate of the bar at a specified index of a specified **ChartBars** object on the chart.

{% callout type="note" %}

Since the index is based upon bars that move across the chart canvas as new bars are painted, the value returned by **GetXByBarIndex()** can be expected to change as new bars are painted on the chart, or as the chart is scrolled backward or forward on the x-axis.

{% /callout %}

## Method Return Value

An int representing a chart-canvas x-coordinate.

## Syntax

**<`chartcontrol`>.GetXByBarIndex(ChartBars chartBars, int barIndex)**

## Method Parameters

{% table %}

* **Parameter**
* **Description**

---

* **chartBars**
* The **ChartBars** object to check.

---

* **barIndex**
* The slot index used to determine an x-coordinate.
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    double xCoordinate = chartControl.GetXByBarIndex(ChartBars, 100);
    
    // Print the x-coordinate value
    Print(xCoordinate);
}
```
