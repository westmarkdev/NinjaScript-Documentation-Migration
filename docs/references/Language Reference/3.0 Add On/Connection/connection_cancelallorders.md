---
title: CancelAllOrders()
pathName: cancelallorders
parent: connection_class
section: references
status: imported
---

## Definition

Cancels all orders for the specified instrument on the connection.

## Syntax

**<`connection`>.CancelAllOrders(Instrument instrument)**

{% table %}

* instrument
* An Instrument object used to identify the instrument for which to cancel orders
{% /table %}

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
    // Cancel all orders if an execution is triggered after 9pm
    if (e.Time > new DateTime(now.Year, now.Month, now.Day, 21, 0, 0))
        myAccount.CancelAllOrders(e.Execution.Instrument);
}
```
