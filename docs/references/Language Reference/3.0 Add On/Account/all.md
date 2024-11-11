---
title: All
pathName: all
parent: account
section: references
status: imported
---

## Definition

A collection of Account objects

## Property Value

A Collection of Account objects

## Syntax

**Accounts.All**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.DataLoaded)
    {
        foreach (Account sampleAccount in Account.All)
        Print(String.Format("The account {0} has a {1} unit FX lotsize set", sampleAccount.Name, sampleAccount.ForexLotSize));
    }
}
```
