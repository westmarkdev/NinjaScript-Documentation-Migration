---
title: "OnMouseMove()"
pathName: /docs/desktop/onmousemove
---

## Definition

An event-driven method which is called any time the mouse pointer is over the chart control and a mouse is moving.

## Method Return Value

This method does not return a value.

{% callout type="note" %}
For a combined single click operation, i.e. mouse down click, move and release the dataPoint reported will always be the initial starting one.
{% /callout %}

## Syntax

You must override the method in your Drawing Tool with the following syntax.

```csharp
public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| chartControl | A [ChartControl](/docs/desktop/chartcontrol) representing the x-axis |
| chartPanel | A [ChartPanel](/docs/desktop/chartpanel) representing the panel for the chart |
| chartScale | A [ChartScale](/docs/desktop/chartscale) representing the y-axis |
| dataPoint | A [ChartAnchor](/docs/desktop/chartanchor) representing a point where the user is moving the mouse |

## Examples

```csharp
private ChartAnchor lastMouseMoveAnchor = new ChartAnchor();
private ChartAnchor MyAnchor;

public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
    // add any logic for when the mouse is moved here
    if (DrawingState == DrawingState.Moving)
    {
        // move the chart anchor when the drawing tool is in a moving state
        MyAnchor.MoveAnchor(lastMouseMoveAnchor, dataPoint, chartControl, chartPanel, chartScale, this);
        // don't forget to update delta point to last used!
        dataPoint.CopyDataValues(lastMouseMoveAnchor);
    }
}
```

