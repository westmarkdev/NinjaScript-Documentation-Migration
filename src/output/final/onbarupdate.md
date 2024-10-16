---
title: "OnBarUpdate()"
pathName: /docs/desktop/onbarupdate
---

## Definition

An event driven method which is called whenever a bar is updated. The frequency in which OnBarUpdate is called will be determined by the "[Calculate](/docs/desktop/calculate)" property. OnBarUpdate() is the method where all of your script's core bar based calculation logic should be contained.

{% callout type="note" %}
• For [multi-timeframe and instrument scripts](/docs/desktop/multi-time_frame__instruments), the OnBarUpdate method is called for each Bars object of a strategy. You MUST filter for the exact bar update events using the "[BarsInProgress](/docs/desktop/barsinprogress)" property you want your system logic to execute against.

• Hosted indicators will need to be accessed by the hosting script to ensure OnBarUpdate functionality. This can be done by:

1) Calling [Update](/docs/desktop/update) on the hosted indicator within the host script,
2) Including a plot in the hosted indicator and accessing the plot in the host script,
3) Including a plot in the hosted indicator and adding the indicator to the chart with [AddChartIndicator](/docs/desktop/addchartindicator) (strategies only)
{% /callout %}

## Related Methods and Properties

|  |  |
| --- | --- |
| [BarsPeriod](/docs/desktop/barsperiod) | The primary Bars object time frame (period type and interval). |
| [Calculate](/docs/desktop/calculate) | Determines how often [OnBarUpdate()](/docs/desktop/onbarupdate) is called for each bar. |
| [Count](/docs/desktop/count) | The total number of bars or data points. |
| [CurrentBar](/docs/desktop/currentbar) | A number representing the current bar in a Bars object that the OnBarUpdate() method in an indicator or strategy is currently processing. |
| [IsDataSeriesRequired](/docs/desktop/isdataseriesrequired) | Determines if a Data Series is required for calculating this NinjaScript object. |
| [IsFirstTickOfBar](/docs/desktop/isfirsttickofbar) | Indicates if the incoming tick is the first tick of a new bar. |
| [IsResetOnNewTradingDays](/docs/desktop/isresetonnewtradingdays) | Determines if the specified bar series is using Break at EOD. |
| [IsTickReplays](/docs/desktop/istickreplays) | Indicates the specified bar series is using Tick Replay. |
| [Update()](/docs/desktop/update) | Forces the OnBarUpdate() method to be called so that indicator values are updated to the current bar. |

## Method Return Value

This method does not return a value.

### Syntax

```csharp
// You must override this method with the following syntax:
protected override void OnBarUpdate()
{

}
```

{% callout type="tip" %}
The NinjaScript code wizards automatically generates the method syntax for you.
{% /callout %}

## Parameters

This method does not take any parameters.

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 1)
        return;

    // Compares the primary bar's low price to the 5-minute bar's low price
    if (Low[0] > Lows[1])
        Print("The current bar's low price is greater");
}
```
