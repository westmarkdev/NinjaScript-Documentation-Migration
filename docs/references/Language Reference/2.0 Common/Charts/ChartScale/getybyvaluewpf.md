---
title: GetYByValueWpf()
pathName: getybyvaluewpf
parent: chartscale
section: references
status: review
---

## Definition

Returns a WPF coordinate on the chart determined by a series value represented on the chart scale.

## Method Return Value

An double value representing a WPF coordinate on the chart scale.

## Syntax

**<`chartscale>**.GetYByValueWpf(**double val**)

## Method Parameters

{% table %}

---

* **val**
* A **double** value which usually represents a price or indicator value
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // gets the wpf coordinate of the price value passed to the method
   int     valueByYWpf = chartScale.GetYByValueWpf(Bars.GetClose(Bars.Count - 1));

   Print("valueByYWpf: " + valueByYWpf); // 207
}
```

In the image below, we pass the last bar close as the value (example logic avoids using a bars ago index, see also [**OnRender()**](onrender) note #5), which in return tells us the last price displayed on the chart is at a WPF location of 207.30998 pixels.

![GetYByValueWpf](getybyvaluewpf.png)
