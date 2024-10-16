---
title: "PartialHolidays"
pathName: /docs/desktop/partialholidays
---

## Definition

A collection of partial holidays which are configured for a Trading Hours template. Holidays are days which fall outside of the normal trading schedule, on which data will be excluded. For more information please see the "Understanding trading holidays" section of the [Using the Trading Hours](/docs/desktop/using_the_trading_hours_window) window.

## Property Value

A [Dictionary](https://msdn.microsoft.com/en-us/library/xfhwa508(v=vs.110).aspx) holding a collection of holiday Dates and PartialHoliday objects for each partial holiday.

|  |  |
| --- | --- |
| Date | A DateTime representing the trading date of the Trading Hours holiday |
| PartialHoliday | An object containing a DateTime representing the date of the early close or late begin, a description of the partial holiday, and two bool properties, IsEarlyClose and IsLateBegin |

## Syntax

`TradingHours.PartialHolidays`

## Examples

```csharp
// Print all partial holidays included in the Bars object's Trading Hours template
foreach(KeyValuePair<DateTime, PartialHoliday> holiday in TradingHours.PartialHolidays)
{
    Print(holiday);
}
```
