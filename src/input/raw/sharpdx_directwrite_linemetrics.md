










 


SharpDX.DirectWrite.TextLayout.LineMetrics







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharpdx_directwrite_linemetrics.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [SharpDX SDK Reference](sharpdx_sdk_reference.htm) &gt; [SharpDX.DirectWrite](sharpdx_directwrite.htm) &gt;
SharpDX.DirectWrite.TextLayout.LineMetrics | [Previous page](sharpdx_directwrite_textformat_wordwrapping.htm)
[Return to chapter overview](sharpdx_directwrite.htm)












|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference.htm) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |



 


 


Definition
----------


Contains information about a formatted line of text.


(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd368099(v=vs.85).aspx))


 


Syntax
------


LineMetrics[int idx]



Properties
----------




|  |  |
| --- | --- |
| Baseline | A float for the distance from the top of the text line to its baseline. |
| Height | A float for the height of the text line. |
| IsTrimmed | A bool indicating the line is trimmed. |
| Length |  An int value for the number of text positions in the text line. This includes any trailing whitespace and newline characters. |
| NewlineLength | An int value for the number of characters in the newline sequence at the end of the text line. If the count is zero, then the text line was either wrapped or it is the end of the text. |
| TrailingWhitespaceLength | Ant int value for the number of whitespace positions at the end of the text line. Newline sequences are considered whitespace.
  |






 
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
 
 
 



