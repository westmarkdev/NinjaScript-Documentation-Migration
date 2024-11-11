---
title: CancelAllOrders()
pathName: cancelallorders
parent: account
order: 0
status: imported
section: references
---

## Definition

Cancels all [Order](order) of an instrument.

## Syntax

**CancelAllOrders(Instrument instrument)**

## Parameters

{% table %}

* instrument

---

* Instrument of the orders to be cancelled
{% /table %}

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
