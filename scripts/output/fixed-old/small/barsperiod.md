---
path: barsperiod
title: BarsPeriod
---

## Definition

The primary Bars object time frame (period type and interval).

{% callout type="warning" %}
This property should NOT be accessed within the [OnStateChange()](onstatechange.md) method before the State has reached State.DataLoaded

{% /callout %}

## Property Value

A [Bars](bars.md) series object representing the time frame of the Bars.

## Syntax

`BarsPeriod.BarsPeriodType` - The type of bars used for the period, as well as the enumeration value under which the any of the 14 default NinjaTrader types are registered. Possible values include:

|  |  |
| --- | --- |
| BarsPeriodType.Tick | 0 |
| BarsPeriodType.Volume | 1 |
| BarsPeriodType.Range | 2 |
| BarsPeriodType.Second | 3 |
| BarsPeriodType.Minute | 4 |
| BarsPeriodType.Day | 5 |
| BarsPeriodType.Week | 6 |
| BarsPeriodType.Month | 7 |
| BarsPeriodType.Year | 8 |
| BarsPeriodType.HeikenAshi | 9 |
| BarsPeriodType.Kagi | 10 |
| BarsPeriodType.Renko | 11 |
| BarsPeriodType.PointAndFigure | 12 |
| BarsPeriodType.LineBreak | 13 |
| BarsPeriodType.Volumetric | 14 |

{% callout type="note" %}
When creating custom [BarsTypes](bars_type.md), it is recommended to pick high, unique enumeration value to avoid conflict from other BarsTypes that may be used by a single installation.  

BarsPeriod = new BarsPeriod { BarsPeriodType = (BarsPeriodType)123456, BarsPeriodTypeName = "MyCustomBars", Value = 1 };`

{% /callout %}

|  |  |
| --- | --- |
| BarsPeriod.BaseBarsPeriodType | Only relevant for [HeikenAshi](addheikenashi.md), [Kagi](addkagi.md), [LineBreak](addlinebreak.md), [PointAndFigure](addpointandfigure.md) and [Volumetric](addvolumetric.md) Bars objects. Same possible values as BarsPeriod.BarsPeriodType |
| BarsPeriod.BaseBarsPeriodValue | Only relevant for [HeikenAshi](addheikenashi.md), [Kagi](addkagi.md), [LineBreak](addlinebreak.md), [PointAndFigure](addpointandfigure.md) and [Volumetric](addvolumetric.md) Bars objects. Determines an integer value representing the basePeriodTypeValue parameter |
| BarsPeriod.MarketDataType | The data type used to build the bars.  Possible values:<ul><li>MarketDataType.Ask</li><li>MarketDataType.Bid</li><li>MarketDataType.Last</li></ul> |
| BarsPeriod.PointAndFigurePriceType | Only relevant for PointAndFigure Bars objects. Possible values:<ul><li>PointAndFigurePriceType.Close</li><li>PointAndFigurePriceType.HighLow</li><li>PointAndFigurePriceType.HighsAndLows</li></ul> |
| BarsPeriod.ReversalType | Only relevant for Kagi Bars objects. Possible values:<ul><li>ReversalType.Percent</li><li>ReversalType.Tick</li></ul> |
| BarsPeriod.Value | Determines an integer value representing the period parameter.<ul><li>When using Kagi Bars objects this represents the "reversal" parameter</li><li>When using LineBreak Bars objects this represents the "lineBreakCount" parameter</li><li>When using PointAndFigure Bars objects this represents the "boxSize" parameter</li><li>When using Renko Bars objects this represents the "brickSize" parameter</li></ul> |
| BarsPeriod.Value2 | Only relevant for PointAndFigure Bars objects. Determines an integer value representing the "reversal" parameter. |

## Examples

### Checking BarsPeriod values

```csharp
// Calculate only if there is a 100 tick chart or greater
protected override void OnBarUpdate()
{
     if (BarsPeriod.BarsPeriodType == BarsPeriodType.Tick && BarsPeriod.Value >= 100)
     {
         // Indicator calculation logic here
     }
}
```

### Creating a new BarsPeriod object

```csharp
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
           // add a 1440 minute apple bars object using the RTH session template
           AddDataSeries("AAPL", new BarsPeriod { BarsPeriodType = BarsPeriodType.Minute, Value = 1440 }, "US Equities RTH");
     }

     else if (State == State.DataLoaded)
     {
           // Print out the loaded bars period
           Print(Instrument.FullName + " " + BarsPeriod); // MSFT 1 Minute
           Print(BarsArray[1].Instrument.FullName + " " + BarsArray[1].BarsPeriod); // AAPL 1440 Minute
     }
}
```
