


Looping Commands









 


Looping Commands















Looping commands control execution flow of your script. If you wanted to print the word NinjaTrader 100 times, you could either use 100 lines of code or do the same using a looping command in only a few lines of code.


 


While Loop
----------


 


while (Boolean expression)


{


     //Do something here


}


 




| ns |
| --- |
| // Print NinjaTrader 100 times to the output window
int x = 0;
while (x &lt; 100)
{
     Print("NinjaTrader");
     x = x + 1;
} |



 


Do While Loop
-------------


 


do


{


     //Do something here


}


while (Boolean expression)


 




| ns |
| --- |
| // Print NinjaTrader 100 times to the output window
int x = 0;
do
{
     Print("NinjaTrader");
     x = x + 1;
}
while (x &lt; 100) |



 


For Loop
--------


 


for (initializer; boolean expression; iterator)


{


     //Do something here


}


 




| ns |
| --- |
| // Print NinjaTrader 100 times to the output window
for (int x = 0; x &lt; 100; x++)
{
     Print("NinjaTrader");
} |



 


Foreach Loop
------------


 


foreach (type identifier in boolean expression)


{


     // Do something here


}


 




| ns |
| --- |
| // Count the number of oatmeal cookies in a cookie jar
int oatmealCookies = 0;
foreach (cookie in cookieJar)
{
     if (cookie.Type == Oatmeal)
     {
         oatmealCookies = oatmealCookies + 1;
     }
}
Print("There are " + numberOatmeal.ToString() + "oatmeal cookies in the cookie jar."); |



 


Break and Continue
------------------


 


You can use the break command to exit a loop at any time. The following example is an infinite loop, but we will break out after the first Print statement.


 




| ns |
| --- |
| // Exit the infinite loop after the first iteration
while (0 == 0)
{
     Print("NinjaTrader");
     break;
} |



 


The continue command will jump ahead to the next iteration of the loop. The following example will never print "NinjaTrader," because the continue command sends control back to the top of the loop each time.


 




| ns |
| --- |
| // Never prints "NinjaTrader"
for (int x = 0; x &lt; 100; x++)
{
     continue;
     Print("NinjaTrader");
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
 
 
 



