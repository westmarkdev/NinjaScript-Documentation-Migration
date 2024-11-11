---
title: Executions
pathName: executions
parent: account
section: references
status: imported
---

## Definition

A collection of Execution objects generated for the specified account. These are the current sessions executions and should match executions reported in the Executions tab of the NinjaTrader Account Data window.

## Property Value

An **Collection** of Execution objects

## Syntax

**<`account`>.Executions**

{% callout type="note" %}

At this time there is not a supported method to retrieve historical executions from the local database.

{% /callout %}

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

private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
    foreach (Execution execution in myAccount.Executions)
    {
        Print(String.Format("Execution triggered for Order {0}", execution.Order));
    }
}
```
