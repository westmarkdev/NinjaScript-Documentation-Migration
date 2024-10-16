---
title: "Values"
pathName: /docs/desktop/performancemetric_values
---

## Definition

The Values array holds five values corresponding to each Cbi.PerformanceUnit. NinjaTrader will then access the Values property to display the calculated performance metric in the UI. You can also access these performance metrics for a NinjaScript strategy.

## Syntax

```csharp
public double[] Values { get; private set; }
```

## Calculating Values OnAddTrade Example

```csharp
protected override void OnAddTrade(Cbi.Trade trade)
{
    Values[(int)Cbi.PerformanceUnit.Currency] += trade.ProfitCurrency;
    Values[(int)Cbi.PerformanceUnit.Percent] = (1.0 + Values[(int)Cbi.PerformanceUnit.Percent]) * (1.0 + trade.ProfitPercent) - 1;
    Values[(int)Cbi.PerformanceUnit.Pips] += trade.ProfitPips;
    Values[(int)Cbi.PerformanceUnit.Points] += trade.ProfitPoints;
    Values[(int)Cbi.PerformanceUnit.Ticks] += trade.ProfitTicks;
}

// The attribute determines the name of the performance value on the grid
[Display("MyPerformanceMetric", Order = 0)]
public double[] Values { get; private set; }
```

## Calculating Values On Demand Example

```csharp
// The attribute determines the name of the performance value on the grid
[Display("MyPerformanceMetric", Order = 0)]
public double[] Values
{
    get
    {
        return /*Your custom math here*/;
    }
    private set;
}
```

