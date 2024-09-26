










 


RenderTarget







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?rendertarget.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
RenderTarget | [Previous page](panelui.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


A SharpDX Direct2D1 RenderTarget creates objects and exposes methods used for drawing in the chart area.  


 




|  |
| --- |
| Notes:  
1.There are two RenderTarget's used in a chart.  This is important to understand when creating/destroying device resources.  Please see the [OnRenderTargetChanged()](onrendertargetchanged.htm) page for more information2.For a walk through for using the SharpDX RenderTarget, please see the educational resource [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering.htm) |





Property Value
--------------


A [SharpDX.Direct2D1.RenderTarget](sharpdx_direct2d1_rendertarget.htm)


 




|  |  |
| --- | --- |
| SharpDX.Direct2D1.WindowRenderTarget  | Used to render the actual contents of the chart to the window |
| SharpDX.Direct2D1.WicRenderTarget | Used to render a bitmap for a few scenarios:
 
1.  A user clicks on a chart area; a bitmap is used to do any hit detection to determine where the user clicked
 
2.  User clicks on the Windows task bar; a bitmap is used to rendered the preview the contents of the chart display through a thumbnail on the task bar
 
3.  A user re-sizes the chart; a bitmap is used to render the current contents of the chart, which is redrawn using the WindowRenderTarget after the desired changes have been set |



 


 


Syntax
------


RenderTarget


 




|  |
| --- |
| Warning:  Each DirectX render target requires its own brushes. You must create a brushes directly in [OnRender()](onrender.htm) or using [OnRenderTargetChanged()](onrestorevalues.htm).  If you do not you will receive an error at run time similar to: 
 
"A direct X error has occured while rendering the chart: HRESULT: [0x88990015], Module: [SharpDX.Direct2D1], ApiCode: [D2DERR\_WRONG\_RESOURCE\_DOMAIN/WrongResourceDomain], Message: The resource was realized on the wrong render target. : Each DirectX render target requires its own brushes. You must create brushes directly in OnRender() or using OnRenderTargetChanged().
 
Please see [OnRenderTargetChanged()](onrendertargetchanged.htm) for examples with brush that needs to be recalculated, or [OnRender()](onrender.htm) for an example of recreating a static brush. |






 
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
 
 
 



