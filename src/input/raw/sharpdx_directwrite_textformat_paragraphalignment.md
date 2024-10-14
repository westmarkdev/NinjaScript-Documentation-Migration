










 


SharpDX.DirectWrite.TextFormat.ParagraphAlignment







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_directwrite_textformat_paragraphalignment.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.DirectWrite](sharpdx_directwrite.htm) &gt; [TextFormat](sharpdx_directwrite_textformat.htm) &gt;
SharpDX.DirectWrite.TextFormat.ParagraphAlignment | [Previous page](sharpdx_directwrite_textformat_fontweight.htm)
[Return to chapter overview](sharpdx_directwrite_textformat.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Gets or sets the alignment option of a paragraph which is relative to the top and bottom edges of a layout box. 


(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316675.aspx))


 


Property Value
--------------


A SharpDX.DirectWrite.ParagraphAlignment enum value that indicates the current paragraph alignment option.


 


Possible values are:




|  |  |
| --- | --- |
| Near | The top of the text flow is aligned to the top edge of the layout box. |
| Far | The bottom of the text flow is aligned to the bottom edge of the layout box. |
| Center | The center of the flow is aligned to the center of the layout box. |



 


Syntax
------


<textlayout>.ParagraphAlignment
-------------------------------






 
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
 
 
 



</textlayout>