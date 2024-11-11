---
title: IsUserDrawn
pathName: isuserdrawn
parent: drawing_tools
status: imported
section: references
---

## Definition  

Indicates if the drawing tool was manually drawn by a user as opposed to programmatically drawn by a **NinjaScript** object (such as an indicator or strategy).

## Property Value

A bool value which when true if the draw object was manually drawn; otherwise false. This property is read-only.

## Syntax

**IsUserDrawn**

## Examples

```csharp
if (IsUserDrawn)
{
// do something only if the object was drawn manually
}
```
