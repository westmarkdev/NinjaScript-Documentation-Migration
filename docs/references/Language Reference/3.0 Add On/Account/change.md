---
title: Change()
pathName: change
parent: account
section: references
status: imported
---

## Definition

Changes specified **Order** object(s).

## Syntax

Change(IEnumerable<`order`> orders)

## Parameters

{% table %}

* orders
* Order(s) to change
{% /table %}

## Examples

```csharp
// Example code
Order stopOrder;
stopOrder.StopPriceChanged = stopOrder.StopPrice - 4 * stopOrder.Instrument.MasterInstrument.TickSize;

private void OnExecutionUpdate(object sender, ExecutionEventArgs e)
{
    // Change the stop order if an execution results in a long position
    if(e.MarketPosition == MarketPosition.Long)
        myAccount.Change(new[] { stopOrder });
}
```
