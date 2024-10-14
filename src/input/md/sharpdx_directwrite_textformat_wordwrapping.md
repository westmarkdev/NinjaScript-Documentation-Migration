










 


SharpDX.DirectWrite.TextFormat.WordWrapping







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_directwrite_textformat_wordwrapping.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.DirectWrite](sharpdx_directwrite.htm) &gt; [TextFormat](sharpdx_directwrite_textformat.htm) &gt;
SharpDX.DirectWrite.TextFormat.WordWrapping | [Previous page](sharpdx_directwrite_textformat_textalignment.htm)
[Return to chapter overview](sharpdx_directwrite_textformat.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Gets or sets the word wrapping option. 


(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316688.aspx))


 


Property Value
--------------


The SharpDX.DirectWrite.WordWraping enum value which determines the word wrapping option. 


 


Possible values are:




|  |  |
| --- | --- |
| Wrap | Indicates that words are broken across lines to avoid text overflowing the layout box. |
| NoWrap | Indicates that words are kept within the same line even when it overflows the layout box. This option is often used with scrolling to reveal overflow text. |



 


Syntax
------


<textlayout>.WordWrapping
-------------------------





 
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