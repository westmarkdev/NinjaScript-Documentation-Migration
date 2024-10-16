---
title: "GetInitialLookBackDays()"
pathName: /docs/getinitiallookbackdays
---

## Definition

Determines how many days of data load when a user makes a "bars back" data request.

## Method Return Value

This method returns an `int` value.

## Method Parameters

|  |  |
| --- | --- |
| barsPeriod | The [Bars Period](/docs/desktop/barsperiod) chosen by the user when utilizing this Bars type |
| tradingHours | The [Trading Hours](/docs/desktop/tradinghours) chosen by the user when utilizing this Bars type |
| barsBack | The bars back chosen by the user when utilizing this Bars type |

## Syntax

```csharp
// You must override the method in your Bars Type with the following syntax.
public override int GetInitialLookBackDays(BarsPeriod barsPeriod, TradingHours tradingHours, int barsBack)
{

}
```

## Examples

```csharp
public override int GetInitialLookBackDays(BarsPeriod barsPeriod, TradingHours tradingHours, int barsBack)
{
    // Returns the minimum number of days needed to successfully load the number
    // of bars back requested for a monthly Bars type
    return (int) barsPeriod.Value * barsBack * 31;
}
```

{% callout type="tip" %}
Tip: Try to request an amount of data that is just right for what is needed. Requesting too large a data set will result in unnecessary data being loaded. Requesting too small a data set will result in multiple requests being done.
{% /callout %}
