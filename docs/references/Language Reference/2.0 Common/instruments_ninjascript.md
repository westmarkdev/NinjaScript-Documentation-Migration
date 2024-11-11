---
title: Instruments
pathName: instruments
parent: common
section: references
status: review
---

## Definition

A collection of **Instrument** objects currently used by a script.

## Property Value

An array of **Instrument** objects

## Syntax

**Instruments[]**

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.DataLoaded)
   {
       // Print all instruments which have been loaded
       foreach (Instrument i in Instruments)
       {
           Print(i.FullName);
       }
   }
}
```
