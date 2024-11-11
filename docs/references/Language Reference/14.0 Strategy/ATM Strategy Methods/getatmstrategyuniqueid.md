---
title: GetAtmStrategyUniqueId()
pathName: getatmstrategyuniqueid
parent: atm_strategy_methods
section: references
status: review
---

## Definition

Generates a unique ATM Strategy ID value.

## Method Return Value

A **string** value representing a unique id value.

## Syntax

**GetAtmStrategyUniqueId()**

## Parameters

This method does not take any parameters.

## Examples

```csharp
protected override void OnBarUpdate()
{
    string orderId = GetAtmStrategyUniqueId();
}
```
