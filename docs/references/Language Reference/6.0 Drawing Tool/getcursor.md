---
title: GetCursor()
pathName: getcursor
parent: drawing_tools
status: imported
section: references
---

## Definition

An event driven method which is called when a chart object is selected. This method can be used to change the cursor image used in various states.

## Method Return Value

This method returns a **Cursor** used to paint the mouse pointer.

## Syntax

You must override the method in your Drawing Tool with the following syntax:

```csharp
public override Cursor GetCursor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
}
```

## Method Parameters

{% table %}

---

* **chartControl**
* A [ChartControl](chartcontrol) representing the x-axis

---

* **chartPanel**
* A [ChartPanel](chartpanel) representing the panel for the chart

---

* **chartScale**
* A [ChartScale](chartscale) representing the y-axis

---

* **point**
* A Point in device pixels representing the current mouse cursor position
{% /table %}

## Examples

```csharp
public override Cursor GetCursor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
    switch (DrawingState)
    {
        //when drawing, display the cursor as a pen
        case DrawingState.Building:   return Cursors.Pen;

        // when moving, display a four-headed sizing cursor
        case DrawingState.Moving:   return Cursors.SizeAll;

        default: return Cursors.Pen;
    }
}
```
