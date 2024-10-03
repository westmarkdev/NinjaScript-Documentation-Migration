---
title: accounts_cancelallorders
path: cancelallorders
created: Thursday, October 3rd 2024, 11:49:35 am
updated: Thursday, October 3rd 2024, 12:16:55 pm
---

## Definition

Cancels all [Order](order.htm)s of an instrument.

## Syntax

```csharp
CancelAllOrders(Instrument instrument)
```

## Parameters

|  |  |
| --- | --- |
| instrument | Instrument of the orders to be cancelled |

## Example

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
    // Cancel all orders if an execution is triggered after 9pm
    if (e.Time > new DateTime(now.Year, now.Month, now.Day, 21, 0, 0))
        myAccount.CancelAllOrders(e.Execution.Instrument);
}
```

{% callout type="note" %}  
Ensure that your logic around execution updates accounts for the current time to prevent unintended order cancellations.  
{% /callout %}
