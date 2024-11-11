---
title: Account
pathName: account
parent: strategy
section: references
status: imported
---

## Definition

Represents the real-world or simulation **Account** configured for the strategy.

## Property Value

An [Account](account) object configured for the strategy.

## Syntax

**Account**

## Examples

```csharp
// Displays text on chart indicating what account the strategy is applied to
Draw.TextFixed(this, "tag1", "Strategy is applied to " + Account.Name, TextPosition.BottomRight);
```
