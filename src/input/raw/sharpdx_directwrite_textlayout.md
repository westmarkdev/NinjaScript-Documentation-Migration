










 


SharpDX.DirectWrite.TextLayout







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_directwrite_textlayout.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.DirectWrite](sharpdx_directwrite.htm) &gt;
SharpDX.DirectWrite.TextLayout | [Previous page](sharpdx_directwrite_linemetrics.htm)
[Return to chapter overview](sharpdx_directwrite.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


The TextLayout interface represents a block of text after it has been fully analyzed and formatted.


(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd316718.aspx))


 




|  |
| --- |
| Note: To draw a formatted string represented by an TextLayout object, Direct2D provides the DrawTextLayout method. |



 


Syntax
------


class TextLayout


 
Constructors
--------------




|  |  |
| --- | --- |
| new TextLayout(Factory factory, string text, [TextFormat](sharpdx_directwrite_textformat.htm) textFormat, float maxWidth, float maxHeight) | Takes a string, text format, and associated constraints, and produces an object that represents the fully analyzed and formatted result.  |







|  |
| --- |
| Tip: For NinjaScript development purposes, when creating a TextLayout object you should use the [NinjaTrader.Core.Globals.DirectWriteFactory](directwritefactory.htm) property |





Methods and Properties
----------------------




|  |  |
| --- | --- |
| [Dispose()](sharpdx_disposebase_dispose.htm) | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.htm).) |
| [FlowDirection](sharpdx_directwrite_textformat_flowdirection.htm) | Gets or sets the direction that text lines flow. (Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [FontFamilyName](sharpdx_directwrite_textformat_fontfamilyname.htm) | Gets a copy of the font family name.(Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [FontSize](sharpdx_directwrite_textformat_fontsize.htm) | Gets the font size in DIP unites. (Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [FontStretch](sharpdx_directwrite_textformat_fontstretch.htm) | Gets the font stretch of the text. (Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [FontStyle](sharpdx_directwrite_textformat_fontstyle.htm) | Gets the font style of the text. (Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [FontWeight](sharpdx_directwrite_textformat_fontweight.htm) | Gets the font weight of the text. (Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [IsDisposed](sharpdx_disposebase_isdisposed.htm) | Gets a value indicating whether this instance is disposed. (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.htm).) |
| [MaxHeight](sharpdx_directwrite_textlayout_maxheight.htm) | Gets or sets the layout maximum height.  |
| [MaxWidth](sharpdx_directwrite_textlayout_maxwidth.htm) | Gets or sets the layout maximum width.  |
| [Metrics](sharpdx_directwrite_textlayout_metrics.htm) | Contains the metrics associated with text after layout. All coordinates are in device independent pixels (DIPs). |
| [ParagraphAlignment](sharpdx_directwrite_textformat_paragraphalignment.htm) | Gets or sets the alignment option of a paragraph which is relative to the top and bottom edges of a layout box.(Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [ReadingDirection](sharpdx_directwrite_textformat_readingdirection.htm) | Gets or sets the current reading direction for text in a paragraph.
(Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [TextAlignment](sharpdx_directwrite_textformat_textalignment.htm) | Gets or sets the alignment option of text relative to the layout box's leading and trailing edge. (Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |
| [WordWrapping](sharpdx_directwrite_textformat_wordwrapping.htm) | Gets or sets the word wrapping option.
(Inherited from [TextFormat](sharpdx_directwrite_textformat.htm).) |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



