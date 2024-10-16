---
title: "IsValidDataPoint()"
pathName: /docs/desktop/isvaliddatapoint
---

## Definition

Indicates if the specified input is set at a barsAgo value relative to the current bar. Please also see the [Reset()](/docs/desktop/reset) method for more information.

{% callout type="note" %}
• If called directly from the instance of the NinjaScript object, the value returned corresponds to the Input Series (e.g., Close, High, Low, SMA, etc).  
• When checking a [Bar](/docs/desktop/bars) or [PriceSeries](/docs/desktop/priceseries), IsValidDataPoint() returns true as long as the barAgo value falls between 0 and the total count for that series. These are special series which always contain a value set at every slot index for multi-series scripting purposes (e.g., comparing two price series with various session templates, or one series has more ticks than the other).  
• For a [Value](/docs/desktop/value) series or custom [Series<t>](/docs/desktop/seriest), IsValidDataPoint() returns true or false depending on if you have set a value at that index location.
{% /callout %}

## Method Return Value

A bool value, when true indicates that specified data point is set; otherwise false.

## Syntax

```csharp
IsValidDataPoint(int barsAgo)

ISeries<t>.IsValidDataPoint(int barsAgo)
```

{% callout type="warning" %}
Calling IsValidDataPoint() will only work for a MaximumBarsLookBackInfinite series. Attempting to check IsValidDataPoint() on a MaximumBarsLookBack256 series will throw an error. Please check the Log tab of the Control Center. In addition, since this method references BarsAgo data, it cannot be used during [OnRender()](/docs/desktop/onrender). Instead, please use the [IsValidDataPointAt](/docs/desktop/isvaliddatapointat) during OnRender.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| barsAgo | An `int` representing the number of historical bars from the current bar that the method will check. |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // only set plot value if hosted indicator is not reset
    if (SMA(20).IsValidDataPoint(0))
        MyPlot[0] = SMA(20)[0];
}
```