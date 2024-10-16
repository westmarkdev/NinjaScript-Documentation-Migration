---
title: "AddKagi()"
pathName: /docs/desktop/addkagi
---

## Definition

Similar to the [AddDataSeries()](/docs/desktop//adddataseries) method for adding Bars objects, this method adds a Kagi Bars object for multi-series NinjaScript.

{% callout type="note" %}

1. When running NinjaScript, you will be able to choose the first instrument and bar interval to run on. This first Bars object will carry a [BarsInProgress](/docs/desktop/barsinprogress) index of 0.
2. In a multi-time frame and multi-instrument NinjaScript, supplementary Bars objects are added via this method in State.Configure state of the [OnStateChange()](/docs/desktop/onstatechange) method and given an incremented BarsInProgress index value. See additional information on running [multi-bars scripts](/docs/desktop/multi-time_frame__instruments).
3. The [BarsInProgress](/docs/desktop/barsinprogress) property can be used to filter updates between different bars series
4. If using [OnMarketData()](/docs/desktop/onmarketdata), a subscription will be created on all bars series added in your indicator or strategy strategy (even if the instrument is the same).  The market data subscription behavior occurs both in real-time and during [TickReplay](/docs/desktop/developing_for__tick_replay) historical
5. For adding regular Bars types please use [AddDataSeries()](/docs/desktop/adddataseries)
6. A Tick Replay indicator or strategy CANNOT use a MarketDataType.Ask or MarketDataType.Bid series.  Please see [Developing for Tick Replay](/docs/desktop/developing_for__tick_replay) for more information.

{% /callout %}

## Syntax

```csharp
AddKagi(string instrumentName, Data.BarsPeriodType baseBarsPeriodType, int baseBarsPeriodTypeValue, int reversal, Data.ReversalType reversalType, Data.MarketDataType marketDataType)  
```

```csharp
AddKagi(string instrumentName, Data.BarsPeriodType baseBarsPeriodType, int baseBarsPeriodTypeValue, int reversal, Data.ReversalType reversalType, Data.MarketDataType marketDataType, string tradingHoursName)  
```

```csharp
AddKagi(string instrumentName, Data.BarsPeriodType baseBarsPeriodType, int baseBarsPeriodTypeValue, int reversal, Data.ReversalType reversalType, Data.MarketDataType marketDataType, string tradingHoursName, bool? isResetOnNewTradingDay)
```

{% callout type="warning" %}
This method should ONLY be called from the [OnStateChange()](/docs/desktop//onstatechange) method during State.Configure

- Should your script be the host for other scripts that are creating indicators and series dependent resources in State.DataLoaded, please make sure that the host is doing the same AddKagi() calls as those hosted scripts would. For further reference, please also review the 'Adding additional Bars Objects to NinjaScript' section in [Multi-Time Frame &amp; Instruments](/docs/desktop/multi-time_frame__instruments)

- Arguments supplied to AddKagi() should be hardcoded and NOT dependent on run-time variables which cannot be reliably obtained during [State.Configure](/docs/desktop/state) (e.g., [Instrument](/docs/desktop/instrument), [Bars](/docs/desktop/bars), or user input).  Attempting to add a data series dynamically is NOT guaranteed and therefore should be avoided.  Trying to load bars dynamically may result in an error similar to: Unable to load bars series. Your NinjaScript may be trying to use an additional data series dynamically in an unsupported manner.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| instrumentName | A `string` determining instrument name such as "MSFT" |
| baseBarsPeriodType | The underlying BarsType used for the Kagi bars period. {% <br> %}  &bull; BarsPeriodType.Day{% <br> %} &bull; BarsPeriodType.Minute{% <br> %} &bull; BarsPeriodType.Second{% <br> %} &bull; BarsPeriodType.Tick{% <br> %} &bull; BarsPeriodType.Volume |
| baseBarsPeriodTypeValue | An `int` determining the underlying period interval such as "3" for 3 minute bars |
| reversal | An `int` determining the required price movement in the reversal direction before a reversal is identified on the chart |
| reversalType | An `enum` determining the mode reversal period is based. {% <br> %} &bull; ReversalType.Percent{% <br> %} &bull; ReversalType.Tick |
| marketDataType | The MarketDataType used for the bars object (last, bid, ask) {% <br> %} &bull; MarketDataType.Ask{% <br> %} &bull; MarketDataType.Bid{% <br> %} &bull; MarketDataType.Last{% <br> %} **Note**: Please see the article here on using Bid/Ask series. |
| tradingHoursName | A string determining the trading hours template for the instrument |
| isResetOnNewTradingDay | A nullable `bool` determining if the Bars object should [Break at EOD](/docs/desktop/break_at_eod) {% <br> %} Will accept true, false or null as the input.  If null is used, the data series will use the settings of the primary data series. |

{% callout type="tip" %}
You can optionally add the exchange name as a suffix to the symbol name. This is only advised if the instrument has multiple possible exchanges that it can trade on and it is configured within the Instruments window. For example: AddKagi("MSFT Arca", PeriodType.Minute, 1, 2, ReversalType.Tick, MarketDataType.Last)
{% /callout %}

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       Name = "Examples Indicator";
   }
   else if (State == State.Configure)
   {
       // Add a 1 minute Kagi Bars object for the ES 03-18 contract - BarsInProgress index = 1
       AddKagi("ES 03-18", BPeriodType.Minute, 1, 2, ReversalType.Tick, MarketDataType.Last);
   }
}

protected override void OnBarUpdate()
{
     // Ignore the primary Bars object and only process the Kagi Bars object
     if (BarsInProgress == 1)
     {
         // Do something;
     }
}
```
