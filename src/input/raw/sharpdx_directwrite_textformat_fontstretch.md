










 


SharpDX.DirectWrite.TextFormat.FontStretch







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_directwrite_textformat_fontstretch.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.DirectWrite](sharpdx_directwrite.htm) &gt; [TextFormat](sharpdx_directwrite_textformat.htm) &gt;
SharpDX.DirectWrite.TextFormat.FontStretch | [Previous page](sharpdx_directwrite_textformat_fontsize.htm)
[Return to chapter overview](sharpdx_directwrite_textformat.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Gets the font stretch of the text. 


(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316646.aspx))


 




|  |
| --- |
| Note:  
1.A font stretch describes the degree to which a font form is stretched from its normal aspect ratio, which is the original width to height ratio specified for the glyphs in the font.2.Values other than the ones defined in the enumeration are considered to be invalid, and are rejected by font API functions. |



 


 


Property Value
--------------


A SharpDX.DirectWrite.FontStretch enum value which indicates the type of font stretch (such as normal or condensed).  See table below


 


Syntax
------


<textlayout>.FontStretch
------------------------



Possible values are:




|  |  |
| --- | --- |
| Undefined | Predefined font stretch : Not known (0). |
| UltraCondensed | Predefined font stretch : Ultra-condensed (1). |
| ExtraCondensed | Predefined font stretch : Extra-condensed (2). |
| Condensed | Predefined font stretch : Condensed (3). |
| SemiCondensed | Predefined font stretch : Semi-condensed (4). |
| Normal | Predefined font stretch : Normal (5). |
| Medium | Predefined font stretch : Medium (5). |
| SemiExpanded | Predefined font stretch : Semi-expanded (6). |
| Expanded | Predefined font stretch : Expanded (7). |
| ExtraExpanded | Predefined font stretch : Extra-expanded (8). |
| UltraExpanded | Predefined font stretch : Ultra-expanded (9). |






 
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