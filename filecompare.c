#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <err.h>
#include <error.h>
#include <unistd.h>

#define BLOCKSIZE 16384

void help(){
  printf("%s\n", "Usage: filecompare: f1 f2");
  exit(-2);
}

void myerr(char* custerr, int errnum){
  printf("%s\n", custerr);
  //err(errnum, NULL);
  if(errnum!=-1)error(0, errnum, NULL);
}

int main (int argc, char* argv[]){
  int ev=0;
  if(argc!=3)help();
  FILE *f1, *f2;
  if((f1=fopen(argv[1], "r"))==NULL){ev=-1; myerr("Cannot open argument 1.", errno);}
  if((f2=fopen(argv[2], "r"))==NULL){ev=-1; myerr("Cannot open argument 1.", errno);}
  int ss1, ss2, fe1, fe2, mincharnum, j=0;
  unsigned long int i=0;
  char *s1, *s2, *es;
  if((s1=(char*)malloc(BLOCKSIZE))==NULL){ev=-1; myerr("malloc err while allocing s1", errno);}
  if((s2=(char*)malloc(BLOCKSIZE))==NULL){ev=-1; myerr("malloc err while allocing s2", errno);}
  if((es=(char*)malloc(BLOCKSIZE))==NULL){ev=-1; myerr("malloc err while allocing es", errno);}
  if(ev==0)while(!feof(f1) && !feof(f2)){
    ss1=(int)read(fileno(f1), (void*)s1, BLOCKSIZE);
    ss2=(int)read(fileno(f2), (void*)s2, BLOCKSIZE);
//    ss1*=BLOCKSIZE;
//    ss2*=BLOCKSIZE;
//    printf("%s %i %i %i, %i, %i\n", "DEBUG: READ SIZES:", ss1, ss2, i, feof(f1), feof(f2));
    if((fe1=ferror(f1))!=0){ev=-1; myerr("error reading f1", errno); break;}
    if((fe2=ferror(f2))!=0){ev=-1; myerr("error reading f2", errno); break;}
    if(ss1<ss2)mincharnum=ss1;
    else mincharnum=ss2;
    i+=mincharnum;
    if(ss1!=ss2){ev=-1; myerr("files are not equal lenght", -1); break;}
    if(mincharnum<1){ev=-1; myerr("Cannot read from the shorter file", -1); break;}
    for(j=0;j<mincharnum;j++)
      if(s1[j]!=s2[j]){
        sprintf(es, "diff @ %lu bytes (%u vs. %u)\n", (unsigned long int)(i+j), (unsigned int)s1[j], (unsigned int)s2[j]);
        myerr(es, -1);
        ev=-1;
      }
  }
  free(s1);
  free(s2);
  free(es);
  if(ev==0 && feof(f1) && feof(f2))printf("%s\n", "everything is all right");
  else printf("%s\n", "one file is shorter, or error happened");
  fclose(f1);
  fclose(f2);
  return(ev);
}
