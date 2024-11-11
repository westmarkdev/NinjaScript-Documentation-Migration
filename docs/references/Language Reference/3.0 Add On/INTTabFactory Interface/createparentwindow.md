---
title: CreateParentWindow()
pathName: createparentwindow
parent: inttabfactory_interface
section: references
status: imported
---

This determines which **NTWindow** is created as the parent window for our Add On.

## Examples

```csharp
// INTTabFactory member. Creates the parent window that contains tabs
public NTWindow CreateParentWindow()
{
     return new MyWindow();
}
```
