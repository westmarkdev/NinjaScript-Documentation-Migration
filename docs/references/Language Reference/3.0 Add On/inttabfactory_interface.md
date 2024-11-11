---
title: INTTabFactory Interface
pathName: inttabfactory_interface
parent: add_on
section: references
status: check
---

If you wish to have tab page functionality like adding, removing, moving, duplicating tabs you must create a class which implements the **INTTabFactory** interface.

This interface contains two methods which must be hidden:

## Syntax

**NTWindow CreateParentWindow()**
**NTTabPage CreateTabPage(string typeName, bool isNewWindow = false)**

## Examples

```csharp
public class MyWindowFactory : INTTabFactory
{
     // INTTabFactory member. Creates the parent window that contains tabs
     public NTWindow CreateParentWindow()
     {
         return new MyWindow();
     }

     // INTTabFactory member. Creates new tab pages whenever the user presses the + button
     public NTTabPage CreateTabPage(string typeName)
     {
         return new MyWindowTabPage();
     }
}
```
