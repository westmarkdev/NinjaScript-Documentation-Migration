---
title: "SharpDX.DirectWrite.TextLayout.Metrics"
pathName: /docs/desktop/sharpdx_directwrite_textlayout_metrics
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Contains the metrics associated with text after layout. All coordinates are in device independent pixels (DIPs).

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd368135.aspx))

## Syntax

## <textlayout>.Metrics

## Properties

|  |  |
| --- | --- |
| Left |  A float value that indicates the left-most point of formatted text relative to the layout box, while excluding any glyph overhang. |
| Top | A float value that indicates the top-most point of formatted text relative to the layout box, while excluding any glyph overhang. |
| Width | A float value that indicates the width of the formatted text, while ignoring trailing whitespace at the end of each line. |
| WidthIncludingTrailingWhitespace |  A float value that indicates the width of the formatted text, taking into account the trailing whitespace at the end of each line. |
| Height |  A float value that indicates the height of the formatted text. The height of an empty string is set to the same value as that of the default font. |
| LayoutWidth | A float value that indicates the initial width given to the layout. It can be either larger or smaller than the text content width, depending on whether the text was wrapped. |
| LayoutHeight | A float value that indicates the initial height given to the layout. Depending on the length of the text, it may be larger or smaller than the text content height. |
| MaxBidiReorderingDepth | An int value representing the maximum reordering count of any line of text, used to calculate the most number of hit-testing boxes needed. If the layout has no bidirectional text, or no text at all, the minimum level is 1. |
| LineCount |  An int value representing total number of lines. |
