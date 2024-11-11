---
title: Holidays
pathName: holidays
parent: tradinghours
section: references
status: review
---

## Definition

A collection of full holidays configured for a Trading Hours template. Holidays are days which fall outside of the regular trading schedule.

{% callout type="note" %}

For more information please see the "Understanding trading holidays" section of the [Using the Trading Hours](using_the_trading_hours_window) window.

{% /callout %}

## Property Value

A **Dictionary** holding a collection of holiday Dates and Descriptions of each holiday.

{% table %}

* Date
* Description

---

* A **DateTime** representing the date of the trading hours holiday
* A string which is used to describe the holiday (e.g., Christmas)
{% /table %}

## Syntax

**TradingHours.Holidays**

## Examples

```csharp
// Print all holidays included in the Bars object's Trading Hours template
foreach(KeyValuePair<datetime, string> holiday in TradingHours.Holidays)
{
    Print(holiday);
}
```
