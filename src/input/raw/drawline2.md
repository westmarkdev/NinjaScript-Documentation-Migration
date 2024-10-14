


DrawLine()









 


DrawLine()















Definition
Draws a line between two points.
-------------------------------------------


 


Syntax
------


RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush)
------------------------------------------------------------------


RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush, float strokeWidth) 
RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush, float strokeWidth, StrokeStyle strokeStyle)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Parameters
----------




|  |  |
| --- | --- |
| point0 | A Vector2 representing the first point to draw between |
| point1 | A Vector2 representing the second point to draw between |
| brush | A Brush representing the brush to draw with |
| strokeWidth | A float representing the width of the stroke |
| strokeStyle | A StrokeStyle representing the stroke's style |



 




Examples
--------




| ns |
| --- |
|  | Vector2 point0 = new Vector2();
Vector2 point1 = new Vector2();
 
point0.X = point0X;
point0.Y = point0Y;
point1.X = point1X;
point1.Y = point1Y;
 
RenderTarget.DrawLine(point0, point1, Stroke.BrushDX, Stroke.Width, Stroke.StrokeStyle); |






 
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
 
 
 



