---
title: "OnBarUpdate()"
pathName: onbarupdate
---

## Definition

An event driven method which is called whenever a bar is updated. The frequency in which OnBarUpdate is called will be determined by the "[Calculate](calculate)" property. OnBarUpdate() is the method where all of your script's core bar based calculation logic should be contained.

{% callout type="note" %}
Notes:

- For [multi-timeframe and instrument scripts](multi-time_frame__instruments), the OnBarUpdate method is called for each Bars object of a strategy. You MUST filter for the exact bar update events using the "[BarsInProgress](barsinprogress)" property you want your system logic to execute against.
- Hosted indicators will need to be accessed by the hosting script to ensure OnBarUpdate functionality. This can be done by:
  1. Calling [Update](update) on the hosted indicator within the host script,
  2. Including a plot in the hosted indicator and accessing the plot in the host script,
  3. Including a plot in the hosted indicator and adding the indicator to the chart with [AddChartIndicator](addchartindicator) (strategies only).
{% /callout %}

## Related Methods and Properties

|  |  |
| --- | --- |
| [BarsPeriod](barsperiod) | The primary Bars object time frame (period type and interval). |
| [Calculate](calculate) | Determines how often [OnBarUpdate()](onbarupdate) is called for each bar. |
| [Count](count) | The total number of bars or data points. |
| [CurrentBar](currentbar) | A number representing the current bar in a Bars object that the OnBarUpdate() method in an indicator or strategy is currently processing. |
| [IsDataSeriesRequired](isdataseriesrequired) | Determines if a Data Series is required for calculating this NinjaScript object. |
| [IsFirstTickOfBar](isfirsttickofbar) | Indicates if the incoming tick is the first tick of a new bar. |
| [IsResetOnNewTradingDays](isresetonnewtradingdays) | Determines if the specified bar series is using Break at EOD. |
| [IsTickReplays](istickreplays) | Indicates the specified bar series is using Tick Replay. |
| [Update()](update) | Forces the OnBarUpdate() method to be called so that indicator values are updated to the current bar. |

## Method Return Value

This method does not return a value.

## Syntax

You must override this method with the following syntax:

```csharp
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
