---
title: Instrument
pathName: instrument
parent: position
section: references
status: imported
---

## Definition

Gets the instrument of a strategy position.

## Property Value

An **Instrument** representing the position's instrument.

## Syntax

**Position.Instrument**

## Examples

```csharp
protected override void OnPositionUpdate(Position position, double averagePrice, int quantity, MarketPosition marketPosition)
{
     // If the position is an AAPL position
     if (position.Instrument.MasterInstrument.Name == "AAPL")
   {
         //do something
   }
}

```
