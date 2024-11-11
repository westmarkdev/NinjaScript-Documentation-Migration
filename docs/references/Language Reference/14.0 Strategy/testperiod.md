---
section: references
status: imported
parent: strategy
title: TestPeriod
pathName: testperiod
---

## Definition

Reserved for **Walk-Forward Optimization**, this property determines the number of days used for the "out of sample" backtest period for a given strategy. See also **OptimizationPeriod**.

{% callout type="note" %}

This property should ONLY be called from the **OnStateChange()** method during State.SetDefaults.

{% /callout %}

## Property Value

An **int** value representing the number of "out of sample" days used for walk-forward optimization; Default value is set to 28.

## Syntax

**TestPeriod**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {         
        //set the default TestPeriod to 31 days for WFOs
        TestPeriod = 31;
    }
}
```
