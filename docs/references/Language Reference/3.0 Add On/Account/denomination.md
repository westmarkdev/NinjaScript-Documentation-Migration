---
title: Denomination
pathName: denomination
parent: account
section: references
status: imported
---

## Definition

Indicates the currency set on an account

## Property Value

A Currency object containing information about the currency denomination specified in the referenced account

## Syntax

`account`>.**Connection**

## Examples

```csharp
private Account myAccount;

protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Initialize myAccount here

        // Print myAccount's currency denomination
        NinjaTrader.Code.Output.Process("myAccount currency is set to " + myAccount.Denomination, PrintTo.OutputTab1);
    }
}
```
