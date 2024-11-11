---
title: IgnoresUserInput
pathName: ignoresuserinput
parent: drawing_tools
status: imported
section: references
---

## Definition  

Determines if the drawing tool can be clicked on by the user.

## Property Value

A bool value which wen true if the drawing tool cannot not be interacted with by a user; otherwise false. Default is set to false.

## Syntax

**IgnoresUserInput**

## Examples

```csharp

protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
           IgnoresUserInput = true; // Set this to true to make the drawing object non-interactive
     }
     else if (State == State.Configure)
     {

     }
}
```
