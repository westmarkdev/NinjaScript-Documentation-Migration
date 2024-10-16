---
title: "GetPercentComplete()"
pathName: /docs/desktop/getpercentcomplete
---

## Definition

Determines the value your BarsType would return for [Bars.PercentComplete](/docs/desktop/percentcomplete).

## Method Return Value

This method returns a double value.

## Method Parameters

|  |  |
| --- | --- |
| bars | The [Bars](/docs/desktop/bars) object chosen by the user when utilizing this Bars type. |
| now | The DateTime value to measure. |

## Syntax

You must override the method in your Bars Type with the following syntax.

```csharp
public override double GetPercentComplete(Bars bars, DateTime now)
{

}
```

## Examples

```csharp
public override double GetPercentComplete(Bars bars, DateTime now)
{
    // Calculate the percent complete for our monthly bars
    if (now.Date <= bars.LastBarTime.Date)
    {
        int month = now.Month;
        int daysInMonth = (month == 2) ? (DateTime.IsLeapYear(now.Year) ? 29 : 28) :
        (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 ? 31 : 30);
        return (daysInMonth - (bars.LastBarTime.Date.AddDays(1).Subtract(now).TotalDays / bars.BarsPeriod.Value)) /
        daysInMonth; // an estimate
    }
    return 1;
}
```
