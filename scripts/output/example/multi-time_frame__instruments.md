---

title: multi-time_frame__instruments
pathName: multi-time-frame-instruments
created: Thursday, October 3rd 2024, 11:28:42 am
updated: Thursday, October 3rd 2024, 12:16:54 pm
---

## Multi-Series Scripting Overview

NinjaScript supports multiple time frames and instruments in a single script. This is possible because you can add additional Bars objects to indicators or strategies, in addition to the primary Bars object to which they are applied. A Bars object represents all of the bars of data on a chart. For example, if you had a MSFT 1-minute chart with 200 bars on it, the 200 bars represent one Bars object. In addition to adding Bars objects for reference or for use with indicator methods, you can execute trades across all the different instruments in a script. There is extreme flexibility in the NinjaScript model that NinjaTrader uses for multi-bars scripts, so it is very important that you understand how it all works before you incorporate additional Bars objects in a script. An important fact to understand is that NinjaScript is truly event-driven; every Bars object in a script will call the [OnBarUpdate()](onbarupdate.htm) method. The significance of this will become evident throughout this page.

{% callout type="note" %}  
Note: If using [OnMarketData()](onmarketdata.htm), a subscription will be created on all bars series added in your indicator or strategy (even if the instrument is the same). The market data subscription behavior occurs both in real-time and during [TickReplay](developing_for__tick_replay.htm) historical.  
{% /callout %}

## Important Methods and Properties

- [AddDataSeries()](adddataseries.htm)
- [BarsArray](barsarray.htm)
- [BarsInProgress](barsinprogress.htm)
- [CurrentBars](currentbars.htm)

{% callout type="note" %}  
Note: As we move through this section, the term "Primary Bars" will be used and for the purpose of clarification, this will always refer to the first Bars object loaded into a script. For example, if you apply a script on MSFT 1-minute chart, the primary Bars would be MSFT 1-minute data set. This section is written in sequential fashion. Example code is re-used and built upon from subsection to subsection.  
{% /callout %}

### Data Processing Sequence

Understanding the sequence in which bars series process and the granularity provided by market data vendors is essential for efficient multi-series development. Let’s assume we have two series (primary and secondary) in our script, which is representing the same instrument, yet different intervals. During historical data processing, NinjaTrader updates the two series strictly according to their timestamps, calling the primary bar series of the corresponding timestamps first, and then calling the secondary series.

{% callout type="note" %}  
Note: Historical bars are processed according to their timestamps with the primary bars first, followed by the secondary, which is NOT guaranteed to be the same sequence that these events occurred in real-time. If your development requires ticks to process in the same sequence historically as well as in real-time, you will need to enable [Tick Replay](developing_for__tick_replay.htm) (utilizes more PC resources).  
{% /callout %}

## Shared Timestamps

In circumstances where multiple bars share the same exact timestamps, your primary bars series will always be processed first, followed by the secondary bars series (regardless of the period value used). Consequently, if you were looking to obtain a value from the secondary bars series, it would ONLY be available after the primary series has been processed for the same timestamps.

{% callout type="tip" %}  
Tip: While the following behavior applies to all period types, the effects are amplified on smaller time frames. If you plan on using a high-resolution (e.g., 1-second, 10-tick, etc.), please make sure to thoroughly read and understand the material below when working with these additional series. It is also important to keep in mind that the granularity of the timestamps will dictate how accurately NinjaTrader can synchronize the bars in historical processing. The available level of granularity will be dependent upon which [data provider](data_by_provider.htm) you use with NinjaTrader.  
{% /callout %}

## Illustration of Processing Sequence

Assume our primary series is a 5-tick bar series, and our secondary series is a 1-tick bar series. The time of day is near the session close, so a rapid sequence of bars is generated.

**Figure 1. Bar processing with shared timestamps**  
(Include your illustration here)

## Adding Additional Bars Objects to NinjaScript

Additional Bars are added to a script via the [AddDataSeries()](adddataseries.htm) method in the [OnStateChange()](onstatechange.htm) method when the [State](state.htm) has reached State.Configure.

The following example demonstrates adding a Bars object:

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "Multi-Time Frame & Instruments Example";
    }
    else if (State == State.Configure)
    {
        AddDataSeries(BarsPeriodType.Minute, 3);
        AddDataSeries("AAPL", BarsPeriodType.Minute, 1);
    }
}
```

{% callout type="note" %}  
Note: To maximize data loading performance, any NinjaScript object (indicator or strategy as host) which references a multi-series indicator that calls AddDataSeries must include its own calls to AddDataSeries().  
{% /callout %}

## Series<t> Objects

[Series<t>](seriest.htm) is the base class for [PriceSeries](priceseries.htm), [TimeSeries](timeseries.htm), and [VolumeSeries](volumeseries.htm). Rather than using one of these pre-defined derived classes, you can create your own Series<t> collection to hold any Type that you choose.

### Initializing a Series<t> with BarsArray

```csharp
private Series<double> myEmptyIndexedSeries;

protected override void OnStateChange()
{
    if (State == State.DataLoaded)
    {
        myEmptyIndexedSeries = new Series<double>(BarsArray[1]);
    }
}
```

### Initializing a Series<t> with an Indicator Method

```csharp
private Series<double> primarySeries;
private Series<double> secondarySeries;

protected override void OnStateChange()
{
    if (State == State.Configure)
    {
        AddDataSeries(BarsPeriodType.Minute, 5);
    }
    else if (State == State.DataLoaded)
    {
        primarySeries = new Series<double>(this);
        secondarySeries = new Series<double>(SMA(BarsArray[1], 50));
    }
}
```

## Accessing the Price Data in a Multi-Bars NinjaScript

You can access the current bar's closing price with the following statement:

```csharp
Close[0];
```

The following example demonstrates various ways to access price data.

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBars[0] <= BarsRequiredToPlot || CurrentBars[1] <= BarsRequiredToPlot || CurrentBars[2] <= BarsRequiredToPlot)
        return;

    if (BarsInProgress == 0)
    {
        double primaryClose = Close[0];
        double msft3minClose = Closes[1][0];
        double aapl1minClose = Closes[2][0];
    }
}
```

## Entering, Exiting and Retrieving Position Information

This section is relevant for NinjaScript strategies only. Here's an example:

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBars[0] <= BarsRequiredToPlot || CurrentBars[1] <= BarsRequiredToPlot || CurrentBars[2] <= BarsRequiredToPlot)
        return;

    if (BarsInProgress == 0)
    {
        EnterLong();
    }
    if (BarsInProgress == 2)
    {
        EnterLong(0, 100, "BUY MSFT");
    }
}
```

{% callout type="note" %}  
Notes:

1. Multiple Bars objects of the same instrument should only submit orders to the first Bars context of that instrument.
2. End-of-session handling applies only to the first Bars context for an instrument.
3. For advanced order methods, always submit historical orders to the most granular of time frames.
4. Use the Positions property carefully to reference the instrument of the current context.  
{% /callout %}
