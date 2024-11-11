---
title: Cancel
pathName: cancel
parent: account
section: references
status: imported
---

## Definition

Cancels specified **Order** object(s).

## Syntax

Cancel(IEnumerable<`order`> orders)

## Parameters

{% table %}

* orders
* Order(s) to cancel
{% /table %}

## Examples

```csharp
private Account myAccount;
Order stopOrder = null;

protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Initialize myAccount
    }
}

private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
    // Cancel the stop order if an execution results in a long position
    if(e.MarketPosition == MarketPosition.Long)
        myAccount.Cancel(new[] { stopOrder });
}
```
