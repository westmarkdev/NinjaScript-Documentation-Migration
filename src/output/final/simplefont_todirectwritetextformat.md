---
title: "ToDirectWriteTextFormat()"
pathName: /docs/desktop/simplefont_todirectwritetextformat
---

## Definition

Converts a [SimpleFont](/docs/desktop/simplefont_class) object to a [SharpDX](/docs/desktop/sharpdx) compatible font which can be used for chart rendering.

{% callout type="note" %}
For more information please see the educational resource on [Using SharpDX for Custom Chart Rendering](/docs/desktop/using_sharpdx_for_custom_chart_rendering)
{% /callout %}

## Method Return Value

Returns a [DirectWrite.TextFormat](/docs/desktop/sharpdx_directwrite_textformat) object.

{% callout type="warning" %}
The returned DirectWrite.TextFormat object should be disposed of immediately when finished drawing text.
{% /callout %}

## Syntax

```csharp
<simplefont>.ToDirectWriteTextFormat()
```

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Set text to chart label simple font object
    SharpDX.DirectWrite.TextFormat textFormat = chartControl.Properties.LabelFont.ToDirectWriteTextFormat();
    // use the textFormat in a RenderTarget.DrawText() or DrawTextLayout() method
    // do not forget to dispose text format when finished
    textFormat.Dispose();
}
```
