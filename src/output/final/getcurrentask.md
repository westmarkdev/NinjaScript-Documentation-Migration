---
title: "GetCurrentAsk()"
pathName: /docs/getcurrentask
---

## Definition

Returns the current real-time ask price.

{% callout type="note" %}

1. When accessed during State.Historical, the [Close](/docs/desktop/close) price of the evaluated bar is substituted. To access historical Ask prices, please see [Developing for Tick Replay](/docs/desktop/developing_for__tick_replay).
2. The GetCurrentAsk() method runs on the bar series currently updating determined by the [BarsInProgress](/docs/desktop/barsinprogress) property. For [multi-instrument](/docs/desktop/multi-time_frame__instruments) scripts, an additional int "barsSeriesIndex" parameter can be supplied which forces the method to run on a supplementary bar series.
{% /callout %}

## Method Return Value

A double value representing the current ask price.

### Syntax

```
GetCurrentAsk()
GetCurrentAsk(int barsSeriesIndex)
```

## Parameters

|  |  |
| --- | --- |
| barsSeriesIndex | An `int` value determining the bar series the method runs. Note: This optional parameter is reserved for multi-instrument scripts |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Ensure we do not call GetCurrentAsk() on historical data
    if (State == State.Historical)
        return;
    double currentAsk = GetCurrentAsk();
    Print("The Current Ask price is: " + currentAsk);
    // The Current Ask price is: 1924.75
}
```

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "Example's Indicator";
    }
    if (State == State.Configure)
    {
        // Add MSFT as our additional data series
        AddDataSeries("MSFT", BarsPeriodType.Minute, 1);
    }
}
protected override void OnBarUpdate()
{
    // Ensure we do not call GetCurrentAsk() on historical data
    if (State == State.Historical)
        return;
    if (BarsInProgress == 0)
    {
        double primaryAsk = GetCurrentAsk(0);
        Print("The Primary Ask price is: " + primaryAsk);
        // The Primary Ask price is: 1924.75
    }
    if (BarsInProgress == 1)
    {
        double msftAsk = GetCurrentAsk(1);
        Print("MSFT's Current Ask price is: " + msftAsk);
        // MSFT's Current Ask is: 43.63
    }
}
```
