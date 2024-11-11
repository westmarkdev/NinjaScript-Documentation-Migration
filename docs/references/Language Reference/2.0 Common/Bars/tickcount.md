---
section: references
title: TickCount
pathName: tickcount
parent: bars
status: review
---

## Definition

Returns the total number of ticks of the current bar processing.

{% callout type="note" %}

Note: For historical usage, you must use **Calculate.OnEachTick** with [**TickReplay**](developing_for_tick_replay.md) enabled; otherwise a value of 1 will be returned.

{% /callout %}

## Property Value

A long value that represents the total number of ticks of the current bar.

## Syntax

**Bars.TickCount**

## Examples

```csharp
// Prints the tick count to the output window
Print("The tick count of the current bar is " + **Bars.TickCount**.ToString());
```
