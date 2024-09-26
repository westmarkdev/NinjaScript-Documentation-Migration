


FillRectangle()









 


FillRectangle()















Definition
Draws a rectangle between two points.
------------------------------------------------


 


Syntax
------


RenderTarget.FillRectangle(RectangleF rect, Brush brush)
--------------------------------------------------------



Parameters
----------




|  |  |
| --- | --- |
| rect | A RectangleF representing the rectangle to be drawn |
| brush | A Brush representing the brush to draw with |



 




Examples
--------




| ns |
| --- |
|  | RectangleF rect = new RectangleF();
 
rect.X      = rectX;
rect.Y      = rectY;
rect.Width  = rectWidth;
rect.Height = rectHeight;
 
RenderTarget.FillRectangle(rect, brush); |






 
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
 
 
 



