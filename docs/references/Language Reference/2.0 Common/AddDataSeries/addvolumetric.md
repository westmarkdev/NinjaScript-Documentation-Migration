---
section: references
parent: adddataseries
title: AddVolumetric()
pathName: addvolumetric
status: imported
---

## Definition

Similar to the [AddDataSeries()](adddataseries) method for adding Bars objects, this method adds a [Order Flow](order_flow_volumetric_bars) Volumetric Bars object for multi-series NinjaScript.

{% callout type="note" %}

1. When running NinjaScript, you will be able to choose the first instrument and bar interval to run on. This first Bars object will carry a [BarsInProgress](barsinprogress) index of 0.
2. In a multi-time frame and multi-instrument NinjaScript, supplementary Bars objects are added via this method in State.Configure state of the [OnStateChange()](onstatechange) method and given an incremented BarsInProgress index value. See additional information on running [multi-bars scripts](multi_time_frame_instruments.md).
3. The [BarsInProgress](barsinprogress) property can be used to filter updates between different bars series
4. If using [OnMarketData()](onmarketdata), a subscription will be created on all bars series added in your indicator or strategy strategy (even if the instrument is the same).  The market data subscription behavior occurs both in real-time and during [TickReplay](developing_for_tick_replay.md) historical
5. For adding regular Bars types please use [AddDataSeries()](adddataseries)
6. A Tick Replay indicator or strategy CANNOT use a MarketDataType.Ask or MarketDataType.Bid series.  Please see [Developing for Tick Replay](developing_for_tick_replay.md) for more information.
7. To access additional Volumetric data points programmtically in your NinjaScript studies, please see the example [here](order_flow_volumetric_bars.md).
{% /callout %}

## Syntax

**AddVolumetric(string instrumentName, Data.BarsPeriodType baseBarsPeriodType, int baseBarsPeriodTypeValue, Data.VolumetricDeltaType deltaType, int tickPerLevel)**

**AddVolumetric(string instrumentName, Data.BarsPeriodType baseBarsPeriodType, int baseBarsPeriodTypeValue, Data.VolumetricDeltaType deltaType, int tickPerLevel, bool? isResetOnNewTradingDay)**

**AddVolumetric(string instrumentName, Data.BarsPeriodType baseBarsPeriodType, int baseBarsPeriodTypeValue, Data.VolumetricDeltaType deltaType, int tickPerLevel, string tradingHoursName, bool? isResetOnNewTradingDay)**

**AddVolumetric(string instrumentName, Data.BarsPeriodType baseBarsPeriodType, int baseBarsPeriodTypeValue, Data.VolumetricDeltaType deltaType, int tickPerLevel, int sizeFilter, string tradingHoursName, bool? isResetOnNewTradingDay) (R17 and higher only)**

{% callout type="warning" %}

* This method should ONLY be called from the [OnStateChange()](onstatechange) method during State.Configure
* Should your script be the host for other scripts that are creating indicators and series dependent resources in State.DataLoaded, please make sure that the host is doing the same AddVolumetric() calls as those hosted scripts would. For further reference, please also review the 'Adding additional Bars Objects to NinjaScript' section in [Multi-Time Frame & Instruments](multi_time_frame_instruments.md)
* Arguments supplied to AddVolumetric() should be hardcoded and NOT dependent on run-time variables which cannot be reliably obtained during [State.Configure](state) (e.g., [Instrument](instrument), [Bars](bars), or user input).  Attempting to add a data series dynamically is NOT guaranteed and therefore should be avoided.  Trying to load bars dynamically may result in an error similar to: Unable to load bars series. Your NinjaScript may be trying to use an additional data series dynamically in an unsupported manner.
{% /callout %}

## Parameters

{% table %}

* instrumentName
* A string determining instrument name such as "MSFT"

---

* baseBarsPeriodType
* The underlying BarsType used for the Volumetric bars period. Possible values are:
  * BarsPeriodType.Tick
  * BarsPeriodType.Volume
  * BarsPeriodType.Range
  * BarsPeriodType.Second
  * BarsPeriodType.Minute
  * BarsPeriodType.Day
  * BarsPeriodType.Week
  * BarsPeriodType.Month
  * BarsPeriodType.Year

---

* baseBarsPeriodTypeValue
* An int determining the underlying period interval such as "3" for 3 minute bars

---

* deltaType
* The DeltaType used for the Volumetric bars object delta calculations. Possible values are:
  * VolumetricDeltaType.BidAsk
  * VolumetricDetlaType.UpDownTick

---

* ticksPerLevel
* An int setting the aggregation of price levels for the Volumetric bar, pass in a 1 to analyze each price level individually

---

* sizeFilter
* An int setting the trade size allowed to count in the delta calculations

---

* tradingHoursName
* A string determining the trading hours template for the instrument

---

* isResetOnNewTradingDay
* A nullable bool determining if the Bars object should [Break at EOD](break_at_eod). Will accept true, false or null as the input.  If null is used, the data series will use the settings of the primary data series.
{% /table %}

{% callout type="note" %}

You can optionally add the exchange name as a suffix to the symbol name. This is only advised if the instrument has multiple possible exchanges that it can trade on and it is configured within the Instruments window. For example: AddVolumetric("MSFT Arca", BarsPeriodType.Minute, 1, VolumetricDeltaType.BidAsk, 1);

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
        // Add a 1 minute Order Flow Volumetric Bars object for the ES 03-18 contract - BarsInProgress index = 1 
        AddVolumetric("ES 03-18", BarsPeriodType.Minute, 1, VolumetricDeltaType.BidAsk, 1);
    }
} 

protected override void OnBarUpdate() 
{ 
    // Ignore the primary Bars object and only process the Order Flow Volumetric object 
    if (BarsInProgress == 1)
    {
        // Do something;
    }
}
```
