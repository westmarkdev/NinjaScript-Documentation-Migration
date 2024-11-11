---
title: MaxTimeToRecover
pathName: maxtimetorecover
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the maximum time to recover from a draw down.

## Property Value

A **TimeSpan** value that represents the maximum time to recover from a draw down.

## Syntax

<`tradecollection`>.TradesPerformance.**MaxTimeToRecover**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the maximum time to recover from a draw down
     Print("Max time to recover is: " + SystemPerformance.AllTrades.TradesPerformance.MaxTimeToRecover);

```
