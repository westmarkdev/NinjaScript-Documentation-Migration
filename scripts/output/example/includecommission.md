---

title: includecommission
pathName: includecommission
created: Thursday, October 3rd 2024, 11:24:37 am
updated: Thursday, October 3rd 2024, 12:16:54 pm
---

## Definition

Determines if the strategy performance results will include commission on a historical backtest. When true, the [Commission Template](understanding_commissions.htm) applied to the account on which the strategy is running will be used.

## Property Value

A bool value which returns true if the strategy includes commission on a historical backtest; otherwise, false. Default value is set to false.

|  |  |
| --- | --- |
| **Warning:** This property should ONLY be set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |

## Syntax

```csharp
IncludeCommission
```

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
