---
title: GetBarIdxByX()
pathName: getbaridxbyx
parent: chartbars
section: references
status: review
---

## Definition

Returns the **ChartBars** index value at a specified x-coordinate relative to the ChartControl.

## Method Return Value

An **int** value representing the bar index.

## Syntax

**ChartBars.GetBarIdxByX(ChartControl chartControl, int x)**

## Method Parameters

{% table %}

---

* **chartControl**
* The **ChartControl** object used to determine the chart's time axis

---

* **x**
* The x-coordinate used to find a bar index value
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // get the users mouse down point and convert to device pixels for DPI accuracy
   int mousePoint = chartControl.MouseDownPoint.X.ConvertToHorizontalPixels(chartControl.PresentationSource);
   
   // convert mouse point to bar index
   int barIdx = ChartBars.GetBarIdxByX(chartControl, mousePoint);
   
   Print("User clicked on Bar #" + barIdx);
}
```
