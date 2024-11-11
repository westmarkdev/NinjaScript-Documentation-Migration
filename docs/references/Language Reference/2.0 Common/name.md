---
title: Name
pathName: name
parent: common
section: references
status: review
---

## Definition

Determines the listed name of the NinjaScript object.

## Property Value

A **string** value.

## Syntax

**Name**

## Examples

```csharp
protected override void OnStateChange()
{
   
   if (State == State.SetDefaults)
   {
     Name                 = "Examples indicator";
     Description           = @"An example of an indicator used for documentation purposes";      
   }
```
