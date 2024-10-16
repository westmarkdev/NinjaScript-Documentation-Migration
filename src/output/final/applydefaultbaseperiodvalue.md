---
title: "ApplyDefaultBasePeriodValue()"
pathName: /docs/desktop/applydefaultbaseperiodvalue
---

## Definition

Sets the default base values used for the [BarsPeriod](/docs/desktop/barsperiod) selected by the user (e.g., the default PeriodValue, DaysToLoad, etc.) for your custom Bar Type.

## Method Return Value

This method does not return a value.

## Parameters

|  |  |
| --- | --- |
| period | The [BarsPeriod](/docs/desktop/barsperiod) chosen by the user when utilizing this Bars type |

## Syntax

You must override the method in your Bars Type with the following syntax:

```csharp
public override void ApplyDefaultBasePeriodValue(BarsPeriod period)
{
}
```

## Examples

```csharp
public override void ApplyDefaultBasePeriodValue(BarsPeriod period)
{
    // sets the default Minute bars period value to 1, and days to load to 5
    if (period.BaseBarsPeriodType == BarsPeriodType.Minute)
    {
        period.BaseBarsPeriodValue = 1;
        DaysToLoad = 5;
    }
    // sets the default Tick bars period value to 150, and days to load to 3
    else if (period.BaseBarsPeriodType == BarsPeriodType.Tick)
    {
        period.BaseBarsPeriodValue = 150;
        DaysToLoad = 3;
    }
}
```

