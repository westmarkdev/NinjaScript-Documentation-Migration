---

title: axisyrightwidth
pathName: axisyrightwidth
created: Thursday, October 3rd 2024, 11:24:43 am
updated: Thursday, October 3rd 2024, 12:16:53 pm
---

## Definition

Measures the distance (in pixels) between the y-axis and the right edge of a chart.

## Property Value

A double representing the number of pixels separating the y-axis and the right edge of the chart.

## Syntax

`<chartcontrol>.AxisYRightWidth`

## Example

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Print the number of pixels between the y-axis and the right edge of the chart
    double rightWidth = chartControl.AxisYRightWidth;
    Print(rightWidth);
}
```

Based on the image below, AxisYRightWidth reveals that the space between the y-axis and the right edge of the chart is 53 pixels on this chart.

![ChartControl_AxisYRightWidth](chartcontrol_axisyrightwidth.png)

{% callout type="note" %}  
Note: When there are no right-justified data series on a chart, AxisYRightWidth will return 0, as there will be no space between the y-axis and the right edge.  
{% /callout %}
