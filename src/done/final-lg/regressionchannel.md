---
title: "RegressionChannel"
pathName: regressionchannel
---

## Definition

Represents an interface that exposes information regarding a Regression Channel [IDrawingTool](idrawingtool).

## Methods and Properties

|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the ending point of the drawing object |
| RegressionStroke | The [Stroke](stroke_class) object used to draw the middle line of the object |
| LowerChannelStroke | The [Stroke](stroke_class) object used to draw the lower line of the object |
| UpperChannelStroke | The [Stroke](stroke_class) object used to draw the upper line of the object |
| PriceType | Possible values are: PriceType.Close, PriceType.High, PriceType.Low, PriceType.Median, PriceType.Open, PriceType.Typical |
| ChannelType | An enum value representing if the object will use standard deviations calculations for the upper/lower lines. Possible values are: RegressionChannelType.Segment, RegressionChannelType.StandardDeviation |
| ExtendLeft | A bool value representing if the object will extend to the left |
| ExtendRight | A bool value representing if the object will extend to the right |
| StandardDeviationLowerDistance | A double value representing the standard deviation distance to the lower line |
| StandardDeviationUpperDistance | A double value representing the standard deviation distance to the upper line |

## Example

```csharp
// Instantiate a RegressionChannel object
NinjaTrader.NinjaScript.DrawingTools.RegressionChannel myRegChan = Draw.RegressionChannel(this, "tag1", 10, 0, Brushes.Blue);
// Change the object's PriceType
myRegChan.PriceType = PriceType.Median;
```

{% callout type="note" %}
Note: To differentiate between DrawingTools.RegressionChannel and Indicators.RegressionChannel when assigning a RegressionChannel object, you will need to invoke the former path explicitly, as seen in the example above.
{% /callout %}