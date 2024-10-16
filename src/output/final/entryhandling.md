---
title: "EntryHandling"
pathName: /docs/desktop/entryhandling
---

## Definition

Sets the manner in how entry orders will handle.

{% callout type="note" %}
This property ONLY applies to Managed order methods. When [IsUnmanaged](/docs/desktop/isunmanaged) is set to true, Entry Handling properties will be hidden from the UI.
{% /callout %}

## Property Value

An enum which sets how the entry orders are handled. Default value is `EntryHandling.AllEntries`. Possible values include:

|  |  |
| --- | --- |
| EntryHandling.AllEntries | NinjaScript will process all [order entry methods](/docs/desktop/order_methods) until the maximum allowable entries set by the [EntriesPerDirection](/docs/desktop/entriesperdirection) property is reached while in an open position. |
| EntryHandling.UniqueEntries | NinjaScript will process order entry methods until the maximum allowable entries set by the [EntriesPerDirection](/docs/desktop/entriesperdirection) property per each uniquely named entry. |

{% callout type="warning" %}
This property should ONLY be set from the [OnStateChange()](/docs/desktop/onstatechange) method during State.SetDefaults or State.Configure.
{% /callout %}

## Syntax

`EntryHandling`

## Examples

## Allow a maximum of two entries while a position is open

```csharp
// Example #1
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        EntriesPerDirection = 2;
        EntryHandling = EntryHandling.AllEntries;
    }
}

protected override void OnBarUpdate()
{
    if (CrossAbove(SMA(10), SMA(20), 1))
        EnterLong("SMA Cross Entry");
}
```

## EnterLong() will be processed once for each uniquely named entry.

```csharp
// Example #2
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        EntriesPerDirection = 1;
        EntryHandling = EntryHandling.UniqueEntries;
    }
}

protected override void OnBarUpdate()
{
    if (CrossAbove(SMA(10), SMA(20), 1))
        EnterLong("SMA Cross Entry");
    if (CrossAbove(RSI(14, 3), 30, 1))
        EnterLong("RSI Cross Entry");
}
```

