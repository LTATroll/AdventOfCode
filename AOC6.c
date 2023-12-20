#include <stdio.h>
#include <stdlib.h>

void main(){
    int numberofraces;
    numberofraces = 1;
    long long int time[] = {53717880};
    long long int distance[] = {275118112151524};
    long long int distancecoverd;
    long long int *totaldifferntwins;
    long long int answer;
    printf("%d",sizeof(long int));
    totaldifferntwins = malloc(sizeof(long long int) * numberofraces);
    for(int i = 0; i < numberofraces; i++){
        totaldifferntwins[i] = 0;
        for(int j = 0; j < time[i]; j++){
            distancecoverd = j * (time[i] - j);
            if(distance[i] < distancecoverd){
                totaldifferntwins[i]++;
            }
        }
        printf("\n%d\n", totaldifferntwins[i]);
    }
    answer = totaldifferntwins[0];
    for(int i = 1; i < numberofraces; i++){
        answer = answer * totaldifferntwins[i];  
    }
    printf("\n%d\n", answer);
    free(totaldifferntwins);
}