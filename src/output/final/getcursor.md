---
title: "GetCursor()"
pathName: /docs/getcursor
---

## Definition

An event driven method which is called when a chart object is selected. This method can be used to change the cursor image used in various states.

## Method Return Value

This method returns a [Cursor](https://msdn.microsoft.com/en-us/library/system.windows.forms.cursor(v=vs.110).aspx) used to paint the mouse pointer.

## Syntax

You must override the method in your Drawing Tool with the following syntax:

```csharp
public override Cursor GetCursor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| chartControl | A [ChartControl](/docs/desktop/chartcontrol) representing the x-axis |
| chartPanel | A [ChartPanel](/docs/desktop/chartpanel) representing the panel for the chart |
| chartScale | A [ChartScale](/docs/desktop/chartscale) representing the y-axis |
| point | A Point in device pixels representing the current mouse cursor position |

## Examples

```csharp
public override Cursor GetCursor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
    switch (DrawingState)
    {
        //when drawing, display the cursor as a pen
        case DrawingState.Building: return Cursors.Pen;

        // when moving, display a four-headed sizing cursor
        case DrawingState.Moving: return Cursors.SizeAll;

        default: return Cursors.Pen;
    }
}
```
