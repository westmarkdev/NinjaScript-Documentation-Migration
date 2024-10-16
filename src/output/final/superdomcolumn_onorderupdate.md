---
title: "OnOrderUpdate()"
pathName: /docs/desktop/superdomcolumn_onorderupdate
---

## Definition

Called every time an [order](/docs/desktop/order) changes state. An order will change state when a change in order quantity, price or state (e.g. working to filled) occurs.

{% callout type="note" %}
The OnOrderUpdate() method is called on ALL order updates (e.g., any account and instrument combination) and NOT just the specific items which are selected in the SuperDOM.
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
protected override void OnOrderUpdate(OrderEventArgs orderUpdate)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| orderUpdate | An `OrderEventArgs` representing the change in order state |

## Examples

```csharp
protected override void OnOrderUpdate(OrderEventArgs orderUpdate)
{
    // Do not take action if the order update does not come from the selected SuperDOM instrument/account
    if (orderUpdate.Order.Instrument != SuperDom.Instrument || orderUpdate.Order.Account != SuperDom.Account)
        return;
    // Do something
}
```
