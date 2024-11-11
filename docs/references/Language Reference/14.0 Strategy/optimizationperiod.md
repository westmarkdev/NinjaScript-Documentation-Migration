---
title: OptimizationPeriod
pathName: optimizationperiod
parent: strategy
section: references
status: imported
---

## Definition

Reserved for **Walk-Forward Optimization**, this property determines the number of days used for the "in sample" backtest period for a given strategy. See also **TestPeriod**.

{% callout type="note" %}

This property should ONLY be called from the **OnStateChange()** method during State.SetDefaults.

{% /callout %}

## Property Value

An **int** value representing the number of "in sample" days used for walk-forward optimization; Default value is set to 10.

## Syntax

**OptimizationPeriod**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {         
        //set the default optimization period to 20 days for WFOs
        OptimizationPeriod = 20;
    }
}
```
