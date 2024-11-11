---
title: OnMouseUp()
pathName: onmouseup
parent: drawing_tools
status: imported
section: references
---

## Definition

An event driven method is called any time the mouse pointer is over the chart control and a mouse button is being released.

## Method Return Value

This method does not return a value.

{% callout type="note" %}

For a combined single click operation, i.e. mouse down click, move and release the dataPoint reported will always be the initial starting one.

{% /callout %}

## Syntax

You must override the method with the following syntax.

**public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)**

## Method Parameters

{% table %}

---

* **chartControl**
* A [ChartControl](chartcontrol) representing the x-axis

---

* **chartPanel**
* A [ChartPanel](chartpanel) representing the the panel for the chart

---

* **chartScale**
* A [ChartScale](chartscale) representing the y-axis

---

* **dataPoint**
* A [ChartAnchor](chartanchor) representing a point where the user is releasing the mouse
{% /table %}

## Examples

```csharp
public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   //when the user releases the mouse, ensure the drawing state is set to normal
   if (DrawingState == DrawingState.Editing || DrawingState == DrawingState.Moving)
     DrawingState = DrawingState.Normal;
}
```
