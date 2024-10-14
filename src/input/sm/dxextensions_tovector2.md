










 


ToVector2()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?dxextensions_tovector2.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt; [DxExtensions](dxextensions.htm) &gt;
ToVector2() | [Previous page](dxextensions_todxbrush.htm)
[Return to chapter overview](dxextensions.htm)










Definition
----------


Converts a System.Windows.Point structure to a SharpDX.Vector2 used for [SharpDX rendering](using_sharpdx_for_custom_chart_rendering.htm).



Method Return Value
-------------------


A new [SharpDX.Vector2](sharpdx_vector2.htm) constructed with the point parameters X and Y values



Syntax
------


DxExtensions.ToVector2(this System.Windows.Point point)  

<point>.ToVector2()


 


Parameters
----------




|  |  |
| --- | --- |
| point | The [System.Windows.Point](https://msdn.microsoft.com/en-us/library/system.windows.point(v=vs.110).aspx) point to convert |





Example
-------




| ns |
| --- |
| // gets the application/user WPF point and converts to a SharpDX Vector 
System.Windows.Point wpfPoint = ChartControl.MouseDownPoint;
 
SharpDX.Vector2 dxVector2 = wpfPoint.ToVector2(); |






 
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
 
 
 



</point>