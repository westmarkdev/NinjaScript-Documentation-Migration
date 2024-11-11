---
title: Instrument
pathName: instrument
parent: positionaccount
section: references
status: imported
---

## Definition

Gets the instrument of an account position.

## Property Value

An **Instrument** representing the account's instrument position.

## Syntax

**PositionAccount.Instrument**

## Examples

```csharp

protected override void OnPositionUpdate(Position position, double averagePrice, int quantity, MarketPosition marketPosition)
{
     // If the position is an AAPL position
     if (PositionAccount.Instrument.MasterInstrument.Name == "AAPL")
   {
         //do something
   }
}
```
