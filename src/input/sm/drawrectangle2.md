


DrawRectangle()









 


DrawRectangle()















Definition
Draws a rectangle between two points.
------------------------------------------------


 


Syntax
------


RenderTarget.DrawRectangle(RectangleF rect, Brush brush)
--------------------------------------------------------


RenderTarget.DrawRectangle(RectangleF rect, Brush brush, float strokeWidth)
RenderTarget.DrawRectangle(RectangleF rect, Brush brush, float strokeWidth, StrokeStyle strokeStyle)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Parameters
----------




|  |  |
| --- | --- |
| rect | A RectangleF representing the rectangle to be drawn |
| brush | A Brush representing the brush to draw with |
| strokeWidth | A float representing the width of the stroke |
| strokeStyle | A StrokeStyle representing the stroke's style |



 




Examples
--------




| ns |
| --- |
|  | RectangleF rect = new RectangleF();
 
rect.X      = rectX;
rect.Y      = rectY;
rect.Width  = rectWidth;
rect.Height = rectHeight;
 
RenderTarget.DrawRectangle(rect, Stroke.BrushDX, Stroke.Width, Stroke.StrokeStyle); |






 
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
 
 
 



