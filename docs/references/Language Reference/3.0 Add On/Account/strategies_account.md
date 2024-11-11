---
title: Strategies
pathName: strategies
parent: account
section: references
status: imported
---

## Definition

A collection of **StrategyBase** objects generated for the specified account

## Property Value

An [Collection](https://msdn.microsoft.com/en-us/library/ms132397(v=vs.110).aspx) of **StrategyBase** objects

## Syntax

**<`account`>.Strategies**

## Examples

```csharp
private Account myAccount;

protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Initialize myAccount
    }
}

private void OnAccountStatusUpdate(object sender, AccountStatusEventArgs e)
{
    foreach (StrategyBase strategy in myAccount.Strategies)
    {
        Print(String.Format("Account status updated. {0} strategy applied with position {1}", strategy.Name, strategy.Position));
    }
}
```
