---
title: adddataseries
pathName: adddataseries
created: Thursday, October 3rd 2024, 11:53:17 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

Adds a Bars object for developing a multi-series (multi-time frame or multi-instrument) NinjaScript.

## Related Methods and Properties

|  |  |
| --- | --- |
| [AddHeikenAshi()](addheikenashi.htm) | This method adds a Heiken Ashi Bars object for multi-series NinjaScript.  |
| [AddKagi()](addkagi.htm) | This method adds a Kagi Bars object for multi-series NinjaScript. |
| [AddLineBreak()](addlinebreak.htm) | This method adds a Line Break Bars object for multi-series NinjaScript.  |
| [AddPointAndFigure()](addpointandfigure.htm) | This method adds a Point-and-Figure Bars object for multi-series NinjaScript. |
| [AddRenko()](addrenko.htm) | This method adds a Renko Bars object for multi-series NinjaScript.  |
| [AddVolumetric()](addvolumetric.htm) | This method adds an Order Flow Volumetric Bars object for multi-series NinjaScript.  |
| [BarsArray](barsarray.htm) | An array holding Bars objects that are added via the [AddDataSeries()](adddataseries.htm) method. |
| [BarsInProgress](barsinprogress.htm) | An index value of the current Bars object that has called the [OnBarUpdate()](onbarupdate.htm) method. |
| [BarsPeriods](barsperiods.htm) | Holds an array of BarsPeriod objects synchronized to the number of unique Bars objects held within the parent NinjaScript object. |
| [CurrentBars](currentbars.htm) | Holds an array of int values representing the number of the current bar in a Bars object. |

## Syntax

The following syntax will add another Bars object for the primary instrument of the script.

```
AddDataSeries(BarsPeriod barsPeriod)
AddDataSeries(BarsPeriodType periodType, int period)
```

The following syntax allows you to add another Bars object for a different instrument to the script:

```
AddDataSeries(string instrumentName, BarsPeriodType periodType, int period)
AddDataSeries(string instrumentName, BarsPeriodType periodType, int period, MarketDataType marketDataType)
AddDataSeries(string instrumentName, BarsPeriod barsPeriod)
AddDataSeries(string instrumentName, BarsPeriod barsPeriod, string tradingHoursName)
AddDataSeries(string instrumentName, BarsPeriod barsPeriod, string tradingHoursName, bool? isResetOnNewTradingDay)
AddDataSeries(string instrumentName, BarsPeriod barsPeriod, int barsToLoad, string tradingHoursName, bool? isResetOnNewTradingDay)
AddDataSeries(string instrumentName) // only for R15 and higher
```

{% callout type="warning" %}

- This method should ONLY be called from the [OnStateChange()](onstatechange.htm) method during State.Configure.  
- If your script is the host for other scripts that are creating indicators and series dependent resources in State.DataLoaded, please make sure that the host is doing the same AddDataSeries() calls as those hosted scripts would.  
- Arguments supplied to AddDataSeries() should be hardcoded and NOT dependent on run-time variables which cannot be reliably obtained during [State.Configure](state.htm).  
- Attempting to add data series dynamically is NOT guaranteed and therefore should be avoided.  
- When adding multiple Data Series of the same instrument and the same Bar Type, the 'barsToLoad' property will only be effective on the first added series.  
- The AddDataSeries(string instrumentName) overload allows loading a different instrument yet using the same BarsPeriod.  
- If your NinjaScript object is using AddDataSeries() allowing to specify a tradingHoursName, please keep in mind that an indicator/strategy with multiple DataSeries of the same instrument will only process real-time OnBarUpdate() calls when a tick occurs in the session of the trading hour template of all added series.  
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| instrumentName | A string determining the instrument name such as "MSFT". |
| barsPeriod | The [BarsPeriod](barsperiod.htm) object (period type and interval). |
| periodType | The BarsType used for the bars period. Possible values are: BarsPeriodType.Tick, BarsPeriodType.Volume, BarsPeriodType.Range, BarsPeriodType.Second, BarsPeriodType.Minute, BarsPeriodType.Day, BarsPeriodType.Week, BarsPeriodType.Month, BarsPeriodType.Year. |
| period | An int determining the period interval such as "3" for 3-minute bars. |
| marketDataType | The MarketDataType used for the bars object (last, bid, ask). Possible values are: MarketDataType.Ask, MarketDataType.Bid, MarketDataType.Last. |
| tradingHoursName | A string determining the trading hours template for the instrument. |
| isResetOnNewTradingDay | A nullable bool determining if the Bars object should [Break at EOD](break_at_eod.htm). Will accept true, false or null as the input. If null is used, the data series will use the settings of the primary data series. |
| barsToLoad | An int determining the number of historical bars to load. |

{% callout type="tips" %}

1. You can optionally add the exchange name as a suffix to the symbol name if the instrument has multiple possible exchanges that it can trade on. For example: `AddDataSeries("MSFT Arca", BarsPeriodType.Minute, 5);`
2. You can add a custom [BarsType](bars_type.htm) which is installed on your system by casting the registered enum value for that BarsPeriodType. For example: `AddDataSeries((BarsPeriodType)14, 10);`
3. You can specify optional [BarsPeriod](barsperiod.htm) values (such as [Value2](optimization_fitness_value.htm)) of a custom BarsType in the BarsPeriod object initializer. For example: `AddDataSeries(new BarsPeriod() { BarsPeriodType = (BarsPeriodType)14, Value = 10, Value2 = 20 });`
4. For the instrument name parameter, null could be passed in, resulting in the primary data series instrument being used.  
{% /callout %}

## Examples

```csharp
protected override void OnStateChange() 
{
    if (State == State.Configure) 
    {
        // Add a 5 minute Bars object - BarsInProgress index = 1 
        AddDataSeries(BarsPeriodType.Minute, 5);
        
        // Add a 100 tick Bars object for the ES 09-16 contract - BarsInProgress index = 2 
        AddDataSeries("ES 09-16", BarsPeriodType.Tick, 100); 
    }
}

protected override void OnBarUpdate() 
{ 
    // Ignore bar update events for the supplementary - Bars object added above 
    if (BarsInProgress == 1 || BarsInProgress == 2) 
        return; 

    // Go long if we have three up bars on all bars objects 
    if (Close[0] > Open[0] && Closes[1][0] > Opens[1][0] && Closes[2][0] > Opens[2][0]) 
        EnterLong(); 
}
```

```csharp
protected override void OnStateChange() 
{
    if (State == State.Configure) 
    {
        // Our hosting script needs to have the AddDataSeries call included as well, which the Pivots indicator we call in the 2nd statement below 
        // also has per default in its own State.Configure method. 
        AddDataSeries(BarsPeriodType.Day, 1);
    } 
    else if (State == State.DataLoaded) 
    {
        // In this state, we pass the 1 day series to the Pivots indicator (as BarsArray[1]) and create its instance 
        pivots = Pivots(BarsArray[1], PivotRange.Weekly, HLCCalculationMode.DailyBars, 0, 0, 0, 20);
    }
}
```

{% callout type="note" %}  
Refer to the NinjaScript documentation for more specific details on each method and property.  
{% /callout %}