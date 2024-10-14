










 


FormatPriceMarker()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?formatpricemarker.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
FormatPriceMarker() | [Previous page](chart_zorder.htm)
[Return to chapter overview](chart.htm)










Definition
----------


Used to override the default string format of a NinjaScript's price marker values. 



Method Return Value
-------------------


A [virtual](https://msdn.microsoft.com/en-us/library/9fkccyh4.aspx) string which is overridden from the default price marker value


 


Syntax
------


You must override the method in your indicator with the following syntax


public override string FormatPriceMarker(double price)  

{


 


}


 


Parameters
----------




|  |  |
| --- | --- |
| price | A double value representing the value to be overridden. |



 


 




|  |
| --- |
| Tip: Standard Numeric Format Strings examples can be found on Microsoft's Developer Network ([MSDN article](https://msdn.microsoft.com/en-us/library/dwhawy9k%28v=vs.110%29.aspx)) |



 


 


Examples
--------




| ns |
| --- |
| // FormatPriceMarker method of a custom indicator
public override string FormatPriceMarker(double price)
{
     // Formats price marker values to 4 decimal places
     return price.ToString("N4");
}      
 
protected override void OnBarUpdate()
{
   // overriding FormatPriceMarker will ensure display of 4 decimal places
   MyPlot[0] = (Close[0] + Open[0] * .0025);  
} |






 
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
 
 
 



