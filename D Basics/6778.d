import std.stdio;
//import std.math;

void main(){
    
    int a,e;
	readf!"%d\n%d"(a,e);
    
    if (3<=a && e<=4){
        writeln("TroyMartian");
    }
    if (a<=6 && 2<=e){
        writeln("VladSaturnian");
    }
    if (a<=2 && e<=3){
        writeln("GraemeMercurian");
    }
}
