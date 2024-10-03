---
path: includecommission
title: IncludeCommission
---

## Definition

Determines if the strategy performance results will include commission on a historical backtest. When true, the [Commission Template](understanding_commissions) applied to the account on which the strategy is running will be used.

## Property Value

A bool value which returns true if the strategy includes commission on a historical backtest; otherwise, false.  Default value is set to false.

{% callout type="warning" %}
This property should ONLY bet set from the [OnStateChange()](onstatechange) method during State.SetDefaults or State.Configure

{% /callout %}

## Syntax

`IncludeCommission`

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IncludeCommission = true;
    }
}
```
