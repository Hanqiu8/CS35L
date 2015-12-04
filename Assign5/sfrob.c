#include <stdio.h>
#include <stdlib.h>

int frobcmp (const void *a, const void *b)
{
  const char *p1 = *(const char**)a;
  const char *p2 = *(const char**)b;
  int n1 = 0;
  int n2 = 0;
  while (p1[n1] != '\0' && p2[n2] != '\0')
    {
      if ((p1[n1] ^ 42) > (p2[n2] ^ 42))
	return 1;
      else if ((p1[n1] ^ 42) < (p2[n2] ^ 42))
	return -1;
      else
	{n1++;n2++;}
    }
    if (p1[n1] == '\0' && p2[n2] == '\0')
      return 0;
    else if (p2[n2] == '\0')
      return 1;
    else
      return -1;
}

int main (){

  int wordnum=0;
  int charnum=0;
  int charsize = sizeof(char);
  int pointersize = sizeof(char*);
  char **allwords = malloc(0);
  char *word = malloc(0);
  
  char c = getchar();

  while (c != EOF)
    {
      charnum++;
      word = realloc(word, charsize*charnum);
      if (word == NULL)
      	{
      	  fprintf(stderr, "Memory allocation error");
      	  exit(1);
      	}
      word[charnum-1] = c;
	 	  
      if (c == ' ')
	{
	  wordnum++;
	  allwords = realloc(allwords, pointersize*wordnum);
	  if (allwords == NULL)
	    {
	      fprintf(stderr, "Memory allocation error");
	      exit(1);
	    }
	  allwords[wordnum-1] = word;
	  charnum = 0;
	  word = malloc(0);
	  }
       c = getchar();
     }
  //for cases if the stdin doesn't end in a space
  if (charnum != 0)
    {
      charnum++;
      word = realloc(word, charsize*charnum);
      if (word == NULL)
      	{
      	  fprintf(stderr, "Memory allocation error");
      	  exit(1);
      	}
      word[charnum-1] = ' ';
      wordnum++;
      allwords = realloc(allwords, pointersize*wordnum);
      if (allwords == NULL)
      	{
      	  fprintf(stderr, "Memory allocation error");
      	  exit(1);
      	}
      allwords[wordnum-1] = word;
      charnum = 0;
      //no need to clear word string since end of file
      
    }

  //sorting time
  qsort (allwords, wordnum, pointersize, frobcmp);
  int n ,m;
  for ( n = 0; n != wordnum; n++)
    {
      for (m = 0; allwords[n][m] != '\0'; m++)
	printf( "%c" , allwords[n][m]);
    }
  int i;
  if(allwords != NULL){
  for(i = 0; i!=wordnum; i++)
    {
      free(allwords[i]);
    }}
  free(allwords);
  free(word);
    
  /* const char *m1 = malloc(3*sizeof(char));
  const char *m2 = malloc(3*sizeof(char));
  *m1 = "car";
  *m2 = "but";
  frobcmp(m1, m2);
  free(m1);
  free(m2);*/
  return 0;
}


