---
title: "CancelOrder()"
path: managed_cancelorder
---

## Definition

Cancels a specified order. This method is reserved for experienced programmers that fully understand the concepts of advanced order handling.

{% callout type="note" %}
This method sends a cancel request to the broker and does not guarantee that an order is completely cancelled. Most of the time you can expect your order to come back 100% cancelled. An order can be completely filled or part filled in the time that you send the cancel request and the time the exchange receives the request. Check the [OnOrderUpdate()](onorderupdate) method for the state of an order you attempted to cancel.
{% /callout %}

### Syntax

```csharp
CancelOrder(Order order)
```

{% callout warning %}
If you have existing historical [order](order) references which have transitioned to real-time, you MUST update the order object reference to the newly submitted real-time order; otherwise errors may occur as you attempt to cancel the order. You may use the [GetRealtimeOrder()](getrealtimeorder) helper method to assist in this transition.
{% /callout %}

## Parameters

| Parameter | Description |
| --- | --- |
| order | An [Order](order) object representing the order you wish to cancel. |

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
    // If more than 5 bars have elapsed, cancel the entry order
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

{% callout type="note" %}
Ensure to manage your orders properly to avoid unnecessary CPU cycle usage, and always check the state of your orders to confirm they are correctly handled.
{% /callout %}
