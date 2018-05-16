#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int nlabels(char * filename){
  int i = 0, j = 0;
  float f;
  FILE *data_file;
  int * labels, *buffer;
  char data_filename[50], c;
  int data_size, data_labels,data_features;
  strcpy(data_filename,"data/");
  strcat(data_filename,filename);
  data_file=fopen(data_filename, "r");
  fscanf(data_file,"%c %d \n", &c, &data_size);
  fscanf(data_file,"%c %d \n", &c, &data_features);
  fscanf(data_file,"%c %d \n", &c, &data_labels);

  labels = (int *) malloc(data_labels*sizeof(int));
  buffer = (int *) malloc(data_labels*sizeof(int));
  if(labels == NULL || buffer == NULL){
    printf("Error in malloc\n");
    return 0;
  }
  /*Initializing array of labels*/
  for(i = 0; i<data_labels; i++){
    labels[i]=0;
    buffer[i]= 0;
  }
  printf("Numero de Lineas: %d \n", data_size);
  printf("Numero de elementos: %d\n", data_features );
  printf("Numero de etiquetas: %d\n",data_labels );

  /*Seek labels*/
for(j = 0; j < data_size; j++){
  for(i = 0; i<data_features;i++){
    fscanf(data_file, "%f",&f);
    //printf("%d: %f\n", i, f);
  }
  for(i = 0; i<data_labels;i++){
    fscanf(data_file, "%d", buffer+i);
    //printf("%d: %d \n", i, buffer[i]);
    labels[i] = labels[i]+buffer[i];
  }
  //fread(labels, sizeof(int), sizeof(int)*data_labels, data_file);
}
  for( i = 0; i<data_labels;i++){
    printf("Etiqueta %d:%d veces\n", i+1, labels[i]);
  }


}
