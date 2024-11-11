---
title: OnRestoreValues()
pathName: onrestorevalues
parent: superdom_column
status: imported
section: references
---

## Definition

Called when the column is restored (e.g. from a workspace). All public properties in a SuperDOM Column are saved to the workspace upon closing and selecting save. You may choose to do something explicit with a certain property when the **OnRestoreValues()** method is called.

## Method Return Value

This method does not return a value.

## Syntax

You may override the method in your SuperDOM column with the following syntax:

**public override void OnRestoreValues()**

## Parameters

This method does not require any parameters.

## Examples

```csharp
public override void OnRestoreValues()
{
   // Do something with the restored values. Can also trigger a repaint via OnPropertyChanged()
}
```
