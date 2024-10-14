


Branching Commands









 


Branching Commands















Branching controls the flow of execution in your script. It allows you to branch into separate logical sequences based on logical conditions.


 


The if Statement
----------------


An if statement allows you to execute different paths of logic depending on a given condition.


 




| ns |
| --- |
| // Single case condition
int x = 0;
if (x == 0)
{
     Print("NinjaTrader");
} |



 


The above example will print "NinjaTrader" to the NinjaScript Output window, since x is equal to 0.


 




| ns |
| --- |
| // Either/Or decision
int x = 1;
if (x == 0)
{
     Print("NinjaTrader");
}
else
{
     Print("NinjaScript");
} |



 


The above example will print "NinjaScript" to the NinjaScript Output window, since x is not equal to 0.


 




| ns |
| --- |
| // Multiple case decision
int x = 2;
if (x == 0)
{
     Print("NinjaTrader");
}
else if (x == 1)
{
     Print("NinjaScript");
}
else
{
     Print("My Algorithm");
} |



 


The above example will print "My Algorithm" to the NinjaScript Output window, since x is not equal to either 0 or 1.


 



The switch Statement
--------------------


The switch statement executes a set of logic depending on the value of a given parameter.


 




| ns |
| --- |
| // Switch example
int x = 2;
switch (x)
{
     case 0:
         Print("x is equal to zero");
         break;
     case 1:
         Print("x is equal to one");
         break;
     case 2:
         Print("x is equal to two");
         break;
} |



 


The above example will print out "x is equal to two" to the NinjaScript Output window. The other two case statements will not be executed, since their conditions do not evaluate to true.





 
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
 
 
 



