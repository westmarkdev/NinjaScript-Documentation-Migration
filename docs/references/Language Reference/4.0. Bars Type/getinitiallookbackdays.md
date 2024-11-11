---
title: GetInitialLookBackDays()
pathName: getinitiallookbackdays
parent: bars_type
status: imported
section: references
---

## Definition

Determines how many days of data load when a user makes a "bars back" data request.

## Method Return Value

This method returns An **int** value.

## Method Parameters

{% table %}

---

* **barsPeriod**
* The [bars period](barsperiod) chosen by the user when utilizing this Bars type

---

* **tradingHours**
* The [trading hours](tradinghours) chosen by the user when utilizing this Bars type

---

* **barsBack**
* The bars back chosen by the user when utilizing this Bars type
{% /table %}

## Syntax

You must override the method in your Bars Type with the following syntax.

**public override int GetInitialLookBackDays(BarsPeriod barsPeriod, TradingHours tradingHours, int barsBack)**

## Examples

```csharp
public override int GetInitialLookBackDays(BarsPeriod barsPeriod, TradingHours tradingHours, int barsBack)
{
     // Returns the minimum number of days needed to successfully load the number
     // of bars back requested for a monthly Bars type
     return (int) barsPeriod.Value * barsBack * 31;
}
```

{% callout type="note" %}

Tip: Try to request an amount of data that is just right for what is needed. Requesting too large a data set will result in unnecessary data being loaded. Requesting too small a data set will result in multiple requests being done.
{% /callout %}
