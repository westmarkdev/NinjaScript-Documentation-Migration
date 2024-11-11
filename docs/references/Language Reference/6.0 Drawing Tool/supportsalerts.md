---
title: SupportsAlerts
pathName: supportsalerts
parent: drawing_tools
status: imported
section: references
---

## Definition

Determines if the drawing tool can be used for manually configured alerts through the UI.

## Property Value

A bool which when true determines that user can setup an alert based off this drawing tool; otherwise false.

{% callout type="note" %}

This property is false by default and MUST be overridden upon initialization to allow for manually configured alerts. You cannot set this during run-time.

{% /callout %}

## Syntax

**SupportsAlerts**

You may choose to override this property using the following syntax:

**public override bool SupportsAlerts**

## Examples

```csharp
public override bool SupportsAlerts { get { return true; } }
```
