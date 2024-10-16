---
title: "OnMouseUp()"
pathName: /docs/desktop/onmouseup
---

## Definition

An event driven method is called any time the mouse pointer is over the chart control and a mouse button is being released.

## Method Return Value

This method does not return a value.

{% callout type="note" %}
For a combined single click operation, i.e. mouse down click, move and release the dataPoint reported will always be the initial starting one.
{% /callout %}

### Syntax

```csharp
public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| chartControl | A [ChartControl](/docs/desktop/chartcontrol) representing the x-axis |
| chartPanel | A [ChartPanel](/docs/desktop/chartpanel) representing the panel for the chart |
| chartScale | A [ChartScale](/docs/desktop/chartscale) representing the y-axis |
| dataPoint | A [ChartAnchor](/docs/desktop/chartanchor) representing a point where the user is releasing the mouse |

## Examples

```csharp
public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
    // When the user releases the mouse, ensure the drawing state is set to normal
    if (DrawingState == DrawingState.Editing || DrawingState == DrawingState.Moving)
        DrawingState = DrawingState.Normal;
}
```

