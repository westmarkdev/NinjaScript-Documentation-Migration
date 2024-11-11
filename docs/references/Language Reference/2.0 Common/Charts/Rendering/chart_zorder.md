---
title: ZOrder
pathName: zorder
parent: rendering
section: references
status: imported
---

## Definition

A unique identifier representing the index in which chart objects are drawn on the chart's Z-axis (front to back ordering). Objects with a higher **ZOrder** are drawn first.

{% callout type="note" %}

The **ZOrder** index should NOT be set using this property. Please use the dedicated [SetZOrder()](setzorder) for this purpose.

{% /callout %}

## Property Value

A int value representing the order that the object is drawn. Default value is categorized by the type of object drawn, which will then increment for each instance of the chart object that is drawn. Each type of object will have a different default starting value to keep these objects separate:

{% table %}

* Type
* Default Value

---

* Chart Bars
* 1

---

* NinjaScript Objects
* 10001

---

* Global Draw Objects
* 20001

---

* Draw Objects
* 30001
{% /table %}

## Syntax

**ZOrder**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // call the base.OnRender() to ensure standard Plots work as designed
    base.OnRender(chartControl, chartScale);

    // Print the currently assigned ZOrder index for this NinjaScript object
    Print("Current ZOrder level is: " + **ZOrder**);
}
```
