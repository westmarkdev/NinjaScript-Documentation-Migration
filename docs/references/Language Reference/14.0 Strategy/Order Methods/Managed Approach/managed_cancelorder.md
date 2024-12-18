---
title: CancelOrder()
pathName: cancelorder
parent: managed_approach
section: references
status: imported
---

## Definition

Cancels a specified order. This method is reserved for experienced programmers that fully understand the concepts of advanced order handling.

{% callout type="note" %}

Notes:

1. This method sends a cancel request to the broker and does not guarantee that an order is completely cancelled. Most of the time you can expect your order to come back 100% cancelled.
2. An order can be completely filled or part filled in the time that you send the cancel request and the time the exchange receives the request. Check the **OnOrderUpdate()** method for the state of an order you attempted to cancel.
{% /callout %}

## Syntax

**CancelOrder(Order order)**

{% callout type="warning" %}

Warning: If you have existing historical **order** references which have transitioned to real-time, you MUST update the order object reference to the newly submitted real-time order; otherwise errors may occur as you attempt to cancel the order. You may use the **GetRealtimeOrder()** helper method to assist in this transition.

{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **order**
* An **Order** object representing the order you wish to cancel.

{% /table %}

## Examples

```csharp
private Order myEntryOrder = null;
private int barNumberOfOrder = 0;

protected override void OnBarUpdate()
{
    // Submit an entry order at the low of a bar
    if (myEntryOrder == null)
    {
        // use 'live until canceled' limit order to prevent default managed order handling which would expire at end of bar
        EnterLongLimit(0, true, 1, Low[0], "Long Entry");
        barNumberOfOrder = CurrentBar;
    }

    // If more than 5 bars has elapsed, cancel the entry order
    if (CurrentBar > barNumberOfOrder + 5)
        CancelOrder(myEntryOrder);
}

protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled,
    double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
    // Assign entryOrder in OnOrderUpdate() to ensure the assignment occurs when expected.
    // This is more reliable than assigning Order objects in OnBarUpdate, as the assignment is not guaranteed to be complete if it is referenced immediately after submitting
    if (order.Name == "Long Entry")
        myEntryOrder = order;

    // Evaluates for all updates to myEntryOrder.
    if (myEntryOrder != null && myEntryOrder == order)
    {
        // Check if myEntryOrder is cancelled.
        if (myEntryOrder.OrderState == OrderState.Cancelled)
        {
            // Reset myEntryOrder back to null
            myEntryOrder = null;
        }
    }
}
```
