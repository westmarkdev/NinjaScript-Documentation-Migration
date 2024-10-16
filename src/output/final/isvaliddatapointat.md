---
title: "IsValidDataPointAt()"
pathName: /docs/desktop/isvaliddatapointat
---

## Definition

Indicates if the specified input is set at a specified bar index value. Please also see the [Reset()](/docs/desktop/reset) method for more information.

{% callout type="note" %}
• If called directly from the instance of the NinjaScript object, the value returned corresponds to the Inputs Series (e.g., Close, High, Low, SMA, etc.).  
• When checking a [Bar](/docs/desktop/bars) or [PriceSeries](/docs/desktop/priceseries), IsValidDataPoint() returns true as long as the barIndex value falls between 0 and the total count for that series. These are special series which always contain a value set at every slot index for multi-series scripting purposes (e.g., comparing two price series with various session templates, or one series has more ticks than the other).  
• For a [Value](/docs/desktop/value) series or custom [Series&lt;t&gt;](/docs/desktop/seriest), IsValidDataPoint() returns true or false depending on if you have set a value at that index location.
{% /callout %}

## Method Return Value

A bool value, when true indicates that specified data point is set; otherwise false.

{% callout type="warning" %}
Calling IsValidDataPointAt() will only work with a MaximumBarsLookBackInfinite series. Attempting to check IsValidDataPointAt() on a MaximumBarsLookBack256 series will throw an error. Please check the Log tab of the Control Center.
{% /callout %}

## Syntax

```csharp
IsValidDataPointAt(int barIndex)

ISeries<t>.IsValidDataPointAt(int barIndex)
```

## Parameters

|  |  |
| --- | --- |
| barIndex | An `int` representing an absolute bar index value |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // only set plot value if hosted indicator is not reset
    if (SMA(20).IsValidDataPointAt(CurrentBar))
        MyPlot[0] = SMA(20)[0];
}
```
