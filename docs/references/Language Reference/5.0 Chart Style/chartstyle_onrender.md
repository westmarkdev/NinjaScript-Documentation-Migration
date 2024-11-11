---
title: OnRender()
pathName: chartstyle_onrender
parent: chart_style
status: imported
section: references
---

## Definition

An event driven method used to render content to a ChartStyle. The **OnRender()** method is called every time the chart values are updated. These updates are driven by incoming data to the chart bars or by a user manually interacting with the chart control or chart scale.

## Method Return Value

This method does not return a value.

## Syntax

You must override the method in your ChartStyle with the following syntax:

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)  
{  
}
```

## Method Parameters

{% table %}

---

* **chartControl**
* A ChartControl representing the x-axis

---

* **chartScale**
* A ChartScale representing the y-axis

---

* **chartBars**
* A ChartBars representing the Bars series for the chart
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)
{
    // Rendering logic for our chart style
}
```
