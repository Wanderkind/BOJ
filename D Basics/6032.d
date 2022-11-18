import std.stdio;
//import std.algorithm;
import std.conv;
//import std.numeric;
//import std.range;
//import std.array;
//import std.bigint;
//import std.string;

void main(){
    
    int ind1, ind2, ind3;
    double prc1, prc2, prc3;
    double hpp1 = 0, hpp2 = 0, hpp3 = 0;
    double j,p,h;
    
    int n;
    scanf("%d",&n);
    foreach(i;0..n){

        scanf("%lf %lf", &j, &p);
        h = j/p;

        if(h>hpp1){
            ind3 = ind2;
            ind2 = ind1;
            ind1 = i+1;
            prc3 = prc2;
            prc2 = prc1;
            prc1 = p;
            hpp3 = hpp2;
            hpp2 = hpp1;
            hpp1 = h;
        }
        else if(h>hpp2){
            ind3 = ind2;
            ind2 = i+1;
            prc3 = prc2;
            prc2 = p;
            hpp3 = hpp2;
            hpp2 = h;
        }
        else if(h>hpp3){
            ind3 = i+1;
            prc3 = p;
            hpp3 = h;
        }
    }

    writeln(to!int(prc1 + prc2 + prc3));
    writeln(ind1);
    writeln(ind2);
    writeln(ind3);
}
