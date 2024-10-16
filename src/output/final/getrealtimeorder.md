---
title: "GetRealtimeOrder()"
pathName: /docs/desktop/getrealtimeorder
---

## Definition

Returns a matching real-time order object based on a specified historical order object reference.

{% callout type="note" %}
This method is only needed if you have historical order references which you wish to transition and manage in real-time (i.e., you had a working order which was submitted historically and re-submitted in real-time as the strategy is enabled). This method only needs to be called once per order object, and should be done in `OnOrderUpdate` to handle all scenarios. Please see the [Advanced Order Handling](/docs/desktop/advanced_order_handling) section on transition orders for more details.
{% /callout %}

## Method Return Value

Returns a real-time [order](/docs/desktop/order) reference associated with the historical order object. If no associated order exists (i.e. OrderState is Filled, Canceled, Rejected, Unknown), a null value returns.

### Syntax

```csharp
GetRealtimeOrder(Order historicalOrder)
```

## Parameters

|  |  |
| --- | --- |
| historicalOrder | The historical [order](/docs/desktop/order) object to update to real-time |

## Examples

```csharp
private Order myOrder;

protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
    // One time only, as we transition from historical
    // Convert any old historical order object references to the live order submitted to the real-time account
    if (myOrder != null && myOrder.IsBacktestOrder && State == State.Realtime)
        myOrder = GetRealtimeOrder(myOrder);
    
    // Assign Order objects here
    // This is more reliable than assigning Order objects in OnBarUpdate, as the assignment is not guaranteed to be complete if it is referenced immediately after submitting
    if (order.Name == "myOrder Signal Name")
        myOrder = order;
    
    // Null Entry order if filled or cancelled. We do not use the Order objects after the order is filled, so we can null it here
    if (myOrder != null && myOrder == order)
    {
        if (order.OrderState == OrderState.Cancelled && order.Filled == 0)
            myOrder = null;
        if (order.OrderState == OrderState.Filled)
            myOrder = null;
    }
}
```
