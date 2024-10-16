---
title: "EntriesPerDirection"
pathName: /docs/desktop/entriesperdirection
---

## Definition

Determines the maximum number of entries allowed per direction while a position is active based on the [EntryHandling](/docs/desktop/entryhandling) property.

{% callout type="note" %}
This property ONLY applies to Managed order methods. When [IsUnmanaged](/docs/desktop/isunmanaged) is set to true, Entry Handling properties will be hidden from the UI.
{% /callout %}

## Property Value

An `int` value represents the maximum number of entries allowed. Default value is 1.

{% callout type="warning" %}
This property should ONLY be set from the [OnStateChange()](/docs/desktop/onstatechange) method during State.SetDefaults or State.Configure.
{% /callout %}

## Syntax

```csharp
EntriesPerDirection
```

## Examples

## If an open position already exists, subsequent `EnterLong()` calls are ignored

```csharp
// Example #1
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        EntriesPerDirection = 1;
        EntryHandling = EntryHandling.AllEntries;
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

## `EnterLong()` will be processed once for each uniquely named entry

```csharp
// Example #2
protected override void OnStateChange()
{
    EntriesPerDirection = 1;
    EntryHandling = EntryHandling.UniqueEntries;
}

protected override void OnBarUpdate()
{
    if (CrossAbove(SMA(10), SMA(20), 1))
        EnterLong("SMA Cross Entry");
    
    if (CrossAbove(RSI(14, 3), 30, 1))
        EnterLong("RSI Cross Entry");
}
```
