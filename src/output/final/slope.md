---
title: "Slope()"
pathName: /docs/desktop/slope
---

## Definition

Returns a measurement of the steepness of a price series (y value) measured by the change over time (x value). The return value can also be thought of as the ratio between the startBarsAgo and endBarsAgo parameters passed to the method.

The formula which is returned from the parameters passed is:

(series[endBarsAgo] - series[startBarsAgo]) / (startBarsAgo - endBarsAgo)

{% callout type="note" %}
The return value should NOT be confused with the angle (or radians) of a line that displays on the chart.
{% /callout %}

## Method Return Value

This method returns a double value indicating the slope of a line; A value of 0 returns if either the startBarsAgo or endBarsAgo parameters are less than 0 or both parameters are of equal value.

### Syntax

```csharp
Slope(ISeries<double> series, int startBarsAgo, int endBarsAgo)
```

{% callout type="warning" %}
The "startBarsAgo" parameter MUST be greater than the "endBarsAgo" parameter.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| series | Any Series<double> type object such as an indicator, Close, High, Low, etc... |
| startBarsAgo | The starting point of a series to be evaluated |
| endBarsAgo | The ending point of a series to be evaluated |

{% callout type="tip" %}
Thinking in degrees, for example a 1 to -1 return range would translate to 45 to -45. To convert, you could look into working with this formula - Math.Atan(Slope) * 180 / Math.PI.
{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Prints the slope of the 20 period simple moving average of the last 10 bars
    Print(Slope(SMA(20), 10, 0));
}
```
