---
title: DirectWriteFactory
pathName: directwritefactory
parent: rendering
section: references
status: review
---

## Definition

Provides a default **DirectWrite** factory used for creating [**SharpDX.DirectWrite**](sharpdx_directwrite) components.

## Property Value

A read-only **SharpDX.DirectWrite.Factory** used to create DirectWrite objects compatible with **NinjaTrader** rendering.

## Syntax

**NinjaTrader.Core.Globals.DirectWriteFactory**

## Examples

```csharp
// create a text format object with default NinjaTrader DirectWrite factory

SharpDX.DirectWrite.TextFormat textFormat = new SharpDX.DirectWrite.TextFormat(NinjaTrader.Core.Globals.DirectWriteFactory,
   "Arial", 12f);

// create a text layout object with default NinjaTrader DirectWrite factory

SharpDX.DirectWrite.TextLayout textLayout = new SharpDX.DirectWrite.TextLayout(NinjaTrader.Core.Globals.DirectWriteFactory,

   "text to render", textFormat, ChartPanel.W, ChartPanel.H);
```
