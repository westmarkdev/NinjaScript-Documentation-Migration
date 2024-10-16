---
title: "Bars Type"
pathName: /docs/desktop/bars_type
---

Creating custom Bars Types allows for incredible flexibility in the way you want to present data in a chart. The methods and properties covered in this section are unique to custom Bars Type development.

## Methods and Properties

|  |  |
| --- | --- |
| [AddBar()](/docs/desktop/addbar) | Adds new data points for the Bars Type. |
| [ApplyDefaultBasePeriodValue](/docs/desktop/applydefaultbaseperiodvalue) | Sets the default base values used for the [BarsPeriod](/docs/desktop/barsperiod) selected by the user (e.g., the default PeriodValue, DaysToLoad, etc.) for your custom Bar Type. |
| [ApplyDefaultValue](/docs/desktop/applydefaultvalue) | Sets the default [BarsPeriod](/docs/desktop/barsperiod) values used for a custom Bar Type. |
| [BuiltFrom](/docs/desktop/builtfrom) | Determines the base dataset used to build the BarsType (i.e., Tick, Minute, Day). |
| [GetInitialLookBackDays()](/docs/desktop/getinitiallookbackdays) | Determines how many days of data load when a user makes a "bars back" data request. |
| [GetPercentComplete()](/docs/desktop/getpercentcomplete) | Determines the value your BarsType would return for [Bars.PercentComplete](/docs/desktop/percentcomplete) |
| [Icon](/docs/desktop/icon_barstype) | The shape which displays next to the Bars Type menu item. |
| [IsRemoveLastBarSupported](/docs/desktop/isremovelastbarsupported) | Determines if the bars type can use the [RemoveLastBar()](/docs/desktop/removelastbar) method when true, otherwise an exception will be thrown. |
| [IsTimebased](/docs/desktop/barstype_istimebased) | Used to indicate the BarsType is built from time-based bars (day, minute, second). |
| [OnDataPoint()](/docs/desktop/ondatapoint) | OnDataPoint() method is where you should adjust data points (bar values) of your series through [AddBar()](/docs/desktop/addbar) and [UpdateBar()](/docs/desktop/updatebar). |
| [RemoveLastBar()](/docs/desktop/removelastbar) | Removes the last data point for the Bars Type. |
| [SessionIterator](/docs/desktop/barstype_sessioniterator) | Provides trading session information to the bars type. Must be built using the bars object. |
| [UpdateBar()](/docs/desktop/updatebar) | Updates a data point in our Bars Type. |

