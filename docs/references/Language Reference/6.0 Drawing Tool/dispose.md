---
title: Dispose()
pathName: dispose
parent: drawing_tools
status: imported
section: references
---

## Definition

Releases any device resources used for the drawing tool.

## Method Return Value

This method does not return a value.

## Syntax

Dispose()

## Method Parameters

This method does not accept any parameters.

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name                 = @"My Drawing Tool";
   }

   else if (State == State.Terminated)
     Dispose();
}
```
